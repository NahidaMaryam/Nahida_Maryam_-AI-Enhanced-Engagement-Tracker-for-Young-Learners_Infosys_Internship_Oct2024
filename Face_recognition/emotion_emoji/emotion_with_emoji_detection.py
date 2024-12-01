import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from imutils import face_utils
from PIL import Image, ImageDraw, ImageFont
import tensorflow as tf

# Suppress TensorFlow warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Initialize dlib's face detector and the facial landmark predictor
p = "/home/maryam/face_recognization/facial-landmarks-recognition/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(p)

# Create directories to save screenshots
if not os.path.exists("Maryam_screenshots_emotion_2"):
    os.makedirs("Maryam_screenshots_emotion_2")

# Load the known image
known_image = face_recognition.load_image_file("/home/maryam/face_recognization/nahida.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information with emotions
columns = ['Name', 'Date', 'Time', 'Screenshot', 'Attentive', 'Emotion', 'Emotion_Score']
df = pd.DataFrame(columns=columns)

# Emoji mapping with simpler characters
emotion_emoji = {
    'happy': ':)',
    'sad': ':(',
    'angry': '>:(',
    'neutral': ':|',
    'surprise': ':O',
    'fear': 'D:',
    'disgust': ':P'
}

def get_head_pose(landmarks, frame):
    """Calculate head pose estimation."""
    try:
        image_points = np.array([
            landmarks[30],  # Nose tip
            landmarks[8],   # Chin
            landmarks[36],  # Left eye left corner
            landmarks[45],  # Right eye right corner
            landmarks[48],  # Left mouth corner
            landmarks[54]   # Right mouth corner
        ], dtype="double")
        
        model_points = np.array([
            (0.0, 0.0, 0.0),             # Nose tip
            (0.0, -330.0, -65.0),        # Chin
            (-165.0, 170.0, -135.0),     # Left eye left corner
            (165.0, 170.0, -135.0),      # Right eye right corner
            (-150.0, -150.0, -125.0),    # Left mouth corner
            (150.0, -150.0, -125.0)      # Right mouth corner
        ])
        
        size = frame.shape
        focal_length = size[1]
        center = (size[1]/2, size[0]/2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]], dtype="double")
        
        dist_coeffs = np.zeros((4,1))
        
        success, rotation_vector, translation_vector = cv.solvePnP(
            model_points, 
            image_points, 
            camera_matrix, 
            dist_coeffs, 
            flags=cv.SOLVEPNP_ITERATIVE
        )
        
        rotation_mat, _ = cv.Rodrigues(rotation_vector)
        pose_mat = cv.hconcat((rotation_mat, translation_vector))
        _, _, _, _, _, _, euler_angles = cv.decomposeProjectionMatrix(cv.hconcat((pose_mat, np.array([[0, 0, 0, 1]]))))
        
        return euler_angles
    except Exception as e:
        print(f"Error in head pose estimation: {e}")
        return np.array([[0.0], [0.0], [0.0]])

def detect_emotion(frame):
    """Simple emotion detection based on facial landmarks"""
    try:
        # Convert frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = detector(gray)
        
        if len(faces) > 0:
            # Get facial landmarks
            face = faces[0]
            shape = landmark_predictor(gray, face)
            shape = face_utils.shape_to_np(shape)
            
            # Simple emotion detection based on mouth shape
            mouth_width = np.linalg.norm(shape[54] - shape[48])
            mouth_height = np.linalg.norm(shape[57] - shape[51])
            smile_ratio = mouth_width / mouth_height
            
            # Determine emotion based on smile ratio
            if smile_ratio > 2.5:
                return 'happy', 0.8
            elif smile_ratio < 1.5:
                return 'sad', 0.7
            else:
                return 'neutral', 0.6
            
    except Exception as e:
        print(f"Error in emotion detection: {e}")
    
    return 'neutral', 0.5

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

frame_count = 0
last_save_time = datetime.now()

try:
    while True:
        frame_count += 1
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive frame")
            break

        if frame_count % 2 == 0:  # Skip every other frame
            continue

        frame = cv.resize(frame, (320, 240))
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces
        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            continue

        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            distance = face_recognition.face_distance([known_faces], face_encoding)[0]

            if distance < 0.6:
                now = datetime.now()
                name = 'Maryam'
                
                # Detect emotion
                emotion, emotion_score = detect_emotion(frame)
                
                # Get face landmarks and attention status
                face_landmarks = landmark_predictor(gray, dlib.rectangle(left, top, right, bottom))
                landmarks = [(p.x, p.y) for p in face_landmarks.parts()]
                
                # Calculate attention status
                euler_angles = get_head_pose(landmarks, frame)
                pitch = euler_angles[0][0]
                yaw = euler_angles[1][0]
                roll = euler_angles[2][0]
                
                PITCH_THRESHOLD = 35
                YAW_THRESHOLD = 35
                ROLL_THRESHOLD = 35
                
                pitch_score = 1 - min(abs(pitch) / PITCH_THRESHOLD, 1)
                yaw_score = 1 - min(abs(yaw) / YAW_THRESHOLD, 1)
                roll_score = 1 - min(abs(roll) / ROLL_THRESHOLD, 1)
                attention_score = (pitch_score + yaw_score + roll_score) / 3
                attentive = attention_score > 0.6

                # Display emotion and emoji
                emoji = emotion_emoji.get(emotion, ':|')
                cv.putText(frame, f'Emotion: {emotion} {emoji}', (10, 140), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv.putText(frame, f'Confidence: {emotion_score:.2f}', (10, 160), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                # Save screenshot
                screenshot_filename = f"Maryam_screenshots_emotion_2/{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                cv.imwrite(screenshot_filename, frame)

                # Log the recognition event with emotion
                new_entry = pd.DataFrame({
                    'Name': [name],
                    'Date': [now.strftime("%Y-%m-%d")],
                    'Time': [now.strftime("%H:%M:%S")],
                    'Screenshot': [screenshot_filename],
                    'Attentive': ['Yes' if attentive else 'No'],
                    'Emotion': [emotion],
                    'Emotion_Score': [emotion_score]
                })
                df = pd.concat([df, new_entry], ignore_index=True)

                # Draw rectangle and labels
                color = (0, 255, 0) if attentive else (0, 0, 255)
                cv.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv.putText(frame, f'{name} - {emotion} {emoji}', (left, top - 10), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Save DataFrame every 30 seconds
        if (datetime.now() - last_save_time) > timedelta(seconds=30):
            df.to_excel('maryam_attendance_with_emotions_2.xlsx', index=False)
            print("Data saved to 'maryam_attendance_with_emotions_2.xlsx'")
            last_save_time = datetime.now()

        # Display the frame
        cv.imshow("Video Stream", frame)
        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()

finally:
    if not df.empty:
        df.to_excel('maryam_attendance_with_emotions_2.xlsx', index=False)
        print("Final data saved to 'maryam_attendance_with_emotions_2.xlsx'")
    
    cam.release()
    cv.destroyAllWindows()