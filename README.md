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


![image3 resized](https://github.com/user-attachments/assets/fe5b6486-10d9-44b9-b2ea-75a734e151df)


Output Image:


![grayscale resized](https://github.com/user-attachments/assets/d373029f-fd42-4f7f-8682-cc3e8d506bea)



**B. Image Blur**
 * Applies blurring to reduce image noise and smooth out details.
 * Common blurring techniques include Gaussian, median, and bilateral blurs.
 * Helps to remove small details, making it easier to detect larger features or objects.

Output Image:


![blur resized](https://github.com/user-attachments/assets/2507d3f4-9bf9-4e2f-abb2-a45342b69557)


  
**C. Image Contour**
 * Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
 * Useful for object recognition, shape analysis, and image segmentation.
 * Commonly used with thresholding or edge detection techniques to isolate contours.

Output Image: 


![contour resized](https://github.com/user-attachments/assets/bc594938-c4fd-46c2-8d41-9148c882bb24)



**D. Image Crop**
 * Extracts a specific region of interest (ROI) from the image.
 * Helps focus on relevant parts of the image and can improve computational efficiency.
 * Frequently used in facial recognition, object tracking, and image localization tasks.

Output Image: 


![crop resized](https://github.com/user-attachments/assets/fcb798e5-2a4e-46b6-ab9c-28a69214777c)


   
**E. Image cv2 (General OpenCV Operations)**
 * Refers to various OpenCV operations that can be applied to an image.
 * Common operations include color transformations, filtering, geometric transformations, and pixel-wise operations.
 * Serves as a base for many higher-level image processing tasks in computer vision.

Output Image:


![cv2 resized](https://github.com/user-attachments/assets/29f8788b-5b57-46fc-870e-2b1cd150cc01)


   
**F. Image Detect and Erosion**
 * Detects features and applies erosion to remove small noise or unwanted features.
 * Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.
 * Often combined with dilation (another morphological operation) to refine object shapes.

Output Image: 


![dilate_erode resized](https://github.com/user-attachments/assets/d927f429-da32-4887-8a6a-e5b6436cf468)


   
**G. Image Edge Detection**
 * Identifies edges in the image by detecting changes in intensity using gradient techniques.
 * Common algorithms include Canny, Sobel, and Laplacian edge detectors.
 * Useful for finding object boundaries, lanes in road images, and other structural information.
   
Input Image:


![image2 resized](https://github.com/user-attachments/assets/68482904-ef41-4588-b275-7cf79dcbf548)

 
Output Image: 


![edge resized](https://github.com/user-attachments/assets/51f77510-83bc-4be2-9e64-9e1e0e87d857)


   
**H. Image Histogram Equalization (Hist_eq)**
 * Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.
 * Helps in improving image visibility, especially in low-light conditions or images with low contrast.
 * Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.

Output Image: 


![hist resized](https://github.com/user-attachments/assets/614ce3dc-8377-413c-ae68-521ee16deaee)



**I. Image HSV**
 * Converts an image from BGR to HSV (Hue, Saturation, Value) color space.
 * HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.
 * Widely used in color-based filtering and object tracking.

Output Image: 


![hsv](https://github.com/user-attachments/assets/b27ef0ec-3640-437b-853d-d993227a8378)


   
**J. Image Stack**
 * Combines multiple images into a single stacked format, often side-by-side or in a grid.
 * Useful for comparing processed images with the original or for creating multi-image displays.
 * Helps in visualizing step-by-step transformations in image processing.

Output Image: 

 Horizontal stacking:

 
 ![image_hor_stack resized](https://github.com/user-attachments/assets/c537f9d4-efa8-448f-8d5b-e4e675cadf20)

 
 Vertical stacking:

 
 ![image_ver_stack resized](https://github.com/user-attachments/assets/8bffc275-9aee-4cf3-82e2-12d96b89bbec)



**K. Image Morph (Morphological Operations)**
 * Performs morphological transformations like dilation, erosion, opening, and closing.
 * Used for noise removal, enhancing object boundaries, and filling gaps.
 * Commonly applied after thresholding or edge detection for shape refinement.

Output Image:


![morph resized](https://github.com/user-attachments/assets/30fefaac-eb17-4e66-9746-2b616f8f7631)


   
**L. Image Resize**
 * Changes the image dimensions while preserving or adjusting aspect ratio.
 * Important for preparing images for machine learning models that require fixed input sizes.
 * Can help balance image resolution with computational efficiency.

Output Image:


![resize resized](https://github.com/user-attachments/assets/c948071d-8adf-4bf4-a915-1d7216d36bb9)


   
**M. Image Rotate**
 * Rotates the image to a specified angle, either clockwise or counterclockwise.
 * Useful for correcting orientation or creating rotated data augmentations for models.
 * The rotation center and scale can be adjusted to control the rotation behavior.

Output Image:


![rotate resized](https://github.com/user-attachments/assets/1a443313-1fe1-46f5-a3ec-d2df7ce32392)


   
**N. Image Template**
 * Creates a template for matching specific patterns or objects within an image.
 * Uses template matching techniques to find occurrences of the template in larger images.
 * Helpful in applications like logo detection, object localization, and pattern recognition.

Output Image:


![template resized](https://github.com/user-attachments/assets/a77e9c47-d24a-400f-9416-8e58038f0b2c)





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


![folderpath resized](https://github.com/user-attachments/assets/c860b54c-4b4d-4616-bb36-8fd5a72550b0)



**B. Video FPS (Frames Per Second)**
 * Controls the playback speed and smoothness of video.
 * Allows adjustment of video speed, such as slow-motion or time-lapse effects.
 * Essential for synchronization with audio and meeting playback standards.

 Output Screenshot:

 
 ![fps resized](https://github.com/user-attachments/assets/3ccd0b5c-8324-43b7-9f84-811caa1125e9)



 ![fps2 resized](https://github.com/user-attachments/assets/97d1b5f0-7ff3-42ee-b83b-597d2ca275a6)

 
 
**C. Video Save**
 * Saves the processed video in a specified format (e.g., MP4, AVI).
 * Allows configuration of compression and resolution for quality and compatibility.
 * Supports adding metadata like timestamps or annotations for better tracking.
   
Output Screenshot: 


![save2 resized](https://github.com/user-attachments/assets/6b182547-492c-403a-92d5-6de58f6f2c53)



**D. Video Stream**
 * Captures live video from sources like webcams, IP cameras, or online streams.
 * Ideal for real-time applications like surveillance or live broadcasting.
 * Enables integration with processing features like motion detection or object tracking.
   
Output Screenshot:


![stream resized](https://github.com/user-attachments/assets/ef639c05-0c00-4a0f-a2ca-e9e34f299e2f)



**E. Video Stack**
 * Combines multiple frames side-by-side or sequentially for analysis.
 * Useful for visual comparisons, like original vs. processed frames.
 * Supports temporal visualization, aiding in monitoring changes over time.
   
Output Screenshot:


![video_stack](https://github.com/user-attachments/assets/a757f5be-c86f-415a-8117-73d03a91f02d)






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


![data_segregate resized](https://github.com/user-attachments/assets/fe6679ff-03b4-4116-a741-bccc11a8d372)



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


![data_label resized](https://github.com/user-attachments/assets/1f942994-c289-42e9-a599-384b1d7e08d2)




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

Output Screenshot: 


![Maryam_2024-11-08_19-13-04](https://github.com/user-attachments/assets/4b2cbcf3-3269-44b1-b4ce-818e67d82b19)


![avg_atten_score resized](https://github.com/user-attachments/assets/6ab3af9a-648c-426e-9476-2146aca6e82c)



**D. Maryam_excel_sc**

 1. **Face Recognition and Logging**:The code recognizes "Maryam" by comparing detected faces with a known image, logging her attendance in a DataFrame with a screenshot and timestamp when she is detected.
 2.**Time-based Logging and Gap Control**:It logs an entry for Maryam every 30 seconds, and if 5 minutes pass without recognition, it logs again. Screenshots are saved with each log.
 3. **Periodic Excel Saving**:The code periodically saves the attendance DataFrame to an Excel file every 30 seconds and at the end of the session, ensuring all recognized entries are recorded.

 Output Screenshot:

 
 ![Maryam_2024-11-08_18-17-49 resized](https://github.com/user-attachments/assets/60f86781-fa9f-4000-aa55-58b1cd8a9f93)


 ![excel resized](https://github.com/user-attachments/assets/c24ace1e-b1dc-473a-ad4f-3d331443abaf)



  **E. Maryam_excel_sc_dt**

 1. **Face Recognition and Logging**: The code recognizes "Maryam" by comparing detected faces with a known image, and logs her attendance every 2 minutes or after a 5-minute gap, capturing screenshots with timestamps.
 2. **Time-Based Logging and Screenshot Saving**:Screenshots are saved with a timestamp on them, and the attendance of "Maryam" is logged in a DataFrame with a screenshot and time. New entries are logged if 2 minutes pass or if a 5-minute gap occurs.
 3. **Periodic Excel Saving**:The code saves the attendance DataFrame to an Excel file every 30 seconds, ensuring continuous logging, and performs a final save at the end of the session.

Output Screenshot: 


![Maryam_2024-11-08_18-37-28 resized](https://github.com/user-attachments/assets/65272451-b736-4798-b2f5-56d0f69d3cf8)


![excel_date resized](https://github.com/user-attachments/assets/1e78e2d9-d83a-4665-8e1e-af18cb16ca1e)



 **F. Maryam_face_recog**

 1. **Face Recognition with Known Image**:The code loads a known image (presumed to be Maryam) and compares detected faces in the video stream with this known image using face encoding.
 2. **Face Detection and Recognition in Real-Time**:The camera continuously captures frames, detects faces, and compares them to the known face encoding. If the detected face matches the known image (based on a confidence threshold), it labels the face as "Maryam".
 3. **Display and Annotate Video Stream**:The code draws bounding boxes around recognized faces and displays the name "Maryam" or "Not Maryam" based on whether the face is recognized. The video stream continues until the user presses the 'q' key to stop it.

Output Screenshot:


![face_recog resized](https://github.com/user-attachments/assets/4750d540-dd60-426f-b672-327ad8f53b18)



**G. Maryam_landmark**

 1. **Face Recognition and Landmark Detection**:The code captures live video, detects faces, and compares them to a known image of Maryam. Upon recognizing Maryam, it performs facial landmark detection to analyze the head pose and detect attentiveness.
 2. **Head Pose Analysis for Attentiveness**:Using detected facial landmarks, the code estimates the head's yaw, pitch, and roll to determine if Maryam is attentive (i.e., facing forward with minimal head movement).
 3. **Screenshot and Data Logging**:If Maryam is attentive, a screenshot is saved with a label ("Attentive" or "Not Attentive"). This information, along with the date, time, and screenshot path, is logged in a DataFrame and saved to an Excel file every 30 seconds.

Output Screenshot: 


![Maryam_2024-11-08_19-19-03](https://github.com/user-attachments/assets/eeda78b0-2a54-4500-95c3-4d1eb630908f)



![landmark resized](https://github.com/user-attachments/assets/da322ece-246f-450d-bf18-7de0e52231bc)



**H. Maryam_test**
 1. **Face Recognition and Attendance Logging**:The code uses the face_recognition library to recognize a known face (Maryam) from the webcam feed. If Maryam is detected, the code logs the recognition event in a DataFrame with the current date and time.
 2. **Entry Validity and Time Gap Handling**:The code checks if a person has been recognized within the last 2 minutes. If no recognition has occurred within that time, a new entry is logged. If 5 minutes have passed since the last entry, another entry is recorded for the same person.
 3. **Periodic Data Saving**:The attendance data (name, date, time) is saved to an Excel file (maryam_recognized_faces.xlsx) every 30 seconds, ensuring that the information is periodically backed up during the live video stream.

 Output Screenshot: 
 

![test resized](https://github.com/user-attachments/assets/fe87148e-2c71-4210-a5a8-3a494caa102c)
 


 
   



