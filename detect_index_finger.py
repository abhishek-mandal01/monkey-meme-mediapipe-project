import cv2
import mediapipe as mp

def is_index_finger_up(hand_landmarks):
    tip_y = hand_landmarks.landmark[8].y
    pip_y = hand_landmarks.landmark[6].y
    mcp_y = hand_landmarks.landmark[5].y
    return tip_y < pip_y and tip_y < mcp_y
