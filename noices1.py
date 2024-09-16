from PIL import Image
im = Image.open(r"Edge_Detection_in-_Python/image.jpg")
im.show()
# Adding Gaussian Noise to image
# Import Image from wand.image module
from wand.image import Image
  
# Read image using Image() function
with Image(filename ="Edge_Detection_in-_Python/image.jpg") as img:
  
    # Generate noise image using spread() function
    img.noise("gaussian", attenuate = 0.9)
    img.save(filename ="Edge_Detection_in-_Python/gaussian_noice.jpg")
# Adding Pepper Noise to image
import random
import cv2
 
def add_noise(img):
 
    # Getting the dimensions of the image
    row , col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to white
        img[y_coord][x_coord] = 255
         
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to black
        img[y_coord][x_coord] = 0
         
    return img
 
img = cv2.imread('Edge_Detection_in-_Python/image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('Edge_Detection_in-_Python/pepper_noise.jpg',add_noise(img))