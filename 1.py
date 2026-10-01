import math

print('x y')

for x in range(-10, 7, 1):

	if x<0:
		y=-0.5*x-3
	elif x<=3:
		y=-round((9-(x**2))**0.5, 2)
	else:
		y=(9-(x-6)**2)**0.5
	print(x, y)
