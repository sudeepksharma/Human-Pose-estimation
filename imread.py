import cv2
#imread is an OpenCV function used to read an image from the file
img = cv2.imread('wolverine.jpg', 1)
# 0 denotes grayscale image and 1 denotes color image

print(img)

#cv2.cvtColor is an OpenCV function used to convert an image from one color space to anothe
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#cv2.imshow is an OpenCV function used to display an image in a window
cv2.imshow('color image', img)
cv2.imshow('Gray_image', img1)
cv2.imshow('RGB_image', img2)
cv2.imshow('HSV_image', img3)
cv2.imshow('LAB_image', img4)

#cv2.waitKey is an OpenCV function used to wait for a keyboard event
cv2.waitKey(0)
#cv2.destroyAllWindows is an OpenCV function used to destroy all the windows
cv2.destroyAllWindows()