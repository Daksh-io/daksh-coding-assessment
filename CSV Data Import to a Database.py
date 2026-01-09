# Note- CSV & Database are assumed, is not real.
# This is a placeholder for the actual implementation.
# Hope all the doubts are cleared because I'm using my real old & modify code okay.

import csv
import sqlite3

# Step 1: Initialize SQLite database.
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    return conn

# Step 2: Read data from CSV file.
def read_csv(file_path):
    users = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append({"name": row["name"], "email": row["email"]})
    return users

# Step 3: Insert data into SQLite.
def insert_users(conn, users):
    cursor = conn.cursor()
    for user in users:
        try:
            cursor.execute("""
                INSERT INTO users (name, email)
                VALUES (?, ?)
            """, (user["name"], user["email"]))
        except sqlite3.IntegrityError:
            print(f"Skipping duplicate email: {user['email']}")
    conn.commit()

# Step 4: Thier is result.
if __name__ == "__main__":
    conn = init_db()
    users = read_csv("users.csv")   # <-- Replace with your CSV file path.
    insert_users(conn, users)
    conn.close()
