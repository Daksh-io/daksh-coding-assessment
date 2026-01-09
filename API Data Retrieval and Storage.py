# Step 1: API Data Retrieval.
# We use "requests library" to fetch data from the API.

import requests

API_URL = "https://api.example.com/books"


def fetch_books():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()  # List of dicts
    else:
        raise Exception(f"API request failed with status {response.status_code}")


# Step 2: data storage with sqllite3.
# We use "sqlite3 library" to store data in a local database.

import sqlite3


def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
        )
    """)
    conn.commit()
    return conn


# Step 3: store data in the database okay.
# Insert all the data books data into the database.


def store_books(conn, books):
    cursor = conn.cursor()
    for book in books:
        cursor.execute(
            """
            INSERT INTO books (title, author, publication_year)
            VALUES (?,)
        """,
            (book["title"], book["author"], book["publication_year"]),
        )
    conn.commit()

# Step 4: displaying the retrieved books data.

def display_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, publication_year FROM books")
    rows = cursor.fetchall()
    print("Books in Database:")
    print("-" * 40)
    for row in rows:
        print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")

# Step 5: Now run this code okay.

if __name__ == "__main__":
    # Step 1: Fetch data
    books = fetch_books()

    # Step 2: Initialize DB
    conn = init_db()

    # Step 3: Store data
    store_books(conn, books)

    # Step 4: Display data
    display_books(conn)

    conn.close()
