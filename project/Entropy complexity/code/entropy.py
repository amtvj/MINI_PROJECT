import cv2
from Steerable import *
import pickle

#Sample program for showing the output of the program

image = cv2.imread("images.jpg")
lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

#taking the indivisual parameters...
lab_l = lab[:,:,0]
lab_a = lab[:,:,1]
lab_b = lab[:,:,2]

s = Steerable(5)
coeff_l = s.buildSCFpyr(lab_l)
coeff_a = s.buildSCFpyr(lab_a)
coeff_b = s.buildSCFpyr(lab_b)


for i in range(5):
    print("i = %d"%(i))
    print(coeff_l[i])
   

#After this similar done for the coeff_a and coeff_b
#how to bin the values ...??
