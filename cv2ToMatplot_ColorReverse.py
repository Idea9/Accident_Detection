import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("img/jennifer.jpg")
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# img2 = np.array(img)
# img2 = img2[:,:,::-1]
print b
plt.imshow(img2, interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()