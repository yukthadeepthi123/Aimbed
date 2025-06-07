
import streamlit as st

st.title("VoiceDoc AI")

if st.button("Generate Clinical Note"):
    with st.spinner("Processing..."):
        exec(open("app.py").read())
        st.success("Clinical note generated!")
        st.download_button("Download PDF", open("output_note.pdf", "rb"), file_name="note.pdf")
