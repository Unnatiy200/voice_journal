# core/speech.py

import whisper

# load once (slow first time)
model = whisper.load_model("small")


def audio_to_text(audio_path: str):
    """
    Convert an audio file to text (supports Hindi, Hinglish, English)
    """
    result = model.transcribe(audio_path)
    return result["text"]
