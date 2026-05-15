"""
Connecting to the data, reading and basic funcs.
"""

import json
from pathlib import Path
from typing import List, Dict, Any

DATA_PATH = Path(__file__).parent.parent / "data" / "products.json"

def load_products() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def get_products() -> List[Dict[str, Any]]:
    return load_products()
