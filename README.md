# Monkey Meme Expression Detection

A fun interactive project that uses MediaPipe for real-time gesture and expression detection, displaying corresponding monkey emotions based on detected poses and gestures.

## Features

The application detects various gestures and expressions in real-time:
- 👅 Tongue Out Detection
- 🤔 Thinking Pose Detection
- ☝️ Index Finger Up Detection
- 🖕 Middle Finger Detection
- 👍 Thumbs Up Detection
- 😐 Neutral Face Detection

Each detected gesture triggers a corresponding monkey emotion image display.

## Prerequisites

- Python 3.8 to 3.11
- Webcam
- Windows

## Setup Instructions

1. **Clone the repository**
   ```powershell
   git clone https://github.com/abhishek-mandal01/monkey-meme-mediapipe-project.git
   ```

3. **Create and activate virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate  # On Windows
   ```

4. **Install required packages**
   ```powershell
   pip install mediapipe opencv-python numpy
   ```

5. **Prepare image assets**
   Ensure you have the following images in your project root:
   - `serious-monkey.png`
   - `thumbsup-monkey.png`
   - `solver-monkey.png`
   - `middleup-monkey.png`
   - `tongueout-monkey.png`
   - `thinking-monkey.png`
Or you can add your own set of images.

## Running the Application

1. Activate the virtual environment (if not already activated)
   ```powershell
   .\venv\Scripts\Activate  # On Windows
   ```

2. Run the main script
   ```powershell
   python main.py
   ```

3. Press 'q' to quit the application

## Gesture Detection Details

### Tongue Out Detection
- Uses MediaPipe Face Mesh to track facial landmarks
- Detects tongue protrusion based on mouth landmarks

### Thinking Pose Detection
- Recognizes when index finger or thumb is near the temple
- Combines hand and face landmark detection
- Distance-based threshold for pose recognition

### Index Finger Detection
- Tracks hand landmarks to identify raised index finger
- Other fingers should be closed

### Middle Finger Detection
- Detects extended middle finger gesture
- Uses relative positions of finger joints

### Thumbs Up Detection
- Recognizes classic thumbs up pose
- Based on thumb extension and other fingers' positions

### Face Detection
- Default expression when only face is detected
- No specific gestures recognized

**Shows a blank screen/tab if no face is detected.

## Project Structure

```
monkey-mediapipe-project/
├── main.py                  # Main application file
├── detect_thinking.py       # Thinking pose detection
├── detect_tongue.py         # Tongue detection
├── detect_index_finger.py   # Index finger detection
├── detect_middle_finger.py  # Middle finger detection
├── detect_thumb.py          # Thumbs up detection
├── detect_face.py          # Face detection
└── README.md               # Project documentation
```

## Gesture Priority Order

The application follows this priority order for displaying emotions:
1. Tongue Out
2. Thinking Pose
3. Index Finger Up
4. Middle Finger
5. Thumbs Up
6. Serious Face
7. Default (Blank)


Feel free to fork the project and submit pull requests. Please ensure your code follows the existing structure and includes appropriate documentation.
