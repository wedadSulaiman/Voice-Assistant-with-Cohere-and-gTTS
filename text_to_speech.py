from gtts import gTTS
import pygame
import tempfile
import time

def speak_text(text, lang='ar'):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang=lang)
        tts.save(fp.name)
        fp_path = fp.name

    pygame.mixer.init()
    pygame.mixer.music.load(fp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.stop()


