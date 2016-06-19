import numpy
x = []
y = []
x.append(0.2)
y.append(0)
v_0 = 100
mu=0.027
g=9.8
a=mu*g
theta = numpy.arctan(0.3)
v_x=v_0*numpy.cos(theta)
v_y=v_0*numpy.sin(theta)
a_x=a*numpy.cos(theta)
a_y=a*numpy.sin(theta)
dt = 0.01
for i in range(int(10)):
	tmp1 = x[-1]+v_x*dt-0.5*a_x*(dt**2)
	tmp2 = y[-1]+v_y*dt-0.5*a_y*(dt**2)
	x.append(tmp1)
	y.append(tmp2)
	if abs(x[-1])>1:
		x.pop()
		y.pop()
		for r in range(int(100)):
			dt1=0.0001
			tmp1 = x[-1]+v_x*dt1-0.5*a_x*(dt1**2)
			tmp2 = y[-1]+v_y*dt1-0.5*a_y*(dt1**2)
			x.append(tmp1)
			y.append(tmp2)
			if abs(x[-1])>1:
				x.pop()
				y.pop()
				v_x=-v_x
				a_x=-a_x

	if abs(y[-1])>1:
		x.pop()
		y.pop()
		for r in range(int(100)):
			dt1=0.0001
			tmp1 = x[-1]+v_x*dt1-0.5*a_x*(dt1**2)
			tmp2 = y[-1]+v_y*dt1-0.5*a_y*(dt1**2)
			x.append(tmp1)
			y.append(tmp2)
			if abs(y[-1])>1:
				x.pop()
				y.pop()
				v_y=-v_y
				a_y=-a_y

from pylab import *
figure(figsize=(10,10),dpi=100)
title("square table with friction")
ylabel("y")
xlabel("x")
xlim(-1,1)
ylim(-1,1)
plot(x,y,c="blue")
show()