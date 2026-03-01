import whisper

model = whisper.load_model("small")  

def transcribe_audio(path, language=None):
    result = model.transcribe(path, language=language, verbose=False)
    return result