import sqlite3

class PropertyAnalyzer:
    def __init__(self):
        self.conn = sqlite3.connect('realestate.db')

    def find_undervalued(self):
        # Create a cursor object
        cursor = self.conn.cursor()

        # Query the database for properties that are undervalued
        cursor.execute("""
            SELECT * FROM properties
            WHERE price < (SELECT AVG(price) FROM properties)
        """)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Close the connection
        self.conn.close()

        return rows
