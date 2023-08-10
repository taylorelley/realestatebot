class PropertyAnalyzer:
    """Class to analyze property data."""

    def __init__(self, db_handler):
        self.db_handler = db_handler

    def find_undervalued_properties(self, table_name):
        """Method to find undervalued properties."""
        query = f"SELECT * FROM {table_name} WHERE price < (SELECT AVG(price) FROM {table_name});"
        return self.db_handler.get_data(query)
