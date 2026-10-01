import math

N=int(input())

for i in range(1, N+1, 1):
	if str(i)==str((i**2)%(10**(len(str(i))))):
		print(i)
