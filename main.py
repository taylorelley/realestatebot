from api_handler import APIHandler
from database_handler import DatabaseHandler
from property_analyzer import PropertyAnalyzer

def main():
    """Main function to pull data from the API, store it in the database, and analyze it."""

    # Create an APIHandler instance
    api_handler = APIHandler('http://api.realestate.co.nz/properties', {'Authorization': 'Bearer YOUR_API_KEY'})

    # Get all properties from the API
    properties = api_handler.get_properties()

    # Create a DatabaseHandler instance
    db_handler = DatabaseHandler('properties.db')

    # Create a table in the database
    db_handler.create_table('properties', ['id', 'location', 'price'])

    # Insert the properties into the database
    db_handler.insert_data('properties', properties)

    # Create a PropertyAnalyzer instance
    property_analyzer = PropertyAnalyzer(db_handler)

    # Find undervalued properties
    undervalued_properties = property_analyzer.find_undervalued_properties('properties')

    print(undervalued_properties)

if __name__ == "__main__":
    main()
