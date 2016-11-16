from sklearn.cluster import KMeans
import numpy as np 
import re


fread = open("feature_vector.txt","r")
feature_list = np.array([[]])
target = open("cluster_ours.txt","w")

polyShape = []
with open('feature_vector_ours.txt') as f:
  for line in f:
    line = line.split() # to deal with blank 
    if line:            # lines (ie skip them)
        line = [float(i) for i in line]
        polyShape.append(line)

'''
n = 2
X = np.empty(shape=[0, n])

for i in range(5):
    for j  in range(2):
        X = np.append(X, [[i, j]], axis=0)

k = 0 


for line in fread.readlines():
	llist = re.split('	|\s*',line)
	temp = np.array([])
	len1 = len(llist)
	if k==0:
		k=1
		continue
	else:
		for i in range(len1):
			temp = np.append(temp,float(llist[i]))
		feature_list = np.append(feature_list,temp,axis=0)
'''
kmeans = KMeans(n_clusters = 6).fit(polyShape)

#for i in range(len(kmeans.labels_)):
#	print(kmeans)
#fp.write(kmeans)
for item in kmeans.labels_:
	target.write("%s\n" % (item))
#print(kmeans.labels_)
#print(kmeans.cluster_centers_)
#print(kmeans)



