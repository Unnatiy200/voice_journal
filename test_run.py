from core.reminders import detect_followup

examples = [
    "Kal se main gym start karungi",
    "Tomorrow I will start studying",
    "I might do it someday"
]

for e in examples:
    print(e, "=>", detect_followup(e))
