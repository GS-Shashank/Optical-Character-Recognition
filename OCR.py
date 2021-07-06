"""""""""""""""""""""""""""""""""""""""""""""
Project: Optical Character Recognition
Description: Character detector which extracts printed or handwritten text from
             an image or video.
By:- Shashank GS
(Project implemented during my internship period in The Sparks Foundation)
(Task 1 part 2)
"""""""""""""""""""""""""""""""""""""""""""""
#importing the required libraries
import cv2
import pytesseract
import numpy as np

#Reading the image from which the tex is to be extracted
img = cv2.imread('image2.jpg')

#converting the imput image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(bin)

s_Arr = np.ones((2, 1), np.uint8)
# It returns a new array of given shape and type, filled with ones
img = cv2.erode(gray, s_Arr, iterations=1)#It performs erosion on the image
img = cv2.dilate(img, s_Arr, iterations=1)
#It is used to detach two connected objects etc.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#Path of tesseract.exe 

char = pytesseract.image_to_string(img)
#tesseract extracts the text from input image and stores in char_output as a string
print("Text extracted from the image is:-")
print("----------------------------------------------------------\n")
print(char)#printing the output
print("----------------------------------------------------------")
#printing the text extracted from the image into the text file   
with open('output.txt', 'w') as f:
    f.write(char)