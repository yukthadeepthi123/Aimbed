
# 🩺 VoiceDoc AI

🎤 Convert doctor’s voice into smart, structured clinical notes using AI.

## 🚀 Demo Flow

1. Doctor speaks into mic (or ESP32)
2. Whisper transcribes voice to text
3. GPT-4 structures clinical note
4. PDF is auto-generated
5. Optional: UI and embedded integration

## 🧠 Technologies Used

- 🔊 Whisper (Speech-to-Text)
- 🧠 GPT-4 (Clinical note generation)
- 📄 FPDF (PDF generation)
- 🌐 Streamlit (Demo UI)
- 📡 ESP32 (optional voice capture)

## 📁 Folder Structure

VoiceDoc-AI/
├── app.py              # Main processing file
├── streamlit_ui.py     # Demo interface
├── prompt_template.txt # GPT prompt format
├── sample_audio.wav    # Voice input
├── output_note.pdf     # Generated output
├── requirements.txt    # Dependencies
└── ESP32/              # Embedded voice capture

## 📽️ Demo Video

▶️ [Link to YouTube Demo](#) *(add after uploading video)*

## 🛠️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## ❤️ Built with purpose during Hackathon 2025
