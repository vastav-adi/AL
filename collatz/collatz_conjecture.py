import sys, random

n = int(random.uniform(2,999))
n_copy = n
ctr = 0

while n_copy!=1:
	if n_copy%2==0 :
		n_copy = n_copy/2

	elif n_copy%2!=0:
		n_copy = (n_copy*3)+1

	ctr += 1


print(n,ctr)