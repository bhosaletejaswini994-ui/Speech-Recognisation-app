# 🎤 Speech Recognition App using Python

## 📌 Project Overview

The **Speech Recognition App** is a Python-based desktop application that listens to the user's voice, converts spoken words into text, and speaks the recognized words back using text-to-speech technology.

The application uses **CustomTkinter** to create a graphical user interface (GUI), **SpeechRecognition** to recognize speech through a microphone, and **pyttsx3** to convert text into speech.

The interface also displays a Talking Tom image, making the application more interactive and visually appealing.

## ✨ Features

- 🎙️ **Voice Input:** Capture speech through a microphone.
- 📝 **Speech-to-Text:** Convert spoken words into text.
- 🔊 **Text-to-Speech:** Speak the recognized words aloud.
- 🖥️ **Graphical User Interface:** Simple and user-friendly interface using CustomTkinter.
- 🐱 **Talking Tom Image:** Displays an image in the application window.
- ⏳ **Listening Status:** Shows a message while the application listens.
- ⚠️ **Error Handling:** Displays an error message if speech recognition fails.
- 🧵 **Multithreading:** Runs the listening process in a separate thread to keep the interface responsive.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Creates the desktop GUI |
| SpeechRecognition | Recognizes spoken words |
| PyAudio | Provides microphone audio input |
| pyttsx3 | Converts text into spoken audio |
| Pillow (PIL) | Loads and displays the image |
| Threading | Runs speech recognition in the background |
| OS | Checks whether the image file exists |

## 📋 Requirements

- Python 3.12 recommended.
- A working microphone.
- Speakers or headphones.
- An internet connection for Google's online speech recognition service.
- The required Python libraries installed.

## ⚙️ Installation

### Step 1: Install the required libraries

Open the VS Code terminal or Command Prompt and run:

```bash
py -3.12 -m pip install customtkinter pillow pyttsx3 "SpeechRecognition[audio]"
```

This command installs CustomTkinter, Pillow, pyttsx3, SpeechRecognition, and its audio dependencies.

### Step 2: Create the project files

Create a folder for your project and add these files:

```text
Speech-Recognition-App/
├── SpeechRecognitionApp.py
├── tom image.webp
└── README.md
```

**Important:** Keep `tom image.webp` in the same folder from which you run the Python script, because the code checks for the image using a relative path.

### Step 3: Run the application

Open the terminal in your project folder and run:

```bash
py -3.12 SpeechRecognitionApp.py
```

The application window should open with the title **Speech Recognition App**.

## 🚀 How to Use

1. Run the Python application.
2. Make sure your microphone is connected and available.
3. Click the **Start Speaking** button.
4. Wait for the message `Listening... please speak!`.
5. Speak clearly into the microphone.
6. The application converts your speech into text and displays the recognized words.
7. The application then speaks the recognized text aloud.
8. If an error occurs, the application displays an error message.

## 🔍 How It Works

1. **Initialize text-to-speech:** The `pyttsx3` engine is initialized and configured with a speaking rate of 150.
2. **Create the interface:** CustomTkinter creates the application window, title, image, status label, and button.
3. **Start listening:** Clicking the button calls the `start_talking()` function.
4. **Capture audio:** SpeechRecognition accesses the microphone and records the user's voice.
5. **Recognize speech:** `recognize_google()` sends the audio to Google's online speech recognition service and returns recognized text.
6. **Display the result:** The recognized words appear in the status label.
7. **Speak the result:** `speaker.say()` and `speaker.runAndWait()` play the recognized text through the computer's speech engine.
8. **Handle errors:** If recording or recognition fails, the application displays an error message and re-enables the button.

## 💻 Important Code Explained

### 1. Speech recognition

```python
recognizer = sr.Recognizer()
```

Creates a recognizer object used to process speech.

### 2. Microphone input

```python
with sr.Microphone() as source:
    audio = recognizer.listen(
        source,
        timeout=5,
        phrase_time_limit=10
    )
```

Captures microphone audio, waits up to five seconds for speech to begin, and limits a recorded phrase to ten seconds.

### 3. Convert speech into text

```python
text = recognizer.recognize_google(audio)
```

Uses Google's online speech recognition service to recognize spoken words.

### 4. Speak the recognized text

```python
speaker.say(text)
speaker.runAndWait()
```

Adds the recognized text to the speech queue and plays it aloud.

### 5. Background thread

```python
threading.Thread(
    target=listen,
    daemon=True
).start()
```

Runs the listening function in a separate thread so the application window can remain responsive while recording and processing audio.

## ⚠️ Limitations

- Google speech recognition requires an internet connection.
- Recognition accuracy depends on microphone quality, background noise, accent, and pronunciation.
- The microphone must be accessible to Python.
- The current code uses a fixed timeout and phrase duration.
- The application speaks back the recognized words; it does not generate intelligent conversational responses.
- The image will not appear if `tom image.webp` cannot be found at the specified relative path.
- The current `reset_button()` function is defined but is not connected to a reset button in the interface.

## 🔮 Future Improvements

- Add a Reset button to clear the previous result.
- Add a Stop Speaking button.
- Display the conversation history in a text box.
- Allow users to choose different voices and speech rates.
- Support multiple languages.
- Add an animated character that reacts to the user's voice.
- Add voice commands to open applications or perform tasks.
- Integrate an AI chatbot to generate meaningful responses.

## 🔐 Privacy Note

The application uses Google's online speech recognition service. Audio is sent to the service for recognition, so users should avoid speaking passwords, confidential information, or other sensitive data.

## 👩‍💻 Project Information

- **Project Name:** Speech Recognition App
- **Language:** Python
- **Project Type:** Desktop GUI Application
- **Domain:** Speech Processing and Human-Computer Interaction
- **Purpose:** To demonstrate voice input, speech-to-text conversion, and text-to-speech output using Python.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
