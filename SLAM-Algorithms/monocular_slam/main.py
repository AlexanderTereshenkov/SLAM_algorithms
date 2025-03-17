import cv2 as cv

image = []

# Initialize the ORB detector with 5k keypoints
orb = cv.ORB_create(nfeatures=5000)
 
# Detect keypoints and compute descriptors
keypoints, descriptors = orb.detectAndCompute(image, None)

