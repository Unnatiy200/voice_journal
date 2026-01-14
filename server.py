# server.py
# Central processing pipeline (text only for now)

from core.analysis import analyze_text
from core.storage import save_journal_entry
from core.guardrails import needs_friend_support, friend_message
from core.reminders import detect_followup, load_reminders, save_reminders


def process_entry(text: str):
    # 1. analyze
    result = analyze_text(text)

    entry = {
        "text": text,
        "mood": result["mood"],
        "topics": result["topics"],
        "summary": result["summary"]
    }

    # 2. save journal
    path = save_journal_entry(entry)

    # 3. friend suggestion logic
    friend_msg = None
    if needs_friend_support(text):
        friend_msg = friend_message()

    # 4. detect reminder
    new_reminder = detect_followup(text)

    if new_reminder:
        reminders = load_reminders()
        reminders.append(new_reminder)
        save_reminders(reminders)

    return {
        "saved_to": path,
        "analysis": entry,
        "friend_message": friend_msg,
        "new_reminder": new_reminder
    }


if __name__ == "__main__":
    # simple test
    print(process_entry("Kal se main serious study start karungi, abhi thoda stress ho raha hai"))
