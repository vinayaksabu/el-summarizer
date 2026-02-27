import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# We are using the OpenAI library, but pointing it to Groq's free servers
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("🎙️ AI Voice Note Summarizer")
st.write("Record a quick thought or upload an audio file, and AI will transcribe and summarize it into action items.")

# 1. Give users TWO options: Record OR Upload
audio_value = st.audio_input("Record a voice note")
uploaded_file = st.file_uploader("Or upload an audio file", type=["wav", "mp3", "m4a"])

# 2. Figure out which one the user actually provided
audio_source = audio_value or uploaded_file

# 3. Process whichever one exists
if audio_source:
    st.success("Audio received! Processing...")
    
    # We need to give the audio file a fake name so Groq knows it's an audio file
    audio_source.name = "recording.wav"
    
    with st.spinner("Transcribing your audio..."):
        # Using Groq's completely free Whisper model
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3", 
            file=audio_source
        )
        
        st.subheader("📝 Transcription")
        st.write(transcript.text)
        
    with st.spinner("Generating summary and action items..."):
        # Using Groq's newest fast Llama model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Summarize the following text briefly and pull out any clear action items in a bulleted list."},
                {"role": "user", "content": transcript.text}
            ]
        )
        
        st.subheader("✅ Summary & Action Items")
        st.write(response.choices[0].message.content)