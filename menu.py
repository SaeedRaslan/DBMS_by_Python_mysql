from db_managment import list_databases, create_database, delete_database
from table_managment import list_tables, get_table_columns, create_table, delete_table
from data_operation import insert_data, update_data, delete_data, display_data

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. List Databases")
        print("2. Create Database")
        print("3. Use Database")
        print("4. Delete Database")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("Databases:", list_databases())
        elif choice == "2":
            db_name = input("Enter new database name: ")
            create_database(db_name)
        elif choice == "3":
            db_name = input("Enter database name to use: ")
            if db_name in list_databases():
                table_menu(db_name)
            else:
                print("Database does not exist!")
        elif choice == "4":
            db_name = input("Enter database name to delete: ")
            delete_database(db_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

def table_menu(db_name):
    while True:
        print("\nTable Menu:")
        print("1. List Tables")
        print("2. Create Table")
        print("3. Use Table")
        print("4. Delete Table")
        print("5. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("Tables:", list_tables(db_name))
        elif choice == "2":
            table_name = input("Enter new table name: ")
            columns = []
            while True:
                col_name = input("Enter column name (or type 'done' to finish): ")
                if col_name.lower() == "done":
                    break
                col_type = input(f"Enter data type for {col_name} (e.g., VARCHAR(100), INT, etc.): ")
                columns.append(f"{col_name} {col_type}")
            create_table(db_name, table_name, columns)
        elif choice == "3":
            table_name = input("Enter table name to use: ")
            print("Columns:", get_table_columns(db_name, table_name))
            data_menu(db_name, table_name)
        elif choice == "4":
            table_name = input("Enter table name to delete: ")
            delete_table(db_name, table_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

def data_menu(db_name, table_name):
    while True:
        print("\nData Menu:")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Display Data")
        print("5. Back")
        choice = input("Enter choice: ")
        
        if choice == "1":
            columns = get_table_columns(db_name, table_name)
            if "id" in columns:
                columns.remove("id")  # إزالة العمود التلقائي "id"
            values = []
            for col in columns:
                value = input(f"Enter value for {col}: ")
                values.append(value)
            insert_data(db_name, table_name, dict(zip(columns, values)))
        elif choice == "2":
            row_id = input("Enter row ID to update: ")
            column = input("Enter column to update: ")
            new_value = input("Enter new value: ")
            update_data(db_name, table_name, column, new_value, row_id)
        elif choice == "3":
            row_id = input("Enter row ID to delete: ")
            delete_data(db_name, table_name, row_id)
        elif choice == "4":
            print("Data:", display_data(db_name, table_name))
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
