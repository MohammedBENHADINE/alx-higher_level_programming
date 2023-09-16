#!/usr/bin/python3
"""script to list all states with name"""
import sys
import MySQLdb


def list_cities_by_state(mysql_username, mysql_password, database_name, state):
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
        query = "SELECT cities.id, cities.name \
                FROM cities JOIN states ON cities.state_id=states.id \
                WHERE states.name={} \
                ORDER BY cities.id ASC;".format(state)
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
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> \
                <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username, mysql_password, database_name, state = \
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    results = list_cities_by_state(mysql_username, mysql_password,
                                   database_name, state)

    if results:
        cities = [row[1] for row in results]
        data = ", ".join(cities)
        print(data)
