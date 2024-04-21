Real-Time Face Detection with OpenCV

## Overview
---------
This project implements real-time face detection using OpenCV, a popular computer vision library. It captures video frames from a webcam, detects faces in each frame, and draws rectangles around the detected faces. This README provides an overview of the project, including setup instructions and usage guidelines.

##  Requirements
------------
- Python 3.x
- OpenCV library (opencv-python)

## Installation
------------
1. Clone the repository:
   git clone https://github.com/your_username/face-detection.git
   
2. Navigate to the project directory:
   cd face-detection
   
3. Install the required libraries using pip:
   pip install opencv-python

## Usage
-----
1. Run the Python script `face_detection.py`:
   python face_detection.py
   
2. A window titled "video_live" will open, displaying the live video feed from your webcam.

3. The script will continuously detect faces in the video feed and draw green rectangles around them.

4. Press the "b" key on your keyboard to exit the program and close the video window.

## Customization
-------------
- You can adjust parameters like the scaling factor, minimum neighbors, and minimum size of detected faces in the `face_detection.py` script to fine-tune the face detection process.
- Experiment with different values to optimize the detection accuracy for your specific use case.


## Acknowledgements
----------------
- This project was inspired by tutorials and documentation from the OpenCV library.
- Thanks to the open-source community for their contributions to the development of computer vision technologies.
