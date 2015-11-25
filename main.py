import numpy as np
import cv2

img = cv2.imread("jennifer.jpg", 0)
# 1-color 0-grey -1-with alpha-channel
print img
# print return none if there is no image, that is debuging, no error code for empty image
cv2.namedWindow('windowName', cv2.WINDOW_AUTOSIZE)
# that might be useful later, it create windows for now without image on it, you can specify window size for now
cv2.imshow("windowName", img)
# do as many windows as you like, just with unique name
cv2.imwrite("deadJennifer.jpg", img)
# just save the picture
cv2.waitKey(0)
# it waits 0 ms for keystroke, you can specified key also but not now
cv2.destroyAllWindows()
# figure it out asshole