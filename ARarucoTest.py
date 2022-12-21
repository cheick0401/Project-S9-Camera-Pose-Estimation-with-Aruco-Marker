import numpy as np
import time
import cv2
import os
import cv2.aruco as aruco

# Load previously saved data
with np.load('cameraParams.npz') as file:
    mtx, dist, rvecs, tvecs = [file[i] for i in ('mtx','dist','rvecs','tvecs')]


def image_augmentation(frame, src_image, dst_points):
    src_h, src_w = src_image.shape[:2]
    h1, w1 = frame.shape[:2]
    mask = np.zeros((h1, w1), dtype=np.uint8)
    src_points = np.array([[0, 0], [src_w, 0], [src_w, src_h], [0, src_w]])
    H, _ = cv2.findHomography(srcPoints=src_points, dstPoints=dst_points)
    warp_image = cv2.warpPerspective(src_image, H, (h1, w1))
    cv2.imshow("warp image", warp_image)
    cv2.fillConvexPoly(mask, dst_points, 255)
    results = cv2.bitwise_and(warp_image, warp_image, frame, mask=mask)




marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters_create()

AR_images = cv2.imread("C:/Users/cheick Diaby/Desktop/5A GPSE/projet_S9/ARImage.png")


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):

            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            image_augmentation(frame, AR_images, corners)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()





"""cap = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)

#num = 0
while True:
    ret, frame = cap.read()
    h1, w1 = frame.shape[:2]
    # Read the camera picture

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    #Marker detection parameters
    param_markers = aruco.DetectorParameters_create()
    #dst1 = cv2.undistort(frame, mtx, dist, None, newcameramtx)

    images_list = read_images("ARImage.png")

    #Use aruco The detectmarkers() function can detect the marker and return the ID and the coordinates of the four corners of the sign board
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,marker_dict,parameters= param_markers)
	
	   #Use aruco The detectmarkers() function can detect the marker and return the ID and the coordinates of the four corners of the sign board
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,marker_dict,parameters= param_markers)
    
#    If you can't find it, type id
    if ids is not None:

        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)

        cv2.drawFrameAxes(frame, mtx, dist, rvecs, tvecs, 0.1) #Draw axis
        aruco.drawDetectedMarkers(frame, corners) #Draw a square around the mark


		
        cv2.putText(frame, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)
		

    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

	#allow to draw a box around the detected marker
	

    # Display result frame
    if cv2.waitKey(1)==113: #press 'q' to quit
            break
    cv2.imshow("img", frame)


cap.release()
cv2.destroyAllWindows()"""



  
 
   