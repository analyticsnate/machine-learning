import cv2
import numpy as np

# numpy.savetxt() and numpy.loadtxt()
# are basic I/O functions for numpy

mat = np.random.rand(100, 100).astype(np.float32)
print('Shape:', mat.shape)
print('Data type:', mat.dtype)

np.savetxt('mat.csv', mat)

mat = np.loadtxt('mat.csv').astype(np.float32)
print('Shape:', mat.shape)
print('Data type:', mat.dtype)