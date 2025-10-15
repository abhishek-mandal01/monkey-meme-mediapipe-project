import cv2
import mediapipe as mp

def is_middle_finger_up(hand_landmarks):
    tip_y = hand_landmarks.landmark[12].y
    pip_y = hand_landmarks.landmark[10].y
    mcp_y = hand_landmarks.landmark[9].y
    return tip_y < pip_y and tip_y < mcp_y
