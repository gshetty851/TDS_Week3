from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [entry['marks'] for entry in data if entry['name'] in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
