import mediapipe as mp
import numpy as np

def detect_thinking(image, face_landmarks, hand_landmarks):
    if not hand_landmarks or not face_landmarks:
        return False

    # Get relevant face landmarks (temple area)
    temple_landmark = face_landmarks.landmark[447]  # Right temple area
    
    # Get index finger tip and thumb tip from hand landmarks
    index_finger_tip = hand_landmarks[0].landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = hand_landmarks[0].landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    
    # Calculate distances between finger tips and temple
    index_distance = np.sqrt(
        (index_finger_tip.x - temple_landmark.x)**2 +
        (index_finger_tip.y - temple_landmark.y)**2
    )
    
    thumb_distance = np.sqrt(
        (thumb_tip.x - temple_landmark.x)**2 +
        (thumb_tip.y - temple_landmark.y)**2
    )
    
    # Define threshold for "near face" detection
    DISTANCE_THRESHOLD = 0.15
    
    # Check if either finger is near the temple
    is_finger_near_temple = (index_distance < DISTANCE_THRESHOLD or 
                           thumb_distance < DISTANCE_THRESHOLD)
    
    # Additional check to ensure hand is relatively still
    # This could be enhanced by tracking hand movement over time
    
    return is_finger_near_temple