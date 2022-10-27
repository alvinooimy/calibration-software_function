import cv2
import numpy as np

sVideo = "./image/hello.h264"

def Image_AVG(nd_Image1, nd_Image2):
    if np.all(nd_Image1 == 0):
        return nd_Image2
    elif  np.all(nd_Image2 == 0):
        return nd_Image1
    else:
        nd_Image1 = nd_Image1.astype('float64')
        nd_Image2 = nd_Image2.astype('float64')
        nd_avg = (nd_Image1+nd_Image2) / 2
        return nd_avg
    

if __name__ == "__main__":
    #sVideo = input('Please Input the Video fileName:')
    cap = cv2.VideoCapture(sVideo)
    fps = cap.get(cv2.CAP_PROP_FPS)
    nd_result = np.zeros(1)
    icnt = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('./image/Image_{:02d}.bmp'.format(icnt), frame)
            nd_result = Image_AVG(nd_result, frame)
        else: break
        icnt+=1
    cap.release()
    cv2.imwrite('./image/Image_result.bmp', nd_result)