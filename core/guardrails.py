# core/guardrails.py

# Words that hint the situation is emotional, heavy, or complicated

SENSITIVE_KEYWORDS = [
    "breakup", "cry", "alone", "hopeless",
    "hurt", "fight", "argument",
    "useless", "regret", "guilty",
    "anxiety", "overthinking", "tension",
    "can't handle", "giving up"
]


def needs_friend_support(text: str) -> bool:
    text_lower = text.lower()

    return any(word in text_lower for word in SENSITIVE_KEYWORDS)


def friend_message():
    return (
        "Lagta hai ye thoda heavy lag raha hai. "
        "Main yahan hoon — maine entry save kar di. "
        "Par shayad is baat par apni kisi close friend se baat karna better rahega. "
        "Wo tumhe zyada ache se samjhegi."
    )
