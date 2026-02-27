# 🎙️ El Summarizer

A sleek, AI-powered web application that instantly transforms spoken thoughts and audio files into structured, actionable text. Built with Python and Streamlit, El Summarizer leverages cutting-edge open-source models to provide lightning-fast transcription and intelligent summarization.

## ✨ Features

* **Dual Input Modes:** Record audio directly through your microphone or upload existing audio files (`.wav`, `.mp3`, `.m4a`).
* **Audio Playback:** Built-in audio player to review your recording before processing.
* **Intelligent Formatting:** Choose your preferred output style:
  * Action Items (Bulleted)
  * Executive Summary (Paragraph)
  * Email Draft
* **Cinematic UI:** Custom dark-mode styling and typography for a premium user experience.
* **1-Click Export:** Download your generated summaries directly as a `.txt` file.

## 🛠️ Tech Stack

* **Frontend & Backend:** [Streamlit](https://streamlit.io/) (Python)
* **Speech-to-Text (STT):** Whisper Large v3 (via Groq API)
* **Large Language Model (LLM):** Llama 3.3 70B Versatile (via Groq API)
* **Environment Management:** `python-dotenv`

## 🚀 Run it Locally

Want to run El Summarizer on your own machine? Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vinayaksabu/ai-voice-summarizer.git](https://github.com/vinayaksabu/ai-voice-summarizer.git)
   cd ai-voice-summarizer