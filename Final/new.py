import numpy
x = []
y = []
x.append(0.51)
y.append(0)
v_0 = 1
theta = numpy.arctan(0.3)
v_x=v_0*numpy.cos(theta)
v_y=v_0*numpy.sin(theta)
dt = 0.01
for i in range(int(10000000)):
	tmp1 = x[-1]+v_x*dt
	tmp2 = y[-1]+v_y*dt
	x.append(tmp1)
	y.append(tmp2)
	if abs(x[-1])>1:
		x.pop()
		y.pop()
		for r in range(int(100)):
			dt1=0.0001
			tmp1 = x[-1]+v_x*dt1
			tmp2 = y[-1]+v_y*dt1
			x.append(tmp1)
			y.append(tmp2)
			if abs(x[-1])>1:
				x.pop()
				y.pop()
				v_x=-v_x

	if abs(y[-1])>1:
		x.pop()
		y.pop()
		for r in range(int(100)):
			dt1=0.0001
			tmp1 = x[-1]+v_x*dt1
			tmp2 = y[-1]+v_y*dt1
			x.append(tmp1)
			y.append(tmp2)
			if abs(y[-1])>1:
				x.pop()
				y.pop()
				v_y=-v_y

	if (x[-1]+0.01)**2+y[-1]**2<0.5**2:
		x.pop()
		y.pop()
		for r in range(int(100)):
			dt1=0.0001
			tmp1 = x[-1]+v_x*dt1
			tmp2 = y[-1]+v_y*dt1
			x.append(tmp1)
			y.append(tmp2)
			if (x[-1]+0.01)**2+y[-1]**2<0.5**2:
				x.pop()
				y.pop()
				n=numpy.array([x[-1]+0.01,y[-1]])
				v=numpy.array([v_x,v_y])
				vn=-(v.dot(n))*n
				vs=v+vn
				v=vs+vn
				v_x=v[0]
				v_y=v[1]
from pylab import *
figure(figsize=(10,10),dpi=100)
title("square table with interior wall")
ylabel("y")
xlabel("x")
xlim(-1,1)
ylim(-1,1)
plot(x,y,c="blue")
show()