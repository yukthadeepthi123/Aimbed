
import openai
import whisper
from fpdf import FPDF

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio file
result = model.transcribe("sample_audio.wav")
transcribed_text = result['text']

# Prepare GPT-4 prompt
openai.api_key = 'your-api-key'
prompt = f"""
Convert the following doctor's dictation into a clinical note.

Format:
- Patient:
- Symptoms:
- Diagnosis:
- Prescription:
- Advice:

Dictation: {transcribed_text}
"""

# Call GPT-4
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
clinical_note = response['choices'][0]['message']['content']

# Export as PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, clinical_note)
pdf.output("output_note.pdf")
