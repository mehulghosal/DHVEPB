import cv2, _thread
import numpy as np
import imreg_dft.imreg as dft
from dataProcessing import save, display

def sparse(cap):

    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 50,
                           qualityLevel = 0.01,
                           minDistance = 2,
                           blockSize = 3)

    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (25,25),
                      maxLevel = 3,
                      criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # Create some random colors
    color = np.random.randint(0,255,(100,3))

    # Take first frame and find corners in it
    old_frame = cap.pop()
    first_frame = old_frame
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    points = []
    vector_frames = []
    errors = []

    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)
    try:
        for i in range(len(cap)):

            frame = cap.pop()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # calculate optical flow
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            
            points.append(p0)
            errors.append(err)

            # Select good points
            good_new = p1[st==1]
            good_old = p0[st==1]

            vector_frames.append(good_old)

            # draw the tracks
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
                frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
            img = cv2.add(frame,mask)

            # to display and debug, un-comment lines 55 & 63-65
            # display(img, t=500)

            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)
    except Exception as e:
        print(e)

    # cv2.destroyAllWindows()
    # display(img, name="last frame")
    # save(img, 'last_frame.png')
    print("vectors calculated")
    vector_frames = resize(vector_frames)
    return vector_frames, np.swapaxes(vector_frames, 0, 1), points

# takes list of 2-d np arrays
# condenses into one 3-d np array
def resize(vectors):
    l = len(vectors[0])
    for v in vectors:
        if not len(v) == l:
            v.resize(l, 2, refcheck=False)
    return np.stack(vectors)