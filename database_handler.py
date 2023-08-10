import sqlite3
import pandas as pd

class DatabaseHandler:
    """Class to handle interactions with the database."""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def create_table(self, table_name, columns):
        """Method to create a table in the database."""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)});"
        self.conn.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        """Method to insert data into the database."""
        df = pd.DataFrame(data)
        df.to_sql(table_name, self.conn, if_exists='append', index=False)

    def get_data(self, query):
        """Method to retrieve data from the database."""
        return pd.read_sql_query(query, self.conn)
