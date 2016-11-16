import numpy as np 
import cv2
import math

#variable declaration...
curve_div = 50
nbins = 16
frame_count = 1000
window = 8
tune_parameter = 2
#changed nrows and ncols to 5
nrows = 4
ncols = 4
diff  = np.array([0])
total_sum = 0

#prev_r_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
#prev_g_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
#prev_b_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]


#calculate histogram of an image..
def r_histogram(image1,windowsize_r,windowsize_c,nrows,ncols,height,width):
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

def g_histogram(image1,windowsize_r,windowsize_c,nrows,ncols,height,width):
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

def b_histogram(image1,windowsize_r,windowsize_c,nrows,ncols,height,width):
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

videoname = np.array(["000"])

fp = open("shot_cut_rate.txt","w")

for videocount in range(3,4):
    #video-capture for the video frame reading..
    videoname = ("ACCEDE%05i.mp4" % videocount)
    cap       =  cv2.VideoCapture(videoname)
    ret,image =  cap.read()

    #size and shape for the crop parts..
    height ,width ,depth = image.shape
    windowsize_r = height / nrows
    windowsize_c = width / ncols

    if(height % nrows == 0):
        nrows += 1
    if(width % ncols == 0):
        ncols += 1

    diff = np.array([0])
    total_sum = 0


    prev_r_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
    prev_g_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]
    prev_b_hist = [[[0 for k in range(nbins)] for j in range(ncols)] for i in range(nrows)]


    #taking the initial values..
    prev_r_hist = r_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)
    prev_g_hist = g_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)
    prev_b_hist = b_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)

    #starting frame reading from the video...
    frame_count =  1
    while(1):
        ret,image = cap.read()
        if ret == True:
            #cv2.imwrite(str(frame_count)+".jpg",image)
            frame_count += 1
            r_hist = r_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)
            g_hist = g_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)
            b_hist = b_histogram(image,windowsize_r,windowsize_c,nrows,ncols,height,width)
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
        else:
            break

    #calculating the mean of the difference values..
    mean = total_sum / frame_count
    #print("Mean :"),
    #print(mean)

    #some backchodi done here....
    diff = np.append(diff,0)

    #making change in the comparing for the boundary or not function...
    #calculating the boundaries..
    is_boundary = np.array([1])
    for i in range(1,frame_count):
        threshold = 0
        for j in range(window):
	        if (i+j) < frame_count:
	            threshold = threshold + diff[i+j]
        threshold = (threshold / window)*tune_parameter

        if(i == frame_count-1):
	        if diff[i]>mean and diff[i] >= threshold and diff[i] >= 2*diff[i-1]:
	            is_boundary = np.append(is_boundary,[1])
	        else:
	            is_boundary = np.append(is_boundary,[0])
        if diff[i]>=mean and diff[i] >= threshold and diff[i] >= 2*diff[i-1] and diff[i] >= 2*diff[i+1]:
	        is_boundary = np.append(is_boundary,[1])
	        #print(i),
        else:
        	is_boundary = np.append(is_boundary,[0])

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


    #new code added at home to finalize the shot cut rate...
    #this is the new code for the left and right boundary to get the shotcutrate..
    #defining the left and right boundary...
    left_boundary  = np.array([0])
    right_boundary = np.array([0])
    shot_boundary_curve = np.array([0])
    left = 0
    right = frame_count-1

    number_shot_cuts = -1

    for i in range(1,frame_count):
        if is_boundary[i] == 1:
	        number_shot_cuts += 1
	        left = i
        left_boundary  = np.append(left_boundary,[left])
        right_boundary = np.append(right_boundary,[0])
        shot_boundary_curve = np.append(shot_boundary_curve,[0])

    for i in range(frame_count-1,-1,-1):
        right_boundary[i] = right
        if is_boundary[i] == 1:
      	  right = i
    shot_cut_rate_final = 0
    print("Number of scene cuts = "+str(number_shot_cuts))

    for i in range(frame_count):
        val = 100*(math.exp((1-(right_boundary[i]-left_boundary[i]))/curve_div))
        shot_cut_rate_final = shot_cut_rate_final + val
        shot_boundary_curve[i] = val
    #print("")
    #print("The Final Shot Cut Rate = %d" % (shot_cut_rate_final/(nframes-1)))
    fp.write("%s - %f\n" % (videoname,(shot_cut_rate_final/(frame_count-1))))
    
