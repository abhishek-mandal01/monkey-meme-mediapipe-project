import cv2
import mediapipe as mp
import numpy as np
from detect_index_finger import is_index_finger_up
from detect_middle_finger import is_middle_finger_up
from detect_thumb import is_thumb_up
from detect_face import is_face_detected
from detect_tongue import is_tongue_out
from detect_thinking import detect_thinking

# Load overlay images
serious_img = cv2.imread('serious-monkey.png')
thumbsup_img = cv2.imread('thumbsup-monkey.png')
solver_img = cv2.imread('solver-monkey.png')
overlay_img = cv2.imread('middleup-monkey.png')
tongue_img = cv2.imread('tongueout-monkey.png')
thinking_img = cv2.imread('thinking-monkey.png')

blank_img = None
if overlay_img is not None:
    blank_img = 255 * np.ones_like(overlay_img)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
cv2.namedWindow('MiddleUp Monkey', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_result = hands.process(rgb_frame)
    face_result = face_mesh.process(rgb_frame)

    index_finger_detected = False
    middle_finger_detected = False
    thumb_up_detected = False
    face_detected = is_face_detected(frame)
    tongue_detected = is_tongue_out(rgb_frame)
    thinking_detected = False

    # Process hand landmarks
    if hand_result.multi_hand_landmarks:
        for hand_landmarks in hand_result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_index_finger_up(hand_landmarks):
                index_finger_detected = True
            if is_middle_finger_up(hand_landmarks):
                middle_finger_detected = True
            if is_thumb_up(hand_landmarks):
                thumb_up_detected = True
            
            # Check for thinking pose if face landmarks are available
            if face_result and face_result.multi_face_landmarks:
                thinking_detected = detect_thinking(frame, face_result.multi_face_landmarks[0], [hand_landmarks])
    else:
        cv2.putText(frame, "", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Show overlay image based on priority
    if tongue_detected and tongue_img is not None:
        cv2.imshow('MiddleUp Monkey', tongue_img)
    elif thinking_detected and thinking_img is not None:
        cv2.imshow('MiddleUp Monkey', thinking_img)
    elif index_finger_detected and solver_img is not None:
        cv2.imshow('MiddleUp Monkey', solver_img)
    elif middle_finger_detected and overlay_img is not None:
        cv2.imshow('MiddleUp Monkey', overlay_img)
    elif thumb_up_detected and thumbsup_img is not None:
        cv2.imshow('MiddleUp Monkey', thumbsup_img)
    elif face_detected and serious_img is not None:
        cv2.imshow('MiddleUp Monkey', serious_img)
    elif blank_img is not None:
        cv2.imshow('MiddleUp Monkey', blank_img)

    cv2.imshow('Camera Simulation', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()