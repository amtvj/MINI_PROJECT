import cv2
from Steerable import *

image = cv2.imread("images.png")
lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
#cv2.imshow("LAB",lab)

lab_l = lab[:,:,0]
lab_a = lab[:,:,1]
lab_b = lab[:,:,2]

s = Steerable(5)
coeff_l = s.buildSCFpyr(lab_l)
coeff_a = s.buildSCFpyr(lab_a)
coeff_b = s.buildSCFpyr(lab_b)


	
cv2.waitKey(0)