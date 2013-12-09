from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
import pylab

x=[]
y={}
yn={}


def main():
	data={200: {'rec.sport.hockey': 92.01915770893483, 'sci.space': 88.51711929866885, 'comp.os.ms-windows.misc': 42.69252437282266, 'sci.med': 81.89139419979443, 'misc.forsale': 61.826557325668, 'sci.crypt': 95.46116984760542, 'rec.autos': 73.18282769939714, 'rec.sport.baseball': 85.00002843903403, 'rec.motorcycles': 62.14524111719644, 'comp.graphics': 70.03894236162532, 'sci.electronics': 51.087228668948754, 'talk.politics.guns': 60.555475706979294, 'talk.politics.misc': 82.6849338507601, 'alt.atheism': 67.85623494534701, 'talk.politics.mideast': 97.90084905985984, 'comp.windows.x': 76.56406899999105, 'comp.sys.ibm.pc.hardware': 71.59428319871692, 'soc.religion.christian': 97.40632931863668, 'talk.religion.misc': 54.8967273850801, 'comp.sys.mac.hardware': 78.54840324905814}, 300: {'rec.sport.hockey': 94.89255389829592, 'sci.space': 84.80071904231538, 'comp.os.ms-windows.misc': 44.61022832279964, 'sci.med': 87.43245006321615, 'misc.forsale': 60.5075681643586, 'sci.crypt': 96.7211944146193, 'rec.autos': 76.06661909201141, 'rec.sport.baseball': 83.59071114361866, 'rec.motorcycles': 78.50423441419468, 'comp.graphics': 81.09284840280615, 'sci.electronics': 57.89870748517207, 'talk.politics.guns': 73.11157194190423, 'talk.politics.misc': 82.8709844993733, 'alt.atheism': 78.81450487592812, 'talk.politics.mideast': 98.67539367818213, 'comp.windows.x': 90.63705929332188, 'comp.sys.ibm.pc.hardware': 72.4658472456243, 'soc.religion.christian': 98.53239405217242, 'talk.religion.misc': 50.140221801822804, 'comp.sys.mac.hardware': 58.37242330117715}, 400: {'rec.sport.hockey': 95.73407239287806, 'sci.space': 88.30921204427338, 'comp.os.ms-windows.misc': 49.78066459408733, 'sci.med': 88.69924012502022, 'misc.forsale': 61.69296438380634, 'sci.crypt': 96.61249623974597, 'rec.autos': 75.6131258229041, 'rec.sport.baseball': 88.86959264476766, 'rec.motorcycles': 78.97320814762558, 'comp.graphics': 78.26369859687824, 'sci.electronics': 61.84092375150044, 'talk.politics.guns': 73.836073254746, 'talk.politics.misc': 87.4233848768625, 'alt.atheism': 78.11928800414766, 'talk.politics.mideast': 96.87904539172675, 'comp.windows.x': 92.16653295855323, 'comp.sys.ibm.pc.hardware': 71.98673603063355, 'soc.religion.christian': 98.90076716212111, 'talk.religion.misc': 48.45065479491383, 'comp.sys.mac.hardware': 70.63510504856016}, 100: {'rec.sport.hockey': 88.16297577921746, 'sci.space': 74.43912356495613, 'comp.os.ms-windows.misc': 33.29574664748524, 'sci.med': 61.917939584567534, 'misc.forsale': 44.56033468522031, 'sci.crypt': 94.56310962152047, 'rec.autos': 48.49456514928285, 'rec.sport.baseball': 77.74909312921682, 'rec.motorcycles': 58.209995462111536, 'comp.graphics': 54.10091167005919, 'sci.electronics': 40.902802669028, 'talk.politics.guns': 54.78585044972741, 'talk.politics.misc': 74.8149660196548, 'alt.atheism': 67.38308276737007, 'talk.politics.mideast': 96.14772087555473, 'comp.windows.x': 69.49098780359029, 'comp.sys.ibm.pc.hardware': 60.54763407263847, 'soc.religion.christian': 96.19662061938787, 'talk.religion.misc': 43.24072031442621, 'comp.sys.mac.hardware': 60.38070762698808}}
	for category in categories:
		y[category]=[]
	for n in range(100,500,100):
		print('n=',n)
		x.append(n)
		for category in categories:
			y[category].append(data[n][category])
		

	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='-',color='red')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='lower right')
	t=pylab.title('Number of training documents vs accuracy')
	t=pylab.grid()
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
