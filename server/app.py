from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API route
@app.route('/')
def get_home():
    return "Go to /data"
    

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Fetching all data from annualized returns 
        data = annualized_data_collection.find({}, {'_id': False})

        results = []
        
        for document in data:
            results.append(document)

        # returning the data
        return results

    except Exception as e:
        # Handle any errors that occur during the process
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    
    # Connecting to Mongodb
    try:
        client = MongoClient('mongodb+srv://nanditanandath:nandita@cluster0.zv8xtm0.mongodb.net/?retryWrites=true&w=majority')
        db = client['mutual_funds']
        monthly_collection = db['mutual_funds_monthly']
        annualized_data_collection = db['mutual_funds_annualized']
        print("Connected to MongoDB successfully!")
    
    except Exception as e:
        print("Error connecting to MongoDB:", str(e))

    ##run the flask app
    app.run(port=8001)
