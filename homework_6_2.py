import math
x_0 = 22 # the x position of the target
y_0 = 4 # the y position of the target
r_f = []
r_f.append(1)  # value the angle
r_l = []
r_l.append(89)
g = 0.01
a = 6.5
for p in range(30):
# the former angle to be scanned
	x = [] 
	y = []
	v_x = []
	v_y = []
	dt = 0.01     # min value of the position of target is 1m?
	x.append(0)
	y.append(0)
	theta = r_f[-1]*3.14/180 ####
	v_x.append(0.7 * math.cos(theta))
	v_y.append(0.7 * math.sin(theta))
	for i in range(int(1000/dt)): # i should be large enough for x[-1] should be almost x_0
		if x[-1]<=x_0:
			tmp1 = x[i] + v_x[i] * dt
			tmp2 = v_x[i] - 4*(10**(-2))*(((v_x[i])*(v_x[i])+(v_y[i])*(v_y[i]))**0.5)*v_x[i]*dt*((1-a*y[i]/288)**2.5)
			tmp3 = y[i] + v_y[i] * dt
			tmp4 = v_y[i] - g * dt - 4*(10**(-2))*(((v_x[i])*(v_x[i])+(v_y[i])*(v_y[i]))**0.5)*v_y[i]*dt*((1-a*y[i]/288)**2.5)
			x.append(tmp1)
			v_x.append(tmp2)
			y.append(tmp3)
			v_y.append(tmp4)
# the latter angle to be scanned
	x_1 = [] 
	y_1 = []
	v_x_1 = []
	v_y_1 = []
	x_1.append(0)
	y_1.append(0)
	theta_1 = r_l[-1]*3.14/180
	v_x_1.append(0.7 * math.cos(theta_1))
	v_y_1.append(0.7 * math.sin(theta_1))
	for i in range(int(1000/dt)):
		if x_1[-1]<=x_0:
			tmp5 = x_1[i] + v_x_1[i] * dt
			tmp6 = v_x_1[i] - 4*(10**(-2))*(((v_x_1[i])*(v_x_1[i])+(v_y_1[i])*(v_y_1[i]))**0.5)*v_x_1[i]*dt*((1-a*y_1[i]/288)**2.5)
			tmp7 = y_1[i] + v_y_1[i] * dt
			tmp8 = v_y_1[i] - g * dt - 4*(10**(-2))*(((v_x_1[i])*(v_x_1[i])+(v_y_1[i])*(v_y_1[i]))**0.5)*v_y_1[i]*dt*((1-a*y_1[i]/288)**2.5)
			x_1.append(tmp5)
			v_x_1.append(tmp6)
			y_1.append(tmp7)
			v_y_1.append(tmp8)
	if abs(y[-1]-y_0) < abs(y_1[-1]-y_0):
		r_l.append(0.5*(r_f[-1]+r_l[-1]))
		r_f.append(r_f[-1])
	if abs(y[-1]-y_0) > abs(y_1[-1]-y_0):
		r_l.append(r_l[-1])
		r_f.append(0.5*(r_f[-1]+r_l[-1]))
print abs(y[-1]-y_0)
from pylab import *
figure(figsize=(10,4), dpi=100)
ylabel('y(km)')
xlabel('x(km)')
title('Cannon shell trajectory')
xlim(0,30)
ylim(0,20)
xticks([0,10,20,30])
yticks([0,2,4,6,8,10,12,14])
plot(x_0,y_0,"ro")
plot(x,y,color="blue", linestyle="--",linewidth=2.0) #output y+y_1 is better
show()
