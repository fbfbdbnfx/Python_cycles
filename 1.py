from math import sqrt

print('x y')

for x in range(-10, 7, 1):

	if x<0:
		y=-0.5*x-3
	elif x<=3:
		y=-sqrt(9-x^2)
	else:
		y=sqrt(9-(x-6)^2)
		print(x-6, (x-6)^2, 9-(x-6)^2,sqrt(9-(x-6)^2))
	#print(x, y)
