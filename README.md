**Image processing** :
Image processing is a technique used to enhance, analyze, and manipulate digital images, typically through algorithms and computer vision tools. It involves a series of operations that transform an image to improve its quality, extract useful information, or prepare it for further analysis. Image processing has a wide array of applications, including photography, medical imaging, robotics, surveillance, and autonomous vehicles.

Libraries or Frameworks used- opencv

Version- 4.10.0.84

**Developed Logics**-
 
**A. Image BGR2GRAY**
 * Converts a color image from BGR (Blue-Green-Red) to grayscale.
 * Grayscale images reduce memory usage and computational cost since they contain only intensity information.
 * Useful as a preprocessing step for many image processing algorithms, like edge detection and object tracking.
   
Input Image: ![image3](https://github.com/user-attachments/assets/7084b142-5dbd-4224-b8b9-6df4bdce4dd5)

Output Image:![grayscale](https://github.com/user-attachments/assets/6edfbb35-9dc3-495b-9844-69d3e263f14e)

**B. Image Blur**
 * Applies blurring to reduce image noise and smooth out details.
 * Common blurring techniques include Gaussian, median, and bilateral blurs.
 * Helps to remove small details, making it easier to detect larger features or objects.

Output Image:![blur](https://github.com/user-attachments/assets/69e5a335-db01-4e97-93d7-677fe1925428)
  
**C. Image Contour**
 * Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
 * Useful for object recognition, shape analysis, and image segmentation.
 * Commonly used with thresholding or edge detection techniques to isolate contours.

Output Image: ![contour](https://github.com/user-attachments/assets/ba1ddf2a-5c44-4846-9be5-8ad4093043b5)
   
**D. Image Crop**
 * Extracts a specific region of interest (ROI) from the image.
 * Helps focus on relevant parts of the image and can improve computational efficiency.
 * Frequently used in facial recognition, object tracking, and image localization tasks.

Output Image: ![crop](https://github.com/user-attachments/assets/18daa9ea-7918-4537-8461-d9dd9d87f357)
   
**E. Image cv2 (General OpenCV Operations)**
 * Refers to various OpenCV operations that can be applied to an image.
 * Common operations include color transformations, filtering, geometric transformations, and pixel-wise operations.
 * Serves as a base for many higher-level image processing tasks in computer vision.

Output Image:![cv2](https://github.com/user-attachments/assets/9e0fa718-a9fb-4e17-98e6-861f76209e8d)
   
**F. Image Detect and Erosion**
 * Detects features and applies erosion to remove small noise or unwanted features.
 * Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.
 * Often combined with dilation (another morphological operation) to refine object shapes.

Output Image: ![dilate_erode](https://github.com/user-attachments/assets/a2019e7d-d13f-42ef-90a3-a781dcf729a2)
   
**G. Image Edge Detection**
 * Identifies edges in the image by detecting changes in intensity using gradient techniques.
 * Common algorithms include Canny, Sobel, and Laplacian edge detectors.
 * Useful for finding object boundaries, lanes in road images, and other structural information.
   
Input Image: ![image2](https://github.com/user-attachments/assets/d70d2cfa-6e9d-45ca-b788-8ed91d53e8c2)

Output Image: ![edge](https://github.com/user-attachments/assets/cda59dcf-aea2-42b2-b6d1-afa14765a343)
   
**H. Image Histogram Equalization (Hist_eq)**
 * Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.
 * Helps in improving image visibility, especially in low-light conditions or images with low contrast.
 * Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.

Output Image: ![hist](https://github.com/user-attachments/assets/2f6afd37-60fb-4f6f-b97a-1dc4cef17c3b)
   
**I. Image HSV**
 * Converts an image from BGR to HSV (Hue, Saturation, Value) color space.
 * HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.
 * Widely used in color-based filtering and object tracking.

Output Image: ![hsv](https://github.com/user-attachments/assets/b27ef0ec-3640-437b-853d-d993227a8378)
   
**J. Image Stack**
 * Combines multiple images into a single stacked format, often side-by-side or in a grid.
 * Useful for comparing processed images with the original or for creating multi-image displays.
 * Helps in visualizing step-by-step transformations in image processing.

Output Image: 
 Horizontal stacking: ![image_hor_stack](https://github.com/user-attachments/assets/90bac040-7f05-49d8-a9ec-f7a26b89147c)
 Vertical stacking: ![image_ver_stack](https://github.com/user-attachments/assets/cd24543c-efff-4b56-abf1-311cec21bba7)


**K. Image Morph (Morphological Operations)**
 * Performs morphological transformations like dilation, erosion, opening, and closing.
 * Used for noise removal, enhancing object boundaries, and filling gaps.
 * Commonly applied after thresholding or edge detection for shape refinement.

Output Image: ![morph](https://github.com/user-attachments/assets/cd0ffe68-2248-4354-8685-8d0e1bda71ae)
   
**L. Image Resize**
 * Changes the image dimensions while preserving or adjusting aspect ratio.
 * Important for preparing images for machine learning models that require fixed input sizes.
 * Can help balance image resolution with computational efficiency.

Output Image: ![resize](https://github.com/user-attachments/assets/ecde1aff-9fcd-4850-afbb-0787dbf4c589)
   
**M. Image Rotate**
 * Rotates the image to a specified angle, either clockwise or counterclockwise.
 * Useful for correcting orientation or creating rotated data augmentations for models.
 * The rotation center and scale can be adjusted to control the rotation behavior.

Output Image: ![rotate](https://github.com/user-attachments/assets/e41de2b1-7176-4b3f-b1f7-1be98e63f1c9)
   
**N. Image Template**
 * Creates a template for matching specific patterns or objects within an image.
 * Uses template matching techniques to find occurrences of the template in larger images.
 * Helpful in applications like logo detection, object localization, and pattern recognition.

Output Image: ![template](https://github.com/user-attachments/assets/9d476ecb-ed49-4827-9602-3064e5ddb858)
   



**Video processing** :
Libraries or Frameworks used- opencv
Version- 4.10.0.84
Developed Logics-
 A.Video Folder Path:Specifies the folder path where video files are stored.
 B.Video FPS: Sets the frames per second (fps) for controlling video playback speed.
 C.Video Save: Saves the processed video to a specified file format.
 D.Video Stream: Captures live video feed from a camera or streaming source.
 E.Video Stack: Combines multiple video frames for side-by-side or sequential analysis.

**Annotations** :
Libraries or Frameworks used- opencv ,LabelImg
Version- 4.10.0.84 ,1.8.6
Developed Logics-
 A. Data Segregate : Splits data into different categories or sets for analysis.
 B. Labelling : Assigns labels or annotations to data for classification.
 C. Label Manipulate : Modifies or adjusts labels to refine data categories or correct errors.

**Face Recognition** :
Libraries or Frameworks used-
face_recognition -- 1.3.0
dlib --1 9.24.6
pandas -- 2.2.3
numpy  -- 2.1.2
datetime -- 5.5
imutils --0.5.4
opencv-python --4.10.0.84
Developed Logics-
  A. Maryam_attendance_save
  B. Maryam_atten_score
  C. Maryam_avg_atten_score
  D. Maryam_excel_sc
  E. Maryam_excel_sc_dt
  F. Maryam_face_recog
  G. Maryam_landmark
  H. Maryam_test
 
 
 
  
