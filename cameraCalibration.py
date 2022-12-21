import numpy as np
import cv2 as cv
import glob
# termination criteria : defining the dimensions of the chessboard
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0) defining the world coordinates for 3D points
objp = np.zeros((7*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:7].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

#extracting path of individual image stored in a given directory
images = glob.glob('*.jpg')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (6,7), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        #refining pixel coordinates for given 2D points
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (6,7), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(0)
    
cv.destroyAllWindows()

"""
Performing camera calibration by 
passing the value of known 3D points (objpoints)
and corresponding pixel coordinates of the 
detected corners (imgpoints)
"""

h,w = img.shape[:2]
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix : \n")
print(mtx)
print("distortion : \n")
print(dist)
print("rotation vectors : \n")
print(rvecs)
print("translation vectors : \n")
print(tvecs)

np.savez("cameraParams", mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
