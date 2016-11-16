import re
a = "0    ACCEDE00000.mp4	47.939117	0.540554	5	1.057049	0.100531	0	1	117	0.005686	5.41E+00	5.48E+00	5.03E+00	4.57E+00	4.00E+00	3.27E+00	2.37E+00	1.69E+00	1.46E+00	1.42E+00	1.41E+00	4.32E+15	0.431373	1.414934"
llist = re.split('\n|\s*',a)

fp = open("nbscene_arousal.txt","w")
fread = open("ACCEDEfeaturesArousal_TAC2015.txt","r")
fp.write("ACCEDEfeaturesArousal_TAC2015.txt\n");

i = 0
for line in fread.readlines():
	#print(line)
	if i == 0:
		i = i+1
	else:	
		i = i+1
		llist = re.split('	|\n|\s*',line)
		fp.write("%d %d\n" % ((int)(llist[0]),(int)(llist[8])))

fp.close()
fread.close()

fp = open("nbscene_valence.txt","w")
fread = open("ACCEDEfeaturesValence_TAC2015.txt","r")
fp.write("ACCEDEfeaturesValene_TAC2015.txt\n");

i = 0
for line in fread.readlines():
	#print(line)
	if i == 0:
		#llist = re.split('\n|\s*',line)
		i = i+1
	else:
		#continue
		#print(i),
		i = i+1
		llist = re.split('	|\n|\s*',line)
		fp.write("%d %d\n" % ((int)(llist[0]),(int)(llist[13])))

fp.close()
fread.close()

