from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Get absolute path of `data.json`
json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')

# Load data from JSON file
if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
else:
    data = []
    print("Error: `q-vercel-python.json` file is missing or empty.")

# Convert data into a dictionary for faster lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    
    # Preserve order by iterating in the order of query params
    marks = [marks_dict[name] for name in names if name in marks_dict]
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
