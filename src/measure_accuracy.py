from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
from k_fold_accuracy import k_fold_accuracy
import pylab

def main():
	x=[]
	y={}
	print (categories)
	for category in categories:
		y[category]=[]
	for n in range(2,10):
		print('n=',n)
		x.append(n)
		yn=k_fold_accuracy(n)
		print(yn)
		for category in categories:
			y[category].append(yn[category])
		
		

	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='--')
	t=pylab.xlabel('Number of folds k')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='upper right')
	t=pylab.title('Number of folds k vs accuracy')
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
