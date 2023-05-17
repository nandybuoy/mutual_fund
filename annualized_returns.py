from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'root',
    'password': 'Pavan',
    'host': 'localhost',
    'database': 'mutual_fund_db',
    'auth_plugin': 'mysql_native_password'
}

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
                'id': row[0],
                'name': row[1],
                'description': row[2]
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
