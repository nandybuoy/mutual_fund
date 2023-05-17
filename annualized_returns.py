from flask import Flask, jsonify
import mysql.connector
from credentials import db_config

app = Flask(__name__)

# API route
@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Query to fetch data from the database
        query = "SELECT * FROM annualized_returns"

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Create a list to store the results
        results = []

        # Iterate through the rows and create a dictionary for each row
        for row in rows:
            result = {
                'index': row[0],
                '1_year': row[1],
                '2_year': row[2],
                '3_year': row[3],
                '7_year': row[4],
                '10_year': row[5],
                # Add more columns as needed
            }
            results.append(result)

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return the results as JSON
        return jsonify(results)

    except mysql.connector.Error as error:
        # Handle any errors that occur during the process
        return jsonify({'error': str(error)})

if __name__ == '__main__':
    app.run(port=8001)
    get_data()
