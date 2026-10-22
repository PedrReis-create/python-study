import mysql.connector
import os
from dotenv import load_dotenv



load_dotenv()


# Cria uma nova conexão com o banco MySQL
def conectar():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        port=int(os.getenv('MYSQL_PORT'))
    )

def cadastrar_tarefa(tarefa):
    try:
        conexao = conectar()
    
    except mysql.connector.Error:
        return "Erro no servidor"
    cursor = conexao.cursor()
    
    # Verifica se a tarefa já existe
    cursor.execute(
        'SELECT * FROM tarefas WHERE titulo = %s',
        (tarefa,)
    )

    resultado = cursor.fetchone()

    if resultado:
        cursor.close()
        conexao.close()
        return False
    
    cursor.execute(
        'INSERT INTO tarefas (titulo) VALUES (%s)',
        (tarefa,)
    )
    conexao.commit()

    cursor.close()
    conexao.close()

    return True