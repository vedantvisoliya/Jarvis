# 🧠 Jarvis - A Voice Controlled Virtual Assistant

Jarvis is a Python-based voice assistant that can perform tasks like opening popular websites and responding to queries using Google Gemini's generative AI model. It listens for a wake word ("Jarvis") and then processes voice commands.

### ✨ Features

    🎙️ Voice recognition using speech_recognition

    🔊 Voice responses using pyttsx3

    🌐 Opens websites like YouTube, Google, GitHub, etc.

    🤖 Handles general queries using Google's Gemini Pro (Generative AI)

    🛠 Wake word detection ("Jarvis")

### 📁 Project Structure

    .
    ├── main.py               # Main program file
    ├── config.py               # API key configuration (GEMINI_API_KEY)
    ├── requirements.txt        # Python dependencies
    └── README.md               # Project documentation

### 🧑‍💻 Requirements

Create a virtual environment and then install the required Python packages:

```
pip install -r requirements.txt
```

### 🔐 API Configuration

Create a .env file a store api keys like so:

```
GEMINI_API_KEY="your_gemini_api_key"
```

### 🛡️ Disclaimer

This is a personal assistant for educational/demo purposes. Voice recognition may be affected by background noise or hardware limitations.

### 🚀 Usage

Run the assistant with:

```
python main.py
```

### 🤝 Contributing

Pull requests and feedback are welcome! Open an issue or suggest improvements.