import cv2 as cv
import face_recognition
import pandas as pd
from datetime import datetime, timedelta

# Load the known image of Maryam
known_image = face_recognition.load_image_file("/home/maryam/face_recognization/nahida.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time']
df = pd.DataFrame(columns=columns)

# Launch the live camera
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Camera not working")
    exit()

confidence_threshold = 0.6
frame_skip = 2
frame_count = 0
recognition_count = 0
recognized_names = set()  # Track recognized individuals

# Time tracking
last_recognition_time = None
entry_time = None
entry_duration = timedelta(minutes=2)  # Duration to keep the entry valid
gap_time = timedelta(minutes=5)  # Gap required to log a new entry

# Save interval
save_interval = timedelta(seconds=30)
last_save_time = datetime.now()

try:
    while True:
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive the frame")
            break

        frame = cv.resize(frame, (640, 480))
        frame_count += 1
        if frame_count % frame_skip != 0:
            continue

        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            continue  # Skip if no faces detected

        face_encodings = face_recognition.face_encodings(frame, face_locations)

        recognized = False

        for face_encoding in face_encodings:
            distance = face_recognition.face_distance([known_faces], face_encoding)[0]

            if distance < confidence_threshold:
                recognized = True
                now = datetime.now()

                # Check if the same person has been seen
                if last_recognition_time is None or (now - last_recognition_time) >= entry_duration:
                    # Record the entry
                    new_entry = pd.DataFrame({
                        'Name': ['Maryam'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")]
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    last_recognition_time = now  # Update the last recognition time
                    entry_time = now  # Update entry time
                elif (now - entry_time) >= gap_time:
                    # If 5 minutes have passed since the last entry, record again
                    new_entry = pd.DataFrame({
                        'Name': ['Maryam'],
                        'Date': [now.strftime("%Y-%m-%d")],
                        'Time': [now.strftime("%H:%M:%S")]
                    })
                    df = pd.concat([df, new_entry], ignore_index=True)
                    entry_time = now  # Update entry time again

                # Draw rectangle and label on frame
                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    cv.rectangle(frame, (left, top), (right, bottom), color=(0, 255, 0), thickness=2)
                    cv.putText(frame, 'Maryam', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                               (255, 0, 0), 2, cv.LINE_AA)

        if not recognized:
            cv.putText(frame, 'Not Maryam', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (255, 0, 0), 2, cv.LINE_AA)

        # Save DataFrame to Excel every 30 seconds
        if datetime.now() - last_save_time >= save_interval:
            df.to_excel('maryam_recognized_faces.xlsx', index=False)
            last_save_time = datetime.now()  # Reset the save timer

        cv.imshow('Video Stream', frame)

        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Final save if any recognitions were made before exiting
    if not df.empty:
        df.to_excel('maryam_attendance.xlsx', index=False)

    # Release the capture
    cam.release()
    cv.destroyAllWindows()