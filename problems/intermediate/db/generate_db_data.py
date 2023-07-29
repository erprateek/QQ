import sqlite3
import random
import os

# Function to create the SQLite database and tables
def create_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'employees' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
    """)

    # Create the 'departments' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
    """)

    conn.commit()
    conn.close()

# Function to generate random employee data
def generate_employee_data():
    first_names = ["John", "Jane", "Michael", "Emily", "William", "Sophia", "Robert", "Olivia"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
    departments = ["HR", "Engineering", "Finance", "Marketing", "Sales"]
    locations = ["New York", "San Francisco", "Chicago", "Los Angeles", "Seattle"]

    employees = []
    for i in range(1, 101):
        name = random.choice(first_names) + " " + random.choice(last_names)
        age = random.randint(22, 60)
        department = random.choice(departments)
        salary = round(random.uniform(50000, 100000), 2)
        employees.append((i, name, age, department, salary))

    return employees

# Function to generate random department data
def generate_department_data():
    departments = ["HR", "Engineering", "Finance", "Marketing", "Sales"]
    locations = ["New York", "San Francisco", "Chicago", "Los Angeles", "Seattle"]

    return [(i, department, random.choice(locations)) for i, department in enumerate(departments, start=1)]

# Function to insert data into the 'employees' table
def insert_employee_data(db_path, employees_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO employees (id, name, age, department, salary) VALUES (?, ?, ?, ?, ?)", employees_data)

    conn.commit()
    conn.close()

# Function to insert data into the 'departments' table
def insert_department_data(db_path, departments_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO departments (id, name, location) VALUES (?, ?, ?)", departments_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_path = "sample_data.db"
    if os.path.exists(db_path):
        os.remove(db_path)  # Remove the database if it already exists

    create_database(db_path)

    employee_data = generate_employee_data()
    department_data = generate_department_data()

    insert_employee_data(db_path, employee_data)
    insert_department_data(db_path, department_data)

    print("Sample data has been successfully generated and inserted into the database.")
