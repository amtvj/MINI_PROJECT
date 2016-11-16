import re

fread = open("nbscene.txt","r")
fp = open("nbscene1.txt","w")
for line in fread.readlines():
	llist = re.split('	|\n|\s*',line)
	fp.write("%d\n" % ((int)(llist[2])))

fp.close()
fread.close()
