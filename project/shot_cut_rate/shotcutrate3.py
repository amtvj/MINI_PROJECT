#Not giving proper results for the intial frames of the trailer....


from matplotlib import pyplot as plt
import numpy as np 
import cv2
import math

#variable declaration...
nbins = 16
nframes = 100
nrows = 4
ncols = 4
diff  = np.array([0])
total_sum = 0

#video-capture for the video frame reading..
cap       =  cv2.VideoCapture("file.mkv")
ret,image =  cap.read()

#size and shape for the crop parts..
height ,width ,depth = image.shape
windowsize_r = height / nrows
windowsize_c = width / ncols

if(height % nrows == 0):
    nrows += 1
if(width % ncols == 0):
    ncols += 1


prev_r_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
prev_g_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
prev_b_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]

#calculate histogram of an image..
def r_histogram(image1):
    hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
    i = 0
    for r in range(0,height - windowsize_r, windowsize_r):
        j = 0
        for c in range(0,width - windowsize_c, windowsize_c):
            window = image1[r:r+windowsize_r,c:c+windowsize_c]
            temp_hist = cv2.calcHist([window],[0],None,[nbins],[0,256])
            for k in range(nbins):
                hist[i][j][k] = temp_hist[k]
            j+=1
        i += 1
    return hist

def g_histogram(image1):
    hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
    i = 0
    for r in range(0,height - windowsize_r, windowsize_r):
        j = 0
        for c in range(0,width - windowsize_c, windowsize_c):
            window = image1[r:r+windowsize_r,c:c+windowsize_c]
            temp_hist = cv2.calcHist([window],[0],None,[nbins],[0,256])
            for k in range(nbins):
                hist[i][j][k] = temp_hist[k]
            j+=1
        i += 1
    return hist

def b_histogram(image1):
    hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
    i = 0
    for r in range(0,height - windowsize_r, windowsize_r):
        j = 0
        for c in range(0,width - windowsize_c, windowsize_c):
            window = image1[r:r+windowsize_r,c:c+windowsize_c]
            temp_hist = cv2.calcHist([window],[0],None,[nbins],[0,256])
            for k in range(nbins):
                hist[i][j][k] = temp_hist[k]
            j+=1
        i += 1
    return hist


#taking the initial values..
prev_r_hist = r_histogram(image)
prev_g_hist = g_histogram(image)
prev_b_hist = b_histogram(image)

#starting frame reading from the video...
frame_count =  1
while(frame_count <= nframes):
    ret,image = cap.read()
    cv2.imwrite(str(frame_count)+".jpg",image)
    frame_count += 1
    r_hist = r_histogram(image)
    g_hist = g_histogram(image)
    b_hist = b_histogram(image)
    total_diff = 0

    for i in range(nrows):
        for j in range(ncols):
            for k in range(nbins):
                total_diff = total_diff + ((abs(r_hist[i][j][k]-prev_r_hist[i][j][k])*(abs(r_hist[i][j][k]-prev_r_hist[i][j][k])))/(abs(prev_r_hist[i][j][k])+1))
                total_diff = total_diff + ((abs(g_hist[i][j][k]-prev_g_hist[i][j][k])*(abs(g_hist[i][j][k]-prev_g_hist[i][j][k])))/(abs(prev_g_hist[i][j][k])+1))
                total_diff = total_diff + ((abs(b_hist[i][j][k]-prev_b_hist[i][j][k])*(abs(b_hist[i][j][k]-prev_b_hist[i][j][k])))/(abs(prev_b_hist[i][j][k])+1))

    for i in range(nrows):
        for j in range(ncols):
            for k in range(nbins):
                prev_r_hist[i][j][k] = r_hist[i][j][k]
                prev_g_hist[i][j][k] = g_hist[i][j][k]
                prev_b_hist[i][j][k] = b_hist[i][j][k]

    diff = np.append(diff,total_diff ** (0.5))
    total_sum = total_sum + total_diff ** (0.5)

#calculating the mean of the difference values..
mean = total_sum / nframes
print("Mean :"),
print(mean)

#calculating the boundaries..
is_boundary  = np.array([1])
for i in range(1,nframes):
    if(diff[i] > mean):
        print(i),

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()