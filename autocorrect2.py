import cv2
import cv2.cv as cv
import numpy as np
from matplotlib import pyplot as plt

#capture = cv.CaptureFromCAM(0)
img = cv2.imread('test.jpg',1)

height,width,depth = img.shape
size = height,width,3
channels = np.zeros(size , np.uint8) 


cv2.imshow("test.jpg",img)
hist = cv2.calcHist([img],[2],None,[256],[0,256])

#convert img to YCR_CB
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

#split image to Y, CR, CB
channels = cv2.split(img2)

#histogram equalization to Y-MATRIX
cv2.equalizeHist(channels[0],channels[0])

#merge this matrix to reconstruct our colored image
cv2.merge(channels,img2)

#convert this output image to rgb
rgb = cv2.cvtColor(img2,cv2.COLOR_YCR_CB2BGR)
hist2 = cv2.calcHist([rgb],[2],None,[256],[0,256])
plt.plot(hist)
plt.plot(hist2)
plt.show()