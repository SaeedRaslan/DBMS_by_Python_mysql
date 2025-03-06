# data_operations.py
from db_connection import connect_db

def insert_data(db_name, table_name, data):
    db = connect_db(db_name)
    cursor = db.cursor()
    
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())
    
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    try:
        cursor.execute(query, values)
        db.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print("Error inserting data:", e)
    finally:
        cursor.close()
        db.close()

def update_data(db_name, table_name, column, new_value, row_id):
    db = connect_db(db_name)
    cursor = db.cursor()
    try:
        cursor.execute(f"UPDATE {table_name} SET {column} = %s WHERE id = %s", (new_value, row_id))
        db.commit()
    except Exception as e:
        print("Error updating data:", e)
    finally:
        cursor.close()
        db.close()

def delete_data(db_name, table_name, row_id):
    db = connect_db(db_name)
    cursor = db.cursor()
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", (row_id,))
        db.commit()
    except Exception as e:
        print("Error deleting data:", e)
    finally:
        cursor.close()
        db.close()

def display_data(db_name, table_name):
    db = connect_db(db_name)
    cursor = db.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching data:", e)
        return []
    finally:
        cursor.close()
        db.close()
