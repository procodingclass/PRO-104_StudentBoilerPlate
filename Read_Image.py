import cv2
import numpy

img = cv2.imread("redhood.jpg")

#cv2.imshow("output", img)
cv2.waitKey(0)

blue, green, red = cv2.split(img)
print(blue)
print(green)
print(red)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)





cv2.waitKey(0)
