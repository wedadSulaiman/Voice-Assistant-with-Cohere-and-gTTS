import whisper

# تحميل النموذج مرة وحدة عند استيراد الملف
model = whisper.load_model("base")

def transcribe_audio(filename="input.wav"):
    result = model.transcribe(filename)
    return result["text"]
