import cv2
import mediapipe as mp

def is_thumb_up(hand_landmarks):
    tip_y = hand_landmarks.landmark[4].y
    ip_y = hand_landmarks.landmark[3].y
    mcp_y = hand_landmarks.landmark[2].y
    return tip_y < ip_y and tip_y < mcp_y
