import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Edge_Detection_in-_Python/image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img,cv2.CV_64F)


plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(laplacian)
plt.title('Laplacian')
plt.show()

img = cv2.imread('Edge_Detection_in-_Python/gaussian_noice.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img,cv2.CV_64F)


plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(laplacian)
plt.title('Gaussian Noice')
plt.show()

img = cv2.imread('Edge_Detection_in-_Python/pepper_noise.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img,cv2.CV_64F)


plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(laplacian)
plt.title('Pepper Noise')
plt.show()
