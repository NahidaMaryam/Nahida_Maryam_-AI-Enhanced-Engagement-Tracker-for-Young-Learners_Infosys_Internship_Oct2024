**Image processing** :
Libraries or Frameworks used- opencv
Version- 4.10.0.84
**Developed Logics**-
  A.Image BGR2GRAY: Converts a color image from BGR to grayscale.
  B.Image Blur: Applies blurring to reduce image noise and details.
  C.Image Contour: Detects and outlines the contours of objects within an image.
  D.Image Crop: Extracts a specific region of interest from the image.
  E.Image cv2: A general OpenCV operation applied to the image.
  F.Image Detect and Erosion: Detects features and applies erosion to remove small noise.
  G.Image Edge Detection: Identifies edges in the image using gradient techniques.
  H.Image Histogram Equalization (Hist_eq): Enhances image contrast by equalizing its histogram.
  I.Image HSV: Converts an image from BGR to HSV color space.
  J.Image Stack: Combines multiple images into a single stacked format.
  K.Image Morph: Performs morphological transformations like dilation or erosion.
  L.Image Resize: Changes the image dimensions while preserving aspect ratio.
  N.Image Rotate: Rotates the image to a specified angle.
  M.Image Template: Creates a template for matching specific patterns within an image.

**A. Image BGR2GRAY**
 * Converts a color image from BGR (Blue-Green-Red) to grayscale.
 * Grayscale images reduce memory usage and computational cost since they contain only intensity information.
 * Useful as a preprocessing step for many image processing algorithms, like edge detection and object tracking.
Input Image: ![image3](https://github.com/user-attachments/assets/7084b142-5dbd-4224-b8b9-6df4bdce4dd5)

Output Image:![grayscale](https://github.com/user-attachments/assets/6edfbb35-9dc3-495b-9844-69d3e263f14e)


  
B. Image Blur
Applies blurring to reduce image noise and smooth out details.
Common blurring techniques include Gaussian, median, and bilateral blurs.
Helps to remove small details, making it easier to detect larger features or objects.
C. Image Contour
Detects and outlines the contours of objects within an image, often based on shape or intensity changes.
Useful for object recognition, shape analysis, and image segmentation.
Commonly used with thresholding or edge detection techniques to isolate contours.
D. Image Crop
Extracts a specific region of interest (ROI) from the image.
Helps focus on relevant parts of the image and can improve computational efficiency.
Frequently used in facial recognition, object tracking, and image localization tasks.
E. Image cv2 (General OpenCV Operations)
Refers to various OpenCV operations that can be applied to an image.
Common operations include color transformations, filtering, geometric transformations, and pixel-wise operations.
Serves as a base for many higher-level image processing tasks in computer vision.
F. Image Detect and Erosion
Detects features and applies erosion to remove small noise or unwanted features.
Erosion reduces the thickness of object boundaries, which can be useful for separating close objects.
Often combined with dilation (another morphological operation) to refine object shapes.
G. Image Edge Detection
Identifies edges in the image by detecting changes in intensity using gradient techniques.
Common algorithms include Canny, Sobel, and Laplacian edge detectors.
Useful for finding object boundaries, lanes in road images, and other structural information.
H. Image Histogram Equalization (Hist_eq)
Enhances image contrast by equalizing its histogram, making details in different brightness ranges more visible.
Helps in improving image visibility, especially in low-light conditions or images with low contrast.
Adaptive histogram equalization (CLAHE) can be used for localized contrast enhancement.
I. Image HSV
Converts an image from BGR to HSV (Hue, Saturation, Value) color space.
HSV makes color-based segmentation and detection easier as hue and saturation channels separate color and intensity.
Widely used in color-based filtering and object tracking.
J. Image Stack
Combines multiple images into a single stacked format, often side-by-side or in a grid.
Useful for comparing processed images with the original or for creating multi-image displays.
Helps in visualizing step-by-step transformations in image processing.
K. Image Morph (Morphological Operations)
Performs morphological transformations like dilation, erosion, opening, and closing.
Used for noise removal, enhancing object boundaries, and filling gaps.
Commonly applied after thresholding or edge detection for shape refinement.
L. Image Resize
Changes the image dimensions while preserving or adjusting aspect ratio.
Important for preparing images for machine learning models that require fixed input sizes.
Can help balance image resolution with computational efficiency.
M. Image Rotate
Rotates the image to a specified angle, either clockwise or counterclockwise.
Useful for correcting orientation or creating rotated data augmentations for models.
The rotation center and scale can be adjusted to control the rotation behavior.
N. Image Template
Creates a template for matching specific patterns or objects within an image.
Uses template matching techniques to find occurrences of the template in larger images.
Helpful in applications like logo detection, object localization, and pattern recognition.



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
 
 
 
  
