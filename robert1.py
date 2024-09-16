import sys
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import io

plt.rcParams['figure.figsize'] = [15, 10]
roberts_cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )
img = io.imread('Edge_Detection_in-_Python/image.jpg')
img1 = img.astype('float64')
gray_img = np.dot(img1[...,:3], [0.2989, 0.5870, 0.1140])
gray_img /= 255
vertical = ndimage.convolve( gray_img, roberts_cross_v )
horizontal = ndimage.convolve( gray_img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
plt.title('Original')
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
plt.title('Roberts' )
plt.imshow(edged_img, cmap=plt.get_cmap('gray'))
plt.show()
img = io.imread('Edge_Detection_in-_Python/gaussian_noice.jpg')
img1 = img.astype('float64')
gray_img = np.dot(img1[...,:3], [0.2989, 0.5870, 0.1140])
gray_img /= 255
vertical = ndimage.convolve( gray_img, roberts_cross_v )
horizontal = ndimage.convolve( gray_img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
plt.title('Gaussian_noise')
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
plt.title('Roberts' )
plt.imshow(edged_img, cmap=plt.get_cmap('gray'))
plt.show()
img = io.imread('Edge_Detection_in-_Python/pepper_noise.jpg')
img1 = img.astype('float64')
vertical = ndimage.convolve( img1, roberts_cross_v )
horizontal = ndimage.convolve( img1, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))


plt.title('Pepper_noise')
plt.imshow(img1, cmap=plt.get_cmap('gray'))
plt.show()
plt.title('Roberts')
plt.imshow(edged_img, cmap=plt.get_cmap('gray'))
plt.show()
