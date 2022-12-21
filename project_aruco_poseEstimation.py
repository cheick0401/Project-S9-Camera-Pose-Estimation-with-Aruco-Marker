import numpy as np
import time
import cv2
import cv2.aruco as aruco



with np.load('cameraParams.npz') as file:
    mtx, dist, rvecs, tvecs = [file[i] for i in ('mtx','dist','rvecs','tvecs')]

cap = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)


while True:
    ret, frame = cap.read()
    h1, w1 = frame.shape[:2]
    # Read the camera picture

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    #Marker detection parameters
    param_markers = aruco.DetectorParameters_create()

    #Use aruco The detectmarkers() function can detect the marker and return the ID and the coordinates of the four corners of the sign board
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,marker_dict,parameters= param_markers)
	
	#Use aruco The detectmarkers() function can detect the marker and return the ID and the coordinates of the four corners of the sign board
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,marker_dict,parameters= param_markers)
    
#    If you can't find it, type id
    if ids is not None:

        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
        # Estimate the attitude of each marker and return the values rvet and tvec --- different
        # from camera coeficcients
        #(rvec-tvec).any() # get rid of that nasty numpy value array error

        cv2.drawFrameAxes(frame, mtx, dist, rvecs, tvecs, 0.1) #Draw axis
        aruco.drawDetectedMarkers(frame, corners) #Draw a square around the mark
		
        cv2.putText(frame, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)
		

    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)
	
    # Display result frame
    if cv2.waitKey(1)==113: #press 'q' to quit
            break
    cv2.imshow("img", frame)
cap.release()
cv2.destroyAllWindows()



  
 
   