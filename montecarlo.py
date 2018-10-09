# Monte Carlo Simluations
import random
N=10000;
p=0;
for x in range(N):
	x1=random.random()       # generate random number between 0 and 1
	x2=random.random()
#	print x1 x2
	r=x1**2+x2**2
	if r<1.0:
		p=p+1
pi=4.0*float(p)/float(N)
print 'Pi is approximately equal',pi
	