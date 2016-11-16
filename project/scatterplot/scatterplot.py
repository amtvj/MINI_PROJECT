import matplotlib.pyplot as plt 
fval = open("valence.txt","r")
faro = open("arousal.txt","r")

val_list = []
ar_list = []
for line in fval.readlines(): 
	num = float(line)
	val_list.append(num)

for line in faro.readlines(): 
	num = float(line)
	ar_list.append(num)

plt.scatter(val_list,ar_list,label="valence-arousal",color='k')
plt.xlabel('Valence')
plt.ylabel('Arousal')
plt.title('Scatter Plot')
plt.show()
#plt.savefig("Scatter.png")