import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt
from datetime import datetime, timedelta


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