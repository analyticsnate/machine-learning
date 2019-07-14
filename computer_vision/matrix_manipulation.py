import cv2
import numpy as np

# numpy.uint8 dtype means that each value
# is 8 bits of information, which 
# means integer values from 0-255 are allowed

# numpy.full() creates an array of a given shape
# and sets all values in that array to a given value
image = np.full((480, 640, 3), 255, np.uint8)
cv2.imshow('white', image)
cv2.waitKey()
cv2.destroyAllWindows()

image = np.full((480, 640, 3), (0, 0, 255), np.uint8)
cv2.imshow('red', image)
cv2.waitKey()
cv2.destroyAllWindows()

image.fill(0)
cv2.imshow('black', image)
cv2.waitKey()
cv2.destroyAllWindows()

# set 3 pixels equal to white
image[240, 160] = (255, 255, 255)
image[240, 320] = (255, 255, 255)
image[240, 480] = (255, 255, 255)
cv2.imshow('black with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()

# set the first channel of all pixels to 255, 
# in order to make the black pixels blue
# not sure I understand what's actually happening here
image[:, :, 0] = 255
cv2.imshow('blue with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()

# set pixels on a vertical line in the middle
# of the image to white

# image[:, 320, :] actually means—
# give all pixels along height and channels 
# that have index 320 along the width dimension
image[:, 320, :] = 255
cv2.imshow('blue with white line', image)
cv2.waitKey()
cv2.destroyAllWindows()

# set the second channel of all pixels in
# a certain region to 255
image[100:600, 100:200, 2] = 255
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()