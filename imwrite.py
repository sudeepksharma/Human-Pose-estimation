import cv2

img = cv2.imread('wolverine.jpg', 1)

print(img)
#status is only True if the image is saved successfully, we take any image
status = cv2.imwrite('wolverine_copy.jpg', img)

print("Image written to file-system : ",status)