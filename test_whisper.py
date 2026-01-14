from core.speech import audio_to_text

text = audio_to_text("test_audio.opus")
print("Whisper heard:", text)
