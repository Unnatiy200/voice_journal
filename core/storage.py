# core/storage.py

import os
import json
from datetime import datetime

BASE_DIR = "data/journal"


def ensure_folder():
    os.makedirs(BASE_DIR, exist_ok=True)


def save_journal_entry(entry: dict):
    """
    Save structured journal entry as a JSON file.
    """
    ensure_folder()

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False, indent=2)

    return filepath
