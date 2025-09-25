import json

def load_json_data(path):
    """Loads data from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)