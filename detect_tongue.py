import mediapipe as mp

TONGUE_OUT_THRESHOLD = 0.03
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_faces=1
)

def is_tongue_out(frame):
    rgb_frame = frame if frame.shape[-1] == 3 else frame[..., :3]
    rgb_frame = rgb_frame.copy()
    results = face_mesh.process(rgb_frame)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]
            mouth_opening = abs(upper_lip.y - lower_lip.y)
            if mouth_opening > TONGUE_OUT_THRESHOLD:
                return True
    return False
