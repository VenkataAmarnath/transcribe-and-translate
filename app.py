# Ensure that ffmpeg-python is properly installed and available in your PATH.

# Import necessary libraries
import streamlit as st
import whisper
from googletrans import Translator, LANGUAGES

st.title("Audio Transcription and Translation App")
st.subheader("Upload an audio file to transcribe it and translate the text into your chosen language.")
st.write("This app supports audio transcription from various file types (MP3, WAV, M4A) and translation into multiple languages.")


# Load the Whisper model and Translator instance
@st.cache_data
def load_model():
    model=whisper.load_model("tiny")
    return model

model=load_model()
translator=Translator()


# Streamlit file uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

# Mapping of file types to file extensions
extension_mapping = {
    "audio/mpeg": "mp3",
    "audio/wav": "wav",
    "audio/mp4": "m4a",
}

# Check if an audio file is uploaded
if audio_file is not None:
    st.success(f"your audio file received")

    # Determine the file extension
    file_extension = extension_mapping.get(audio_file.type, None)

    try:
        # Save the uploaded audio file with the correct extension
        file_path = f"uploaded_audio.{file_extension}"
        with open(file_path, "wb") as f:
            f.write(audio_file.getbuffer())
    except Exception as e:
        raise Exception(e)        

    try:
        # Transcribe the uploaded audio using the Whisper model
        with st.spinner("Processing your request. Please wait..."):
            result = model.transcribe(file_path)
        st.write("result stored")
        st.write(" Your audio in English:")
        st.write(result['text'])
    except:
        st.write("Error while transcribing file")


    # Populate language options for translation
    lang=list(LANGUAGES.values())
    lang.insert(0, "Select a language")
    selected_option = st.selectbox(
        "Select a language for translation",lang
    )

    if selected_option!="Select a language":
        # Find the language code from the selected language
        for key,value in LANGUAGES.items():
            if selected_option==LANGUAGES[key]:
                translation_lang=key
        
        try:
            with st.spinner("Processing your request. Please wait..."):
                translation=translator.translate(result['text'],src="en", dest=translation_lang)
            st.write(f"Your script in {selected_option}")
            st.write(translation.text)
        except Exception as e:
            st.write(f"Error occured while translating file to {selected_option}")
            st.error(f"Details: {e}")

    else:
        # Placeholder for no language selected
        pass

else:
    st.write("Upload your audio file here")