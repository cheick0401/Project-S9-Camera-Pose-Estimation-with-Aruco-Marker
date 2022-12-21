# Project-S9-Camera-Pose-Estimation-with-Aruco-Marker
This following repository contains all the tree for the S9 project inluding (camera calibration, aruco detection, camera pose estimation and AR with aruco marker)

Camera calibration

We want to extract the calibrate matrix to have the intrinsic parameters of our camera like focal length and optical centers. We are going to base our process on the pinhole model which is the most common camera model used. pinhole model = it describes the mathematical relationship between the coordinates of a point in three dimensional space and its reprojection onto the image plane. the cameraCalibration.py are going to return 2 numpy arrays (the calibrate matrix and the distortion matrix).

Aruco marker detection 
Our aruco marker has been extracted from the specific dictionary 4x4_50 and its identifier is 0 that means that it the first aruco marker of ths dictionary. While the 4 corners of our aruco marker has been capted by the camera a virtual signal (yellow square box) appear to give the information that our aruco marker has been corectly detected, The code is projetc_arUco1.py.

Pose estimation
After extracted the calibrate matrix we are going to do the pose estimation which include a translation 3D (to coincid the world coordinate system and the camera coordinate system) and a rotation 3D (to align the two coordinates system) with the code project_aruo_poseEstimation.py. After this operation we have transposed our aruco marker in its coordinate system to the camera coordinate system so we now know the position and the orientation of our camera and can to some application la tracking or augmented reality;

Augmented reality with aruco marker
After detected our aruco marker and know the orientation and position of our camera in a given environment we are going to match a virtual image with our aruco marker by knowing the aruco marker size and the border size. While the aruco marker has been detected we will see a virtual image instead of the aruco marker. The code is ARarucoTest.py

Inputs
There are all the chessboard used for calibration, the virtual image for AR and the aruco marker used.

Outputs
There are all the outputs after running all the different process (aruco detection, calibration, pose estimation and AR).
