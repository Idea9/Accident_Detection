import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (3, 3), (510, 510), (255, 0, 0), 15)
cv2.circle(img,(447,63), 63, (0,0,255), 3)
cv2.circle(img,(447,63), 15, (0,233,255), -40)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# bo line nic nie zwraca, a jedynie dziala na elemencie ktory otrzymal
cv2.imwrite("line.bmp", img)

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
