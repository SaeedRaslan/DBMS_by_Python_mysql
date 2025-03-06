# db_management.py
from db_connection import connect_server

def list_databases():
    db = connect_server()
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    db.close()
    return databases

def create_database(db_name):
    db = connect_server()
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    db.close()

def delete_database(db_name):
    db = connect_server()
    cursor = db.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    db.close()