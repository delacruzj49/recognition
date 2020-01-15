import cv2
import sys
import glob
import numpy as np

# Get user supplied values
imagePath = sys.argv[0]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


#read every single frame and asign name file and run thru for loop
files = glob.glob (" ") # Insert path to directory with decomposed frames
for myFile in files:
    print(myFile)
    # Read the image
    image = cv2.imread (myFile)
    #turn the image Gray to read
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    #if no faces found print
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    #cv2.waitKey(0)  only for images not for frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))