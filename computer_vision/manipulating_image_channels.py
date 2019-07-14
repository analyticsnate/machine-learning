import cv2
import numpy as np

image = cv2.imread('cool-image.jpg').astype(np.float32) / 255
print('Shape:', image.shape)
cv2.imshow('original', image)
cv2.waitKey()
cv2.destroyAllWindows()

image[:, :, [0, 2]] = image[:, :, [2, 0]]
cv2.imshow('blue_and_red_swapped', image)
cv2.waitKey()
cv2.destroyAllWindows()

image[:, :, [0, 2]] = image[:, :, [2, 0]]
image[:, :, 0] = (image[:, :, 0] * 0.2).clip(0, 1)
image[:, :, 1] = (image[:, :, 1] * 1.5).clip(0, 1)
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()