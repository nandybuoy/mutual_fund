# {
#  "cells": [
#   {
#    "cell_type": "code",
#    #"execution_count": null,
#    "id": "22f187d9",
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "from flask import Flask, jsonify\n",
#     "from sqlalchemy import create_engine\n",
#     "import pandas as pd\n",
#     "\n",
#     "app = Flask(__name__)\n",
#     "\n",
#     "@app.route('/api/v1/returns', methods=['GET'])\n",
#     "def get_returns():\n",
#     "    engine = create_engine('mysql://root:Pavan@localhost/mutual_fund_db')\n",
#     "    query = 'SELECT * FROM annualized_returns'\n",
#     "    df = pd.read_sql_query(query, engine)\n",
#     "    return jsonify(df.to_dict(orient='records'))\n",
#     "\n",
#     "if __name__ == '__main__':\n",
#     "    app.run(debug=True)"
#    ]
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3 (ipykernel)",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.9.12"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 5
# }


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
