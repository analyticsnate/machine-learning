import cv2
import numpy as np

image = cv2.imread('cool-image.jpg').astype(np.float32) / 255
print('Shape:', image.shape)
cv2.imshow('original', image)
cv2.waitKey()
cv2.destroyAllWindows()

gamma = 0.5
corrected_image = np.power(image, gamma)
cv2.imshow('corrected_image', corrected_image)
cv2.waitKey()
cv2.destroyAllWindows()