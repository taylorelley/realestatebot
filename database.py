import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('realestate.db')

    def store_data(self, data):
        # Create a cursor object
        cursor = self.conn.cursor()

        # Create a table to store the data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER,
                location TEXT,
                size INTEGER
            )
        """)

        # Insert the data into the table
        for property in data:
            cursor.execute("""
                INSERT INTO properties (name, price, location, size)
                VALUES (?, ?, ?, ?)
            """, (property['name'], property['price'], property['location'], property['size']))

        # Commit the changes and close the connection
        self.conn.commit()
