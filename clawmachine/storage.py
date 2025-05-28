import os
import json
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data.json')

DEFAULT_DATA = {
    "promotions": {"1000": 55, "2000": 115, "4000": 240},
    "cash_ins": [],
    "machines": [],
    "stock_entries": [],
    "plays": []
}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_DATA.copy()

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
