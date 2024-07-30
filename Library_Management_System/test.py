import os
import sqlite3
from pathlib import Path

# Define the directory path and database file name
base_path = Path("C:/Library Management System/Database")
db_file = base_path / "LMSDB.db"

# Create the directory if it doesn't exist
os.makedirs(base_path, exist_ok=True)

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_file)
cu = conn.cursor()
# cu.execute('create table users(name text)')
conn.close()

print(f"Database {db_file} created successfully!")
