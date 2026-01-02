# core/reminders.py

import json
import os
import re
from datetime import datetime, timedelta

REMINDERS_FILE = "data/reminders.json"


def load_reminders():
    if not os.path.exists(REMINDERS_FILE):
        return []

    with open(REMINDERS_FILE, "r") as f:
        return json.load(f)


def save_reminders(reminders):
    with open(REMINDERS_FILE, "w") as f:
        json.dump(reminders, f, indent=2)


def detect_followup(text: str):
    """
    Detect statements like:
    - kal se start karungi
    - tomorrow I will do it
    """

    text_lower = text.lower()

    patterns = [
        r"kal se",
        r"kal .* kar(unga|ungi|na)",
        r"tomorrow",
        r"from tomorrow",
        r"start (from )?tomorrow"
    ]

    if any(re.search(p, text_lower) for p in patterns):
        reminder = {
            "text": text,
            "due_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "checked": False
        }
        return reminder

    return None
