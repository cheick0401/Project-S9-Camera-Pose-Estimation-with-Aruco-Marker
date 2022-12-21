import os
from symbol import parameters
import numpy as np
import cv2
import cv2.aruco as aruco


def main():

    #Find the marqueur from the 4x4 dictionary
    marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    #Marker detection parameters
    param_markers = aruco.DetectorParameters_create()

    #Get access to the first camera or the only one
    cap = cv2.VideoCapture(0)

    while True:
        _, img=cap.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change the grayscale
        marker_corners, marker_IDs, reject = aruco.detectMarkers(
            gray_img, marker_dict, parameters= param_markers
        )
        #print("les coins sont :",marker_corners)
        #print("l'identifiant est :",marker_ids)


        #allow to draw a box around the detected marker
        if marker_corners:
            for ids, corners in zip(marker_IDs, marker_corners):
                cv2.polylines(
                    img, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA
                )

            
        if cv2.waitKey(1)==113: #press 'q' to quit
            break
        cv2.imshow("img", img)
    cap.release()
    cv2.destroyAllWindows()



    




if __name__=='__main__':
    main()



      