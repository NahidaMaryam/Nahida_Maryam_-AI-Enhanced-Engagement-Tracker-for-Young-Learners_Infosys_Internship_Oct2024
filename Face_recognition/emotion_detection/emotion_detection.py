import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from imutils import face_utils
from deepface import DeepFace
from PIL import Image, ImageDraw, ImageFont

# Initialize dlib's face detector and the facial landmark predictor
p = "/home/maryam/face_recognization/facial-landmarks-recognition/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(p)

# Create directories to save screenshots
if not os.path.exists("Maryam_screenshots_emotion"):
    os.makedirs("Maryam_screenshots_emotion")

# Load the known image
known_image = face_recognition.load_image_file("/home/maryam/face_recognization/nahida.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information with emotions
columns = ['Name', 'Date', 'Time', 'Screenshot', 'Attentive', 'Emotion']
df = pd.DataFrame(columns=columns)

# Emoji mapping
emotion_emoji = {
    'happy': '🙂',    # Alternative: ':)'
    'sad': '🙁',      # Alternative: ':('
    'angry': '>:(',
    'neutral': ':|',
    'surprise': ':O',
    'fear': 'D:',
    'disgust': ':P'
}

def put_text_with_emoji(img, text, position, font_size=30, color=(255, 255, 255)):
    """Draw text with emoji on the image using PIL."""
    # Convert OpenCV image (BGR) to PIL image (RGB)
    img_pil = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    
    try:
        # Try to load a font that supports emojis
        font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", font_size)
    except:
        try:
            # Fallback to another emoji font
            font = ImageFont.truetype("/usr/share/fonts/noto-emoji/NotoEmoji-Regular.ttf", font_size)
        except:
            print("Emoji font not found. Installing required font...")
            # If font is not found, install it
            os.system('sudo apt-get update && sudo apt-get install -y fonts-noto-color-emoji')
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", font_size)
            except:
                print("Could not load emoji font. Using default font.")
                return img

    # Draw the text with emoji
    draw.text(position, text, font=font, fill=color)
    
    # Convert back to OpenCV image (BGR)
    return cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR)

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
        
        # Camera internals
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
    """Detect emotion in the frame using DeepFace"""
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            result = result[0]
        emotion = result['dominant_emotion']
        return emotion, result['emotion'][emotion]
    except Exception as e:
        print(f"Emotion detection error: {e}")
        return 'neutral', 0.0

def load_emoji_images():
    """Load emoji images for each emotion."""
    emoji_path = "emojis/"  # Create this directory and add emoji images
    if not os.path.exists(emoji_path):
        os.makedirs(emoji_path)
        
    emoji_images = {}
    for emotion in ['happy', 'sad', 'angry', 'neutral', 'surprise', 'fear', 'disgust']:
        try:
            img_path = os.path.join(emoji_path, f"{emotion}.png")
            if os.path.exists(img_path):
                emoji_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
                emoji_img = cv.resize(emoji_img, (30, 30))
                emoji_images[emotion] = emoji_img
        except Exception as e:
            print(f"Could not load emoji for {emotion}: {e}")
    
    return emoji_images

def overlay_emoji(frame, emoji_img, position):
    """Overlay emoji image on frame."""
    try:
        x, y = position
        h, w = emoji_img.shape[:2]
        
        # Create ROI
        roi = frame[y:y+h, x:x+w]
        
        # Create mask
        if emoji_img.shape[2] == 4:  # If PNG with alpha channel
            alpha = emoji_img[:, :, 3] / 255.0
            for c in range(3):
                roi[:, :, c] = roi[:, :, c] * (1 - alpha) + emoji_img[:, :, c] * alpha
        else:
            frame[y:y+h, x:x+w] = emoji_img
            
    except Exception as e:
        print(f"Error overlaying emoji: {e}")

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
                pitch = euler_angles[0][0]  # Access the first element of each angle
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

                # Load emoji images once
                emoji_images = load_emoji_images()
                
                # Display emotion text and emoji image
                cv.putText(frame, emotion, (10, 140), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                if emotion in emoji_images:
                    overlay_emoji(frame, emoji_images[emotion], (100, 120))

                # Display confidence score using regular OpenCV text
                cv.putText(frame, 
                          f'Score: {emotion_score:.2f}', 
                          (10, 180),
                          cv.FONT_HERSHEY_SIMPLEX, 
                          0.5, 
                          (255, 255, 255), 
                          1)

                # Update the name display with emoji
                name_emotion_text = f'{name} - {emotion} {emotion_emoji[emotion]}'
                frame = put_text_with_emoji(
                    frame,
                    name_emotion_text,
                    (left, max(top - 30, 10)),
                    font_size=20
                )

                # Save screenshot
                screenshot_filename = f"Maryam_screenshots_emotion/{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                cv.imwrite(screenshot_filename, frame)

                # Log the recognition event with emotion
                new_entry = pd.DataFrame({
                    'Name': [name],
                    'Date': [now.strftime("%Y-%m-%d")],
                    'Time': [now.strftime("%H:%M:%S")],
                    'Screenshot': [screenshot_filename],
                    'Attentive': ['Yes' if attentive else 'No'],
                    'Emotion': [emotion]
                })
                df = pd.concat([df, new_entry], ignore_index=True)

                # Draw rectangle and labels
                color = (0, 255, 0) if attentive else (0, 0, 255)
                cv.rectangle(frame, (left, top), (right, bottom), color, 2)
                cv.putText(frame, f'{name} - {emotion} {emotion_emoji[emotion]}', (left, top - 10), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Save DataFrame every 30 seconds
        if (datetime.now() - last_save_time) > timedelta(seconds=30):
            df.to_excel('maryam_attendance_with_emotions.xlsx', index=False)
            print("Data saved to 'maryam_attendance_with_emotions.xlsx'")
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
        df.to_excel('maryam_attendance_with_emotions.xlsx', index=False)
        print("Final data saved to 'maryam_attendance_with_emotions.xlsx'")
    
    cam.release()
    cv.destroyAllWindows() 