# Camera Vision App

A Streamlit app that takes a webcam photo and asks an OpenAI vision model about it.

## Why this exists
A small experiment with multimodal LLMs: sending a live camera image plus an instruction to GPT-4o.

## What it does
- Captures a photo with `st.camera_input`
- Sends the image (base64) and your instruction to `gpt-4o`
- Shows the model's description or answer
- Includes a separate script that tracks people from the webcam with YOLOv8 and shows FPS

## Project structure
```
camera-openai-vision-streamlit/
├── app.py                     Streamlit camera and vision app
├── yolov8_person_tracking.py  Webcam person tracking (YOLOv8)
├── index.html                 Static browser version
└── requirements.txt           Python dependencies
```

## Getting started
Requirements: Python 3.10+, a webcam, an OpenAI API key.
```bash
git clone https://github.com/abhijha8287/camera-openai-vision-streamlit.git
cd camera-openai-vision-streamlit
pip install -r requirements.txt
streamlit run app.py
```
Paste your API key in the sidebar when the app opens.

For the YOLOv8 script:
```bash
pip install ultralytics opencv-python
python yolov8_person_tracking.py
```

## Configuration
The OpenAI API key is entered in the app's sidebar and is not stored.

## Tech stack
Python, Streamlit, OpenAI API (GPT-4o), Ultralytics YOLOv8, OpenCV

## Notes
Live demo: https://cameraopenaivisionapp.streamlit.app
