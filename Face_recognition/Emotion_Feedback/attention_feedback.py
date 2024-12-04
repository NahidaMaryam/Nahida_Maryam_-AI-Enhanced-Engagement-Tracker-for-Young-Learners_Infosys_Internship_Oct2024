import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from imutils import face_utils
import random

# Initialize dlib's face detector and the facial landmark predictor
p = "/home/maryam/face_recognization/facial-landmarks-recognition/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(p)

# Create directories to save screenshots
if not os.path.exists("Attention_feedback_screenshots"):
    os.makedirs("Attention_feedback_screenshots")

# Load the known image
known_image = face_recognition.load_image_file("/home/maryam/face_recognization/nahida.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame
columns = ['Name', 'Date', 'Time', 'Screenshot', 'Attentive', 'Feedback']
df = pd.DataFrame(columns=columns)

# Feedback messages
positive_feedback = [
    "Great focus! Keep it up! 👍",
    "Excellent attention! 🌟",
    "You're doing great! 💪",
    "Perfect concentration! ⭐",
    "Wonderful engagement! 🎯",
    "Outstanding attention! 🏆",
    "Keep up the good work! 📈",
    "You're crushing it! 🚀"
]

attention_reminders = [
    "Please stay focused! 🎯",
    "Let's maintain attention! 👀",
    "Remember to stay engaged! 💭",
    "Attention needed! ⚠️",
    "Please focus on the session! 📚",
    "Let's get back on track! 🎯",
    "Stay with us! 🤝",
    "Your attention is important! ⭐"
]

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

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

frame_count = 0
last_save_time = datetime.now()
feedback_update_time = datetime.now()
current_feedback = ""
attention_streak = 0
inattention_streak = 0

try:
    while True:
        frame_count += 1
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive frame")
            break

        if frame_count % 2 == 0:  # Skip every other frame
            continue

        frame = cv.resize(frame, (640, 480))
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
                
                # Get face landmarks and attention status
                face_landmarks = landmark_predictor(gray, dlib.rectangle(left, top, right, bottom))
                landmarks = [(p.x, p.y) for p in face_landmarks.parts()]
                
                # Calculate attention status with dynamic thresholds and weights
                euler_angles = get_head_pose(landmarks, frame)
                pitch = euler_angles[0][0]
                yaw = euler_angles[1][0]
                roll = euler_angles[2][0]
                
                # Dynamic thresholds based on movement
                PITCH_THRESHOLD = 30  # Looking up/down
                YAW_THRESHOLD = 25    # Looking left/right
                ROLL_THRESHOLD = 20   # Head tilting

                # Weight factors for different movements
                PITCH_WEIGHT = 0.4  # More weight to up/down movement
                YAW_WEIGHT = 0.4    # More weight to left/right movement
                ROLL_WEIGHT = 0.2   # Less weight to tilting

                # Calculate normalized scores with weights
                pitch_score = (1 - min(abs(pitch) / PITCH_THRESHOLD, 1)) * PITCH_WEIGHT
                yaw_score = (1 - min(abs(yaw) / YAW_THRESHOLD, 1)) * YAW_WEIGHT
                roll_score = (1 - min(abs(roll) / ROLL_THRESHOLD, 1)) * ROLL_WEIGHT

                # Calculate attention score with movement factor
                attention_score = (pitch_score + yaw_score + roll_score) * 2  # Multiply by 2 to normalize to 0-1 range
                
                # Add movement detection
                if len(landmarks) > 1:
                    current_positions = np.array(landmarks)
                    if 'previous_positions' in locals():
                        movement = np.mean(np.abs(current_positions - previous_positions))
                        # Adjust attention score based on movement
                        if movement > 5:  # Threshold for significant movement
                            attention_score *= (1 - min(movement/20, 0.5))  # Reduce score based on movement
                    previous_positions = current_positions

                # Smooth the attention score
                if 'previous_score' in locals():
                    attention_score = 0.7 * previous_score + 0.3 * attention_score  # Smoothing factor
                previous_score = attention_score

                # Determine attentiveness with dynamic threshold
                attentive = attention_score > 0.65  # Slightly higher threshold

                # Display detailed attention metrics
                cv.putText(frame, 
                          f'Attention Score: {attention_score:.2f}',
                          (20, 50),
                          cv.FONT_HERSHEY_SIMPLEX,
                          0.6,
                          (0, 255, 0) if attentive else (0, 0, 255),
                          2)
                
                # Display component scores
                cv.putText(frame, 
                          f'Pitch: {pitch_score:.2f} Yaw: {yaw_score:.2f} Roll: {roll_score:.2f}',
                          (20, 80),
                          cv.FONT_HERSHEY_SIMPLEX,
                          0.5,
                          (255, 255, 255),
                          1)

                # Update feedback based on attention score ranges
                if attention_score > 0.8:
                    current_feedback = "Excellent focus! 🌟"
                elif attention_score > 0.65:
                    current_feedback = "Good attention! 👍"
                elif attention_score > 0.5:
                    current_feedback = "Try to focus more! 🎯"
                else:
                    current_feedback = "Please pay attention! ⚠️"

                # Update attention streaks and feedback
                if (datetime.now() - feedback_update_time).seconds >= 3:  # Update feedback every 3 seconds
                    if attentive:
                        attention_streak += 1
                        inattention_streak = 0
                        if attention_streak >= 3:  # After 3 consecutive attentive detections
                            current_feedback = random.choice(positive_feedback)
                    else:
                        inattention_streak += 1
                        attention_streak = 0
                        if inattention_streak >= 2:  # After 2 consecutive inattentive detections
                            current_feedback = random.choice(attention_reminders)
                    
                    feedback_update_time = datetime.now()

                # Display feedback with background
                feedback_size = cv.getTextSize(current_feedback, cv.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                feedback_bg_color = (0, 255, 0) if attentive else (0, 0, 255)
                cv.rectangle(frame, 
                           (10, 400),
                           (10 + feedback_size[0] + 20, 400 + feedback_size[1] + 20),
                           feedback_bg_color, 
                           -1)
                cv.putText(frame, 
                          current_feedback,
                          (20, 420),
                          cv.FONT_HERSHEY_SIMPLEX,
                          0.7,
                          (255, 255, 255),
                          2)

                # Save screenshot
                screenshot_filename = f"Attention_feedback_screenshots/{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                cv.imwrite(screenshot_filename, frame)

                # Log the recognition event
                new_entry = pd.DataFrame({
                    'Name': [name],
                    'Date': [now.strftime("%Y-%m-%d")],
                    'Time': [now.strftime("%H:%M:%S")],
                    'Screenshot': [screenshot_filename],
                    'Attentive': ['Yes' if attentive else 'No'],
                    'Feedback': [current_feedback]
                })
                df = pd.concat([df, new_entry], ignore_index=True)

                # Draw rectangle
                color = (0, 255, 0) if attentive else (0, 0, 255)
                cv.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv.putText(frame, name, (left, top - 10), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Save DataFrame every 30 seconds
        if (datetime.now() - last_save_time) > timedelta(seconds=30):
            df.to_excel('attention_feedback_log.xlsx', index=False)
            print("Data saved to 'attention_feedback_log.xlsx'")
            last_save_time = datetime.now()

        # Display the frame
        cv.imshow("Attention Feedback", frame)
        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()

finally:
    if not df.empty:
        df.to_excel('attention_feedback_log.xlsx', index=False)
        print("Final data saved to 'attention_feedback_log.xlsx'")
    
    cam.release()
    cv.destroyAllWindows() 