from matplotlib import pyplot as plt
import numpy as np 
import cv2
import math

nlen = 2400
kaiser_mul = 0.06
curve_div = 100
window = 16
tune_parameter = 2
nbins = 16

nbins = 16

#calculate histogram of an image..
def r_histogram(image):
    hist = cv2.calcHist([image],[0],None,[nbins],[0,256])
    return hist
def g_histogram(image):
    hist = cv2.calcHist([image],[1],None,[nbins],[0,256])
    return hist
def b_histogram(image):
    hist = cv2.calcHist([image],[2],None,[nbins],[0,256])
    return hist


diff  = np.array([0])
total_sum = 0

cap = cv2.VideoCapture("dragonball.mp4")
ret,image = cap.read()

prev_r_hist = r_histogram(image)
prev_g_hist = g_histogram(image)
prev_b_hist = b_histogram(image)

#starting frame reading from the video...
frame_count = 1
while(frame_count<=2000):
    ret,image = cap.read()
    cv2.imwrite(str(frame_count)+".jpg",image)
    frame_count += 1
    r_hist = r_histogram(image)
    g_hist = g_histogram(image)
    b_hist = b_histogram(image)
    total_diff = 0
    
    for j in range(nbins):
        total_diff = total_diff + (abs(r_hist[j]-prev_r_hist[j])*(abs(r_hist[j]-prev_r_hist[j])))/(abs(prev_r_hist[j])+1)
    for j in range(nbins):
        total_diff = total_diff + (abs(g_hist[j]-prev_g_hist[j])*(abs(g_hist[j]-prev_g_hist[j])))/(abs(prev_g_hist[j])+1)
    for j in range(nbins):
        total_diff = total_diff + (abs(b_hist[j]-prev_b_hist[j])*(abs(b_hist[j]-prev_b_hist[j])))/(abs(prev_b_hist[j])+1)
    
    for j in range(nbins):
        prev_r_hist[j] = r_hist[j]
        prev_g_hist[j] = g_hist[j]
        prev_b_hist[j] = b_hist[j]

    diff = np.append(diff,total_diff ** (0.5))
    total_sum += total_diff ** (0.5)

mean = total_sum / 1000
print("Mean :"),
print(mean)

for i in range(1001):
    #print("%d %d "%(i,diff[i]))
    if(diff[i] > mean):
        print(i)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()