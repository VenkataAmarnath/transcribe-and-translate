# Audio Transcription and Translation Web App

This project is a web application built with **Streamlit** that allows users to upload audio files, transcribe the content to English, and translate the transcribed text into a chosen language. The app leverages the **Whisper** model for transcription and **Google Translator** for translation.

## Project Overview

- **Transcription**: The app uses OpenAI's Whisper model to transcribe audio files into English text.
- **Translation**: The transcribed text can be translated into a selected language using Google Translator.
- **File Upload**: Users can upload audio files in `.wav`, `.mp3`, or `.m4a` formats.

## Installation and Setup

To run this project locally, ensure you have the following installed:

1. **Python** (version 3.7 or higher)
2. **Streamlit**
3. **Whisper**
4. **Googletrans**

### Step-by-Step Guide:

1. **Clone this repository:**

   ```bash
   git clone https://github.com/VenkataAmarnath/transcribe-and-translate.git
   cd your-repo-name
   ```

2. **Install the required packages:**

   Create a `requirements.txt` file with the following content:

   ```txt
   streamlit
   whisper
   googletrans==4.0.0-rc1
   ```

   Then, install the packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## How to Use

1. Open the app in your browser (URL is provided in the terminal after running `streamlit run`).
2. Upload an audio file (`.wav`, `.mp3`, or `.m4a`).
3. Wait for the transcription process to complete.
4. Select a language from the dropdown menu for translation.
5. View the transcribed text and translated content.

## Troubleshooting

- If you face issues with audio processing, ensure `ffmpeg-python` is properly installed and `ffmpeg` is added to your system PATH.
- To install `ffmpeg-python`, run:

  ```bash
  pip install ffmpeg-python
  ```

## Project Structure

```
your-repo-name/
│
├── app.py                # Main Streamlit app script
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation
```

## Dependencies

- **Streamlit**: For building the interactive web app.
- **Whisper**: For audio transcription.
- **Googletrans**: For text translation.
- **ffmpeg-python**: To handle audio file processing.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to [OpenAI](https://openai.com) for the Whisper model.
- Thanks to [Googletrans](https://pypi.org/project/googletrans/) for the translation API.

---

For any questions or feedback, please contact [Linkedin](https://www.linkedin.com/in/venkata-a-1a9690334/).
```