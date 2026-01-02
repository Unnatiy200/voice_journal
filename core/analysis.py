# core/analysis.py

# --- Basic mood detection (starter version) ---

MOOD_KEYWORDS = {
    "sad": ["sad", "cry", "alone", "hurt", "breakup", "down", "regret"],
    "angry": ["angry", "mad", "frustrated", "irritated"],
    "anxious": ["scared", "nervous", "anxious", "tension"],
    "stressed": ["stress", "pressure", "overwhelmed", "tired"],
    "happy": ["happy", "excited", "glad", "good", "grateful"],
    "calm": ["peaceful", "relaxed", "ok", "fine"]
}

TOPIC_KEYWORDS = {
    "relationships": ["attach", "love", "breakup", "friend", "trust", "feelings"],
    "study": ["study", "exam", "notes", "college", "assignment"],
    "career": ["job", "internship", "work", "resume", "future"],
    "health": ["gym", "sleep", "diet", "tired", "headache"],
    "money": ["money", "bills", "rent", "salary", "spend"],
    "mental_state": ["overthinking", "anxiety", "stress", "thoughts"]
}


def detect_mood(text: str):
    text_lower = text.lower()

    for mood, words in MOOD_KEYWORDS.items():
        if any(word in text_lower for word in words):
            return mood
    
    return "unknown"


def detect_topics(text: str):
    text_lower = text.lower()
    topics = []

    for topic, words in TOPIC_KEYWORDS.items():
        if any(word in text_lower for word in words):
            topics.append(topic)

    if not topics:
        topics.append("general")

    return topics


def analyze_text(text: str):
    mood = detect_mood(text)
    topics = detect_topics(text)

    return {
        "original_text": text,
        "mood": mood,
        "topics": topics,
        "summary": "analysis coming soon..."
    }
