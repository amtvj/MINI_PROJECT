import shutil
import os

source = './'
dest1 = '../'

files = os.listdir(source)
fp = open("filename.txt","r")
for line in fp.readlines():
	lline = line[:-1]
	for f in files:
		if(f.startswith(lline)):
			shutil.move(f,dest1)