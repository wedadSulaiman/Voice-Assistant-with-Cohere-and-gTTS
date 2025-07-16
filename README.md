# Voice Assistant using Whisper, Cohere, and gTTS

This project is a simple Arabic voice assistant that listens to your voice, understands what you say, and responds with a spoken reply in Arabic.

## Project Overview

1. The assistant records your voice through the microphone.
2. It converts your speech into text using Whisper.
3. The transcribed text is sent to Cohere's AI model, which generates a smart and relevant response.
4. The response is then converted into Arabic speech using gTTS.
5. The final reply is played immediately through your device's speakers.

## Technologies Used

- Whisper for speech-to-text transcription.
- Cohere for generating conversational responses.
- gTTS and pygame for text-to-speech in Arabic.
- Python with a modular design (split into multiple files).

## Project Files

- `record_audio.py`: Records audio input from the user.
- `transcribe.py`: Transcribes the audio to text.
- `chatbot.py`: Sends the transcribed text to Cohere and gets a reply.
- `text_to_speech.py`: Converts the reply text into spoken audio.
- `main.py`: Coordinates the full process in one flow.

## Demonstration

Please refer to the attached video for a full demonstration of how the assistant works from voice input to voice output in real time.


https://github.com/user-attachments/assets/66572ab9-777b-440e-97c0-6082a53f158d

