# import the necessary packages
from panorama import Stitcher

import imutils
import cv2
 

# load the two images 
imageA = cv2.imread('resultOf3.png')
imageB = cv2.imread('3.jpg')

#resize them 
imageA = imutils.resize(imageA)
imageB = imutils.resize(imageB)

 
# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
 
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)



