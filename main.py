from record_audio import record_audio
from transcribe import transcribe_audio
from chatbot import get_bot_reply
from text_to_speech import speak_text

# تسجيل صوت المستخدم
record_audio()

# تحويل الصوت إلى نص
user_text = transcribe_audio()
print("🗣️ Say:", user_text)

# إرسال إلى Cohere والطلب منه الرد بالعربية فقط
reply = get_bot_reply(user_text)
print("🤖 Assistant response:", reply)

# تشغيل الرد بصوت عربي مباشرة
speak_text(reply)

