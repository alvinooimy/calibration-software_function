import numpy as np
import matplotlib.pyplot as plt
import cv2

sIamgePath = "./image/Image_result.bmp"

x = 0
y = 366
deltax = 1280
deltay = 20

nImage = cv2.imread(sIamgePath, cv2.IMREAD_GRAYSCALE)
nCrop_IMG = nImage[y:y+deltay, x:x+deltax]

nColmean = np.mean(nCrop_IMG, axis = 0) #axis = 0 for column
nImgColMean = nColmean.reshape(1, len(nColmean)) #reshape to 1d array

datay = nImgColMean[0]
datax = np.arange(0,len(datay))

plt.plot(datax, datay, "b-", label = "Raw Data")
plt.legend()
plt.show()