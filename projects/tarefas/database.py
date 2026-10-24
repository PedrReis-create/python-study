
# -*- coding: utf-8 -*-

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


# Cria uma nova conexão com o banco MySQL
def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=int(os.getenv("MYSQL_PORT"))
    )


def cadastrar_tarefa(tarefa):
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Verifica se a tarefa já existe
        cursor.execute(
            "SELECT * FROM tarefas WHERE titulo = %s",
            (tarefa,)
        )

        resultado = cursor.fetchone()

        if resultado:
            return False

        cursor.execute(
            "INSERT INTO tarefas (titulo) VALUES (%s)",
            (tarefa,)
        )

        conexao.commit()
        return True

    except mysql.connector.Error:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()

        return "Erro no servidor"

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


def listar_tarefas():
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()

        return tarefas

    except mysql.connector.Error:
        return None

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()
