
import cv2
import glob
import numpy as np

X_data = []
files = glob.glob ("C:/Users/DeLaCruz/Desktop/Ai/face-detection/P2E_S5_C1.1/*.jpg")
for myFile in files:
    print(myFile)
    image = cv2.imread (myFile)
    X_data.append (image)
print(files)
