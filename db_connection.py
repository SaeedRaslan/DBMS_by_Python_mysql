# db_connection.py
import mysql.connector

def connect_server():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="00000000"
    )

def connect_db(db_name):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="00000000",
        database=db_name
    )