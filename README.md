# 🛠️ Dynamic Database Management System

## 📖 Overview
This **Dynamic Database Management System** is a Python-based project that provides an interactive command-line interface for managing MySQL databases. It allows users to create, modify, and manage databases and tables effortlessly, making database operations more intuitive and user-friendly.

---

## 🚀 Features

### 🔹 **Database Management**
- 📋 **List Databases** – View all existing databases.
- ➕ **Create a Database** – Dynamically create a new database.
- 🔄 **Use a Database** – Select an active database for operations.
- ❌ **Delete a Database** – Remove unwanted databases safely.

### 🔹 **Table Management**
- 📋 **List Tables** – Display all tables within a selected database.
- ➕ **Create Tables** – Define table structures with flexible column names and data types.
- ✏️ **Modify Tables** – Add new columns dynamically.
- ❌ **Delete Tables** – Remove tables when no longer needed.

### 🔹 **Data Operations**
- ➕ **Insert Data** – Dynamically input values based on table structure.
- ✏️ **Update Data** – Modify specific column values.
- ❌ **Delete Data** – Remove selected rows efficiently.
- 📊 **Display Data** – View stored records in a structured format.

---

## 🔧 Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/database-management.git
cd database-management
```

### 2️⃣ **Install Dependencies**
Ensure you have **Python 3.9+** and **MySQL Connector** installed.
```bash
pip install mysql-connector-python
```

### 3️⃣ **Set Up Your Database Connection**
Update the `db_connection.py` file with your **MySQL credentials**:
```python
def connect_db(db_name=None):
    return mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database=db_name
    )
```

### 4️⃣ **Run the Program**
```bash
python menu.py
```

---

## 🏗️ Project Structure
```
📂 database-management/
│── 📜 menu.py             # Main menu interface
│── 📜 db_connection.py     # MySQL connection handler
│── 📜 db_management.py     # Database-level operations
│── 📜 table_management.py  # Table-related operations
│── 📜 data_operations.py   # Data manipulation (Insert, Update, Delete)
│── 📜 README.md            # Documentation
```

---

## 🎯 How It Works

1️⃣ **Start the program (`menu.py`)**  
2️⃣ **Navigate through options** to manage databases, tables, and records.  
3️⃣ **Enter required inputs** (database name, table name, column values).  
4️⃣ **View results instantly!**  

---

## 🚀 Future Improvements
- ✅ **Graphical User Interface (GUI)**
- ✅ **Role-Based Access Control (RBAC)**
- ✅ **Cloud Database Support (AWS RDS, Azure SQL)**
- ✅ **Logging and Error Handling Enhancements**

---
