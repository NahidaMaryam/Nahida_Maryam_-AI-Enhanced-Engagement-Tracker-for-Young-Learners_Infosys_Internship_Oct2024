**Image processing** :
Image processing is a technique used to enhance, analyze, and manipulate digital images, typically through algorithms and computer vision tools. It involves a series of operations that transform an image to improve its quality, extract useful information, or prepare it for further analysis. Image processing has a wide array of applications, including photography, medical imaging, robotics, surveillance, and autonomous vehicles.

Libraries or Frameworks used- opencv

Version- 4.10.0.84

**Developed Logics**-
 
**A. Image BGR2GRAY**
 * Converts a color image from BGR (Blue-Green-Red) to grayscale.
 * Grayscale images reduce memory usage and computational cost since they contain only intensity information.
 * Useful as a preprocessing step for many image processing algorithms, like edge detection and object tracking.
   
Input Image:
![image3 resized](https://github.com/user-attachments/assets/5f9155ce-35c6-41cd-aa85-b0029042aa20)



Output Image:
![grayscale resized](https://github.com/user-attachments/assets/5e52d691-26f5-4a60-9c32-08f39a3297df)


**B. Image Blur**
 * Applies blurring to reduce image noise and smooth out details.
 * Common blurring techniques include Gaussian, median, and bilateral blurs.
 * Helps to remove small details, making it easier to detect larger features or objects.

Output Image:
![blur resized](https://github.com/user-attachments/assets/25b18be9-a0f1-46d6-8ec0-9fa28c022c1f)


  
**C. Image Contour**
 * Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
 * Useful for object recognition, shape analysis, and image segmentation.
 * Commonly used with thresholding or edge detection techniques to isolate contours.

Output Image: 
![contour resized](https://github.com/user-attachments/assets/a1d5bb26-ff06-4319-9fb4-61864a489827)


   
**D. Image Crop**
 * Extracts a specific region of interest (ROI) from the image.
 * Helps focus on relevant parts of the image and can improve computational efficiency.
 * Frequently used in facial recognition, object tracking, and image localization tasks.

Output Image: 
![crop resized](https://github.com/user-attachments/assets/d4a5bd9d-3138-4fc3-bda4-905847600dcc)

   
**E. Image cv2 (General OpenCV Operations)**
 * Refers to various OpenCV operations that can be applied to an image.
 * Common operations include color transformations, filtering, geometric transformations, and pixel-wise operations.
 * Serves as a base for many higher-level image processing tasks in computer vision.

Output Image:
![cv2 resized](https://github.com/user-attachments/assets/81ab42fd-a384-4d82-bbf8-47a7c0f036f6)

   
**F. Image Detect and Erosion**
 * Detects features and applies erosion to remove small noise or unwanted features.
 * Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.
 * Often combined with dilation (another morphological operation) to refine object shapes.

Output Image: 
![dilate_erode resized](https://github.com/user-attachments/assets/949c0b88-b78c-4aa3-be72-d4e60ef3b591)

   
**G. Image Edge Detection**
 * Identifies edges in the image by detecting changes in intensity using gradient techniques.
 * Common algorithms include Canny, Sobel, and Laplacian edge detectors.
 * Useful for finding object boundaries, lanes in road images, and other structural information.
   
Input Image:
![image2 resized](https://github.com/user-attachments/assets/726f966d-93ad-453a-81af-6acdc817513a)

Output Image: 
![edge resized](https://github.com/user-attachments/assets/6ff27159-5168-448d-8b05-3cc3e915a292)


   
**H. Image Histogram Equalization (Hist_eq)**
 * Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.
 * Helps in improving image visibility, especially in low-light conditions or images with low contrast.
 * Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.

Output Image: 
![hist resized](https://github.com/user-attachments/assets/db68d122-d01e-4c4d-bce3-36d5cd395604)



**I. Image HSV**
 * Converts an image from BGR to HSV (Hue, Saturation, Value) color space.
 * HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.
 * Widely used in color-based filtering and object tracking.

Output Image: 
![hsv resized](https://github.com/user-attachments/assets/7829671b-40cf-43a2-8ee0-c3894e41d742)



    
**J. Image Stack**
 * Combines multiple images into a single stacked format, often side-by-side or in a grid.
 * Useful for comparing processed images with the original or for creating multi-image displays.
 * Helps in visualizing step-by-step transformations in image processing.

Output Image: 
 Horizontal stacking:
![image_hor_stack resized](https://github.com/user-attachments/assets/d12813f1-07cf-4dea-a465-da458b85048e)

 
 Vertical stacking:
![image_ver_stack resized](https://github.com/user-attachments/assets/690e79b6-4868-47cf-95ad-d30525254fb8)



**K. Image Morph (Morphological Operations)**
 * Performs morphological transformations like dilation, erosion, opening, and closing.
 * Used for noise removal, enhancing object boundaries, and filling gaps.
 * Commonly applied after thresholding or edge detection for shape refinement.

Output Image:
![morph resized](https://github.com/user-attachments/assets/41ac272b-e82b-4304-a950-c0ab6c0407f0)

   
**L. Image Resize**
 * Changes the image dimensions while preserving or adjusting aspect ratio.
 * Important for preparing images for machine learning models that require fixed input sizes.
 * Can help balance image resolution with computational efficiency.

Output Image:
![resize resized](https://github.com/user-attachments/assets/71c4729c-0708-4134-b2e4-720d0374faa0)

   
**M. Image Rotate**
 * Rotates the image to a specified angle, either clockwise or counterclockwise.
 * Useful for correcting orientation or creating rotated data augmentations for models.
 * The rotation center and scale can be adjusted to control the rotation behavior.

Output Image:
![rotate resized](https://github.com/user-attachments/assets/dd250029-0df2-4f3f-a8a2-8ee98d6f2663)

   
**N. Image Template**
 * Creates a template for matching specific patterns or objects within an image.
 * Uses template matching techniques to find occurrences of the template in larger images.
 * Helpful in applications like logo detection, object localization, and pattern recognition.

Output Image:
![template resized](https://github.com/user-attachments/assets/877105d9-f7de-4402-95c5-03ef7ae11c4d)






**Video processing** :
Video processing refers to the manipulation, enhancement, and analysis of video data using various computational techniques. It involves applying algorithms to extract useful information, improve video quality, or transform the video for specific applications, such as computer vision, entertainment, security, or healthcare. Video processing encompasses a range of operations from basic editing to complex analysis, often performed in real-time or on pre-recorded content.

Libraries or Frameworks used- opencv

Version- 4.10.0.84

**Developed Logics-**

**A. Video Folder Path**
 * Specifies the directory for storing and accessing video files for organized processing.
 * Enables batch processing by allowing automated access to multiple videos.
 * Facilitates easy retrieval and organization of video datasets or archived footage.

Output Screenshot:
![folderpath resized](https://github.com/user-attachments/assets/9ce0118c-cc9e-48ca-b355-fb7bcd8a8bee)



**B. Video FPS (Frames Per Second)**
 * Controls the playback speed and smoothness of video.
 * Allows adjustment of video speed, such as slow-motion or time-lapse effects.
 * Essential for synchronization with audio and meeting playback standards.

 Output Screenshot:
 

![fps2 resized](https://github.com/user-attachments/assets/097466ce-75e7-4684-ba3b-be1e0c371fd7)

 
 
**C. Video Save**
 * Saves the processed video in a specified format (e.g., MP4, AVI).
 * Allows configuration of compression and resolution for quality and compatibility.
 * Supports adding metadata like timestamps or annotations for better tracking.
   
Output Screenshot: 
![save2](https://github.com/user-attachments/assets/9b025d89-c470-4f67-8aac-752d029267c1)



**D. Video Stream**
 * Captures live video from sources like webcams, IP cameras, or online streams.
 * Ideal for real-time applications like surveillance or live broadcasting.
 * Enables integration with processing features like motion detection or object tracking.
   
Output Screenshot: 
![stream resized](https://github.com/user-attachments/assets/836d56fc-0453-4b2f-85d5-cd80da445cf2)



**E. Video Stack**
 * Combines multiple frames side-by-side or sequentially for analysis.
 * Useful for visual comparisons, like original vs. processed frames.
 * Supports temporal visualization, aiding in monitoring changes over time.
   
Output Screenshot:
![video_stack resized](https://github.com/user-attachments/assets/cb670aed-7de3-4238-a779-63a59913615c)






**Annotations** :

Annotations in the context of data science, machine learning, and image/video processing refer to the process of adding descriptive or metadata labels to data. These labels provide additional context or information that helps in training algorithms, understanding data, or facilitating analysis. Annotations are particularly important in supervised learning, where models are trained using labeled data.

Libraries or Frameworks used- opencv ,LabelImg

Version- 4.10.0.84 ,1.8.6

**Developed Logics-**
 
**A. Data Segregate**
 * Splits data into different categories or sets for analysis based on certain criteria or characteristics.
 * Helps in organizing data into groups, making it easier to process, analyze, and draw meaningful conclusions.
 * Commonly used in machine learning to separate training, validation, and test datasets, or to organize data based on features like class labels, demographics, or time periods.
   
Output Screenshot:
![data_segregate resized](https://github.com/user-attachments/assets/8ddad4be-c127-47d9-95b5-1ed834833c4d)




**B. LabelImg**
 * Directory and File Handling:The code iterates through the label files in the specified label_dir and checks for corresponding images in image_dir. If the output directory does not exist, it creates it to save processed images with bounding boxes.
 *  Bounding Box Drawing:For each label file, the code reads bounding box information (class ID, x and y center, width, height), calculates the bounding box coordinates, and draws a green rectangle on the image to represent the bounding box.
 *  Output Image Saving:Each processed image with bounding boxes is saved to output_dir, and a confirmation message is printed for each successfully processed file.
   
Output Screenshot: 
![3](https://github.com/user-attachments/assets/79a5efb7-cdf4-46a4-958e-febc8b56e483)


**C. Label Manipulate**
 * Modifies or adjusts labels to refine data categories or correct labeling errors.
 * Can be used to handle mislabeled data or to reassign labels to reflect more accurate or refined categories, such as updating class labels based on new insights or correcting annotation mistakes.
 * Often used during data cleaning and preprocessing phases to improve the quality of the dataset and ensure the accuracy of the model being trained.
   
Output Screenshot: 
![data_label resized](https://github.com/user-attachments/assets/0037108e-2e8d-4688-a108-20e2a1b17f8b)





**Face Recognition** :

Face recognition is a biometric technology used to identify or verify individuals by analyzing their facial features. It involves capturing and analyzing facial patterns from an image or video and comparing them to a database of known faces to find a match. Face recognition can be used for both identification (determining who someone is) and verification (confirming someone’s identity).

Libraries or Frameworks used-

face_recognition -- 1.3.0
dlib --1 9.24.6
pandas -- 2.2.3
numpy  -- 2.1.2
datetime -- 5.5
imutils --0.5.4
opencv-python --4.10.0.84

**Developed Logics-**

**A. Maryam_attendance_save**

  1. **Face Recognition and Detection**:The code detects faces in real-time using the webcam, compares the detected face with a known face (Maryam), and identifies her if the match is above a certain confidence threshold.
  2. **Recording Attendance**:When Maryam is recognized, the system records the date and time in a DataFrame and saves the attendance to an Excel file once a specified number of recognitions (5) is reached.
  3. **Real-Time Video Processing**:The code captures video from the webcam, draws a bounding box around recognized faces, displays "Maryam" or "Not Maryam," and shows the video stream in real-time until the 'q' key is pressed.

Input Image: 
![nahida resized](https://github.com/user-attachments/assets/13c732ba-7378-40e6-9865-86fc94f8232f)


Output Screenshot:
![atten_save resized](https://github.com/user-attachments/assets/348ced9d-39a2-42d4-b347-61f4d5ca913c)



![atten resized](https://github.com/user-attachments/assets/59fa496a-25d2-4e6d-b6ce-f53d6872e3a3)


                              

**B. Maryam_atten_score**

 1.**Face Recognition and Attentiveness**:The code recognizes Maryam's face and calculates an attentiveness score based on her head pose (yaw and pitch). If the score is above 0.5, she is marked as attentive.
 2. **Logging and Saving Screenshots**:When Maryam is recognized, the program logs her attendance, attentiveness score, and saves a screenshot with a label indicating her attentiveness.
 3. **Periodic Data Saving**:The attendance and attentiveness data is saved to an Excel file every 30 seconds and also upon program exit to preserve the information.

Output Screenshot:

![Maryam_2024-11-08_19-01-27](https://github.com/user-attachments/assets/87019b0e-1714-4a95-a1a3-ff4bf08664f9)


![atte_score resized](https://github.com/user-attachments/assets/bcdb4b3d-8b6e-452a-b2d0-72363d5de34f)


**C. Maryam_avg_atten_score**

 1. **Face Recognition and Attentiveness Calculation**:The code recognizes Maryam's face and calculates an attentiveness score based on head pose (yaw and pitch). If the score is above 0.5, she is considered attentive.
 2.**Logging and Screenshot Saving**:When Maryam is detected, the program logs her attendance, attentiveness score, and saves a screenshot with a label indicating her attentiveness.
 3. **Periodic Data Saving and Average Calculation:**The code saves the attendance data to an Excel file every 30 seconds and calculates the average attentiveness score at the end of the session, appending it to the final log.

Output Screenshot:  ![Maryam_2024-11-08_19-13-04](https://github.com/user-attachments/assets/4b2cbcf3-3269-44b1-b4ce-818e67d82b19)

![avg_atten_score resized](https://github.com/user-attachments/assets/6ab3af9a-648c-426e-9476-2146aca6e82c)


**D. Maryam_excel_sc**

 1. **Face Recognition and Logging**:The code recognizes "Maryam" by comparing detected faces with a known image, logging her attendance in a DataFrame with a screenshot and timestamp when she is detected.
 2.**Time-based Logging and Gap Control**:It logs an entry for Maryam every 30 seconds, and if 5 minutes pass without recognition, it logs again. Screenshots are saved with each log.
 3. **Periodic Excel Saving**:The code periodically saves the attendance DataFrame to an Excel file every 30 seconds and at the end of the session, ensuring all recognized entries are recorded.

 Output Screenshot:
 
 ![Maryam_2024-11-08_18-18-19](https://github.com/user-attachments/assets/afe007bd-4aa3-47cc-950f-07d861f241df)


 ![excel resized](https://github.com/user-attachments/assets/f737a71f-79c7-4488-afad-7d67cf47863e)

 
 
 **E. Maryam_excel_sc_dt**

 1. **Face Recognition and Logging**: The code recognizes "Maryam" by comparing detected faces with a known image, and logs her attendance every 2 minutes or after a 5-minute gap, capturing screenshots with timestamps.
 2. **Time-Based Logging and Screenshot Saving**:Screenshots are saved with a timestamp on them, and the attendance of "Maryam" is logged in a DataFrame with a screenshot and time. New entries are logged if 2 minutes pass or if a 5-minute gap occurs.
 3. **Periodic Excel Saving**:The code saves the attendance DataFrame to an Excel file every 30 seconds, ensuring continuous logging, and performs a final save at the end of the session.

Output Screenshot: 


![Maryam_2024-11-08_18-37-28](https://github.com/user-attachments/assets/3837fa23-1bf9-4ffd-bf7c-47130c1eedb8)


![excel_date resized](https://github.com/user-attachments/assets/1e78e2d9-d83a-4665-8e1e-af18cb16ca1e)



 **F. Maryam_face_recog**

 1. **Face Recognition with Known Image**:The code loads a known image (presumed to be Maryam) and compares detected faces in the video stream with this known image using face encoding.
 2. **Face Detection and Recognition in Real-Time**:The camera continuously captures frames, detects faces, and compares them to the known face encoding. If the detected face matches the known image (based on a confidence threshold), it labels the face as "Maryam".
 3. **Display and Annotate Video Stream**:The code draws bounding boxes around recognized faces and displays the name "Maryam" or "Not Maryam" based on whether the face is recognized. The video stream continues until the user presses the 'q' key to stop it.

Output Screenshot:

![face_recog resized](https://github.com/user-attachments/assets/45332421-3c06-46cf-be0b-16f978c54c46)



**G. Maryam_landmark**

 1. **Face Recognition and Landmark Detection**:The code captures live video, detects faces, and compares them to a known image of Maryam. Upon recognizing Maryam, it performs facial landmark detection to analyze the head pose and detect attentiveness.
 2. **Head Pose Analysis for Attentiveness**:Using detected facial landmarks, the code estimates the head's yaw, pitch, and roll to determine if Maryam is attentive (i.e., facing forward with minimal head movement).
 3. **Screenshot and Data Logging**:If Maryam is attentive, a screenshot is saved with a label ("Attentive" or "Not Attentive"). This information, along with the date, time, and screenshot path, is logged in a DataFrame and saved to an Excel file every 30 seconds.

Output Screenshot: 


![Maryam_2024-11-08_19-19-03](https://github.com/user-attachments/assets/eeda78b0-2a54-4500-95c3-4d1eb630908f)



![landmark resized](https://github.com/user-attachments/assets/1a670ac4-cd10-472f-8d5c-ed72987b0bbf)



**H. Maryam_test**
 1. **Face Recognition and Attendance Logging**:The code uses the face_recognition library to recognize a known face (Maryam) from the webcam feed. If Maryam is detected, the code logs the recognition event in a DataFrame with the current date and time.
 2. **Entry Validity and Time Gap Handling**:The code checks if a person has been recognized within the last 2 minutes. If no recognition has occurred within that time, a new entry is logged. If 5 minutes have passed since the last entry, another entry is recorded for the same person.
 3. **Periodic Data Saving**:The attendance data (name, date, time) is saved to an Excel file (maryam_recognized_faces.xlsx) every 30 seconds, ensuring that the information is periodically backed up during the live video stream.

 Output Screenshot: 
 

![test resized](https://github.com/user-attachments/assets/fe87148e-2c71-4210-a5a8-3a494caa102c)

 


 
   



