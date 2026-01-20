# core/speech.py

from faster_whisper import WhisperModel
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re

# More accurate than "small", still OK on CPU
model = WhisperModel("medium", device="cpu", compute_type="int8")


def is_hindi_char(char):
    return '\u0900' <= char <= '\u097F'


def contains_hindi(text):
    return any(is_hindi_char(c) for c in text)


def transliterate_hindi_to_hinglish(text: str) -> str:
    """
    Convert only Hindi-script parts to Romanized Hinglish.
    Keep English unchanged.
    """

    words = text.split()
    output_words = []

    for word in words:
        if contains_hindi(word):
            try:
                roman = transliterate(word, sanscript.DEVANAGARI, sanscript.ITRANS)
                output_words.append(roman)
            except:
                output_words.append(word)
        else:
            output_words.append(word)

    return " ".join(output_words)


def audio_to_text(audio_path: str) -> str:
    """
    Speech → Accurate transcription → Stable Hinglish
    """

    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language=None,
        task="transcribe"
    )

    raw_text = ""
    for segment in segments:
        raw_text += segment.text + " "

    raw_text = raw_text.strip()

    # Convert Hindi script → Hinglish
    final_text = transliterate_hindi_to_hinglish(raw_text)

    return final_text
