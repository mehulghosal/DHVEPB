import cv2
import numpy as np
    
# not working exactly with a video - working with list of files
# cap is list of image files
def flow(cap):

    frame1 = cap.pop(0)
    prvs = frame1.copy()
    hsv = np.empty([551, 501, 3], dtype=np.uint8)
    hsv[...,1] = 255

    for i in range(len(cap)-1):
        frame2 = cap.pop(0)
        nextt = frame2.copy()

        flow = cv2.calcOpticalFlowFarneback(prvs,nextt, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        hsv[...,0] = ang*180/np.pi/2
        hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        print(hsv)
        rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

        cv2.imshow('frame2',rgb)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break

        prvs = nextt

    cv2.destroyAllWindows()