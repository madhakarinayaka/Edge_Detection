import cv2
import numpy as np
from matplotlib import pyplot as plt
#original image
img = cv2.imread('Edge_Detection_in-_Python/image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(img_sobel)
plt.title('Sobel')
plt.show()

#gaussian noise image
img = cv2.imread('Edge_Detection_in-_Python/gaussian_noice.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


plt.imshow(img)
plt.title('Gaussian Noice')
plt.show()
plt.imshow(img_sobel)
plt.title('Sobel')
plt.show()
#pepper noise image
img = cv2.imread('Edge_Detection_in-_Python/pepper_noise.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


plt.imshow(img)
plt.title('Pepper Noice')
plt.show()
plt.imshow(img_sobel)
plt.title('Sobel')
plt.show()
