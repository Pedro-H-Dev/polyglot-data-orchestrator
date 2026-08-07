import pymysql
from pymongo import MongoClient
import sys

def test_mysql():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootpassword123',
            database='app_db',
            port=3306
        )
        print("[SUCESSO] Conexão com o MySQL estabelecida com sucesso!")
        connection.close()
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao conectar no MySQL: {e}")
        return False

def test_mongodb():
    try:
        client = MongoClient(
            "mongodb://admin:adminpassword123@localhost:27017/"
        )
        # O ping força a comunicação com o servidor
        client.admin.command('ping')
        print("[SUCESSO] Conexão com o MongoDB estabelecida com sucesso!")
        client.close()
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao conectar no MongoDB: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando auditoria dos motores de banco de dados (PolyGlot Data Orchestrator)...\n")
    
    mysql_ok = test_mysql()
    mongo_ok = test_mongodb()
    
    if mysql_ok and mongo_ok:
        print("\n[STATUS GERAL] Todos os bancos de dados estão operacionais e saudáveis!")
    else:
        print("\n[STATUS GERAL] Há falhas em um ou mais serviços de banco de dados.")
        sys.exit(1)