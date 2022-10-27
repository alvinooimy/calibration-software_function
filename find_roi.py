import numpy as np
import cv2

sImagePath = "./image/hello.bmp"
nImage = cv2.imread(sImagePath, cv2.IMREAD_GRAYSCALE)
nRowSum = np.sum(nImage, axis = 1) #axis = 1 for row
y = np.argmax(nRowSum)

print(y)