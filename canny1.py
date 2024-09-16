import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('Edge_Detection_in-_Python/image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img,100,200)


plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(img_canny)
plt.title('Canny')
plt.show()

img = cv2.imread('Edge_Detection_in-_Python/gaussian_noice.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img,100,200)


plt.imshow(img)
plt.title('Gaussian Noice')
plt.show()
plt.imshow(img_canny)
plt.title('Canny')
plt.show()


img = cv2.imread('Edge_Detection_in-_Python/pepper_noise.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img,100,200)


plt.imshow(img)
plt.title('Pepper Noice')
plt.show()
plt.imshow(img_canny)
plt.title('Canny')
plt.show()