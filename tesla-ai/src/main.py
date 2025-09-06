import openai
import whisper
from gtts import gTTS
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Whisper model
model = whisper.load_model("base")

def listen():
    # Record audio or load a file
    pass

def respond_to_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Nikola Tesla. Answer questions about electricity, inventions, or your life."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")  # Requires mpg123 installed

if __name__ == "__main__":
    question = input("Ask Tesla: ")  # Replace with voice input later
    answer = respond_to_question(question)
    print(f"Tesla: {answer}")
    speak(answer)
