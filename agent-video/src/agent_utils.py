import json
from pathlib import Path

PATH_HISTORY = Path("histories/history.json")

def load_history():
    if PATH_HISTORY.exists():
        return json.loads(PATH_HISTORY.read_text())

    return []

def save_history(history):
    PATH_HISTORY.write_text(json.dumps(history, indent=4, ensure_ascii=False))  
