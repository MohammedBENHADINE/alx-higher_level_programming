#!/usr/bin/python3
"""script to list all states with name"""
import sys
import MySQLdb


def list_cities(mysql_username, mysql_password, database_name):
    """function to get states from databse"""
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to retrieve states starting with 'N'
        query = "SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states on states.id=cities.state_id \
                ORDER BY cities.id ASC;"
        cursor.execute(query)

        # Fetch and return the results
        results = cursor.fetchall()
        return results

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> \
                <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username, mysql_password, database_name = \
        sys.argv[1], sys.argv[2], sys.argv[3]

    results = list_cities(mysql_username, mysql_password,
                          database_name)

    if results:
        for row in results:
            print(row)
