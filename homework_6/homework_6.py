import math
x = []
y = []
v_x = []
v_y = []
dt = 1
x.append(0)
y.append(0)
theta = 35./180*3.14
v_x.append(0.7 * math.cos(theta))
v_y.append(0.7 * math.sin(theta))
g = 0.01
for i in range(int(100/dt)):
	tmp1 = x[i] + v_x[i] * dt
	tmp2 = v_x[i] - 4*(10**(-2))*(((v_x[i])*(v_x[i])+(v_y[i])*(v_y[i]))**0.5)*v_x[i]*dt
	tmp3 = y[i] + v_y[i] * dt
	tmp4 = v_y[i] - g * dt - 4*(10**(-2))*(((v_x[i])*(v_x[i])+(v_y[i])*(v_y[i]))**0.5)*v_y[i]*dt
	x.append(tmp1)
	v_x.append(tmp2)
	y.append(tmp3)
	v_y.append(tmp4)
x_2 = []
y_2 = []
v_x_2 = []
v_y_2 = []
x_2.append(0)
y_2.append(0)
theta_2 = 45./180*3.14
v_x_2.append(0.7 * math.cos(theta_2))
v_y_2.append(0.7 * math.sin(theta_2))
for i in range(int(100/dt)):
	tmp5 = x_2[i] + v_x_2[i] * dt
	tmp6 = v_x_2[i] - 4*(10**(-2))*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_x_2[i]*dt
	tmp7 = y_2[i] + v_y_2[i] * dt
	tmp8 = v_y_2[i] - g * dt - 4*(10**(-2))*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_y_2[i]*dt
	x_2.append(tmp5)
	v_x_2.append(tmp6)
	y_2.append(tmp7)
	v_y_2.append(tmp8)
x_3 = []
y_3 = []
v_x_3 = []
v_y_3 = []
a = 6.5
x_3.append(0)
y_3.append(0)
v_x_3.append(0.7 * math.cos(theta))
v_y_3.append(0.7 * math.sin(theta))
for i in range(int(100/dt)):
	tmp9 = x_3[i] + v_x_3[i] * dt
	tmp1_0 = v_x_3[i] - 4*(10**(-2))*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_x_3[i]*dt*((1-a*y_3[i]/288)**2.5)
	tmp1_1 = y_3[i] + v_y_3[i] * dt
	tmp1_2 = v_y_3[i] - g * dt - 4*(10**(-2))*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_y_3[i]*dt*((1-a*y_3[i]/288)**2.5)
	x_3.append(tmp9)
	v_x_3.append(tmp1_0)
	y_3.append(tmp1_1)
	v_y_3.append(tmp1_2)
x_4 = []
y_4 = []
v_x_4 = []
v_y_4 = []
x_4.append(0)
y_4.append(0)
v_x_4.append(0.7 * math.cos(theta_2))
v_y_4.append(0.7 * math.sin(theta_2))
for i in range(int(100/dt)):
	tmp1_3 = x_4[i] + v_x_4[i] * dt
	tmp1_4 = v_x_4[i] - 4*(10**(-2))*(((v_x_4[i])*(v_x_4[i])+(v_y_4[i])*(v_y_4[i]))**0.5)*v_x_4[i]*dt*((1-a*y_4[i]/288)**2.5)
	tmp1_5 = y_4[i] + v_y_4[i] * dt
	tmp1_6 = v_y_4[i] - g * dt - 4*(10**(-2))*(((v_x_4[i])*(v_x_4[i])+(v_y_4[i])*(v_y_4[i]))**0.5)*v_y_4[i]*dt*((1-a*y_4[i]/288)**2.5)
	x_4.append(tmp1_3)
	v_x_4.append(tmp1_4)
	y_4.append(tmp1_5)
	v_y_4.append(tmp1_6)
from pylab import *
figure(figsize=(12,10), dpi=100)
ylabel('y(km)')
xlabel('x(km)')
title('Cannon shell trajectory')
xlim(0,30)
ylim(0,10)
xticks([0,10,20,30])
yticks([0,2,4,6,8])
plot(x,y,color="blue", linestyle="--",linewidth=2.0,label="Without density correction(35)")
plot(x_2,y_2,color="green", linestyle="--",linewidth=2.0,label="Without density correction(40)")
plot(x_3,y_3,color="blue", linestyle="-",linewidth=2.0,label="With density correction(35)")
plot(x_4,y_4,color="green", linestyle="-",linewidth=2.0,label="With density correction(40)")
legend(loc='upper right')
show()
