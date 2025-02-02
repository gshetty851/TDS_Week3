from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Get absolute path of `data.json`
json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

# Load JSON data correctly
try:
    if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = []
        print("Error: `data.json` file is missing or empty.")
except json.JSONDecodeError as e:
    data = []
    print("Error decoding JSON:", str(e))

# Convert data into a dictionary for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get names from query parameters
    
    # Ensure order is maintained as in the request
    marks = [marks_dict[name] for name in names if name in marks_dict]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
