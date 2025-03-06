from db_connection import connect_db

def list_tables(db_name):
    db = connect_db(db_name)
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    db.close()
    return tables

def get_table_columns(db_name, table_name):
    db = connect_db(db_name)
    cursor = db.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]
    db.close()
    return columns

def create_table(db_name, table_name, columns):
    db = connect_db(db_name)
    cursor = db.cursor()
    
    # وضع "id" كأول عمود في الجدول
    columns_sql = "id INT AUTO_INCREMENT PRIMARY KEY, " + ", ".join(columns)
    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")
    
    db.close()

def add_column(db_name, table_name):
    db = connect_db(db_name)
    cursor = db.cursor()
    
    column_name = input("Enter column name: ")
    column_type = input(f"Enter data type for {column_name} (e.g., VARCHAR(100), INT, etc.): ")
    column_def = f"{column_name} {column_type}"
    
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_def}")
    
    db.close()

def delete_table(db_name, table_name):
    db = connect_db(db_name)
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    db.close()
