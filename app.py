import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
st.markdown("""
<style>
    /* Main background and text color */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Style the main title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F8F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    /* Subtitle styling */
    .sub-title {
        font-size: 1.1rem;
        color: #A0AEC0;
        margin-bottom: 2rem;
    }
    /* Style the audio player */
    audio {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- APP SETUP ---
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# --- UI HEADER ---
st.markdown('<p class="main-title">🎙️ El Summarizer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Capture your thoughts. Let AI do the heavy lifting.</p>', unsafe_allow_html=True)

# --- USER CONTROLS ---
# Add a dropdown so the user can control the AI's behavior
col1, col2 = st.columns([1, 1])
with col1:
    summary_style = st.selectbox(
        "Choose output format:",
        ["Action Items (Bulleted)", "Executive Summary (Paragraph)", "Email Draft"]
    )

# --- AUDIO INPUT ---
st.write("---")
audio_value = st.audio_input("Record a voice note")
uploaded_file = st.file_uploader("Or upload an audio file", type=["wav", "mp3", "m4a"])

audio_source = audio_value or uploaded_file

# --- PROCESSING LOGIC ---
if audio_source:
    st.success("Audio locked in! Processing...")
    
    # 🌟 NEW FEATURE: Let the user play back their own audio
    st.audio(audio_source)
    
    audio_source.name = "recording.wav"
    
    with st.spinner("Transcribing your audio..."):
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3", 
            file=audio_source
        )
        
        with st.expander("📝 View Raw Transcription"):
            st.write(transcript.text)
        
    with st.spinner(f"Crafting your {summary_style.lower()}..."):
        
        system_prompt = f"You are an expert assistant. Process the following text and format it as: {summary_style}."
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": transcript.text}
            ]
        )
        
        final_text = response.choices[0].message.content
        
        st.subheader("✨ Final Result")
        st.write(final_text)
        
        st.download_button(
            label="💾 Download Summary",
            data=final_text,
            file_name="el_summarizer_output.txt",
            mime="text/plain"
        )