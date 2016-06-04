import math
x_4 = []
y_4 = []
v_x_4 = []
v_y_4 = []
dt = 1
x_4.append(0)
y_4.append(0)
theta = 40./180*3.14
v_x_4.append(0.7 * math.cos(theta))
v_y_4.append(0.7 * math.sin(theta))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp1_3 = x_4[i] + v_x_4[i] * dt
	tmp1_4 = v_x_4[i] - 4*(10**(-2))*(((v_x_4[i])*(v_x_4[i])+(v_y_4[i])*(v_y_4[i]))**0.5)*v_x_4[i]*dt*((1-a*y_4[i]/288)**2.5)
	tmp1_5 = y_4[i] + v_y_4[i] * dt
	tmp1_6 = v_y_4[i] - g * dt - 4*(10**(-2))*(((v_x_4[i])*(v_x_4[i])+(v_y_4[i])*(v_y_4[i]))**0.5)*v_y_4[i]*dt*((1-a*y_4[i]/288)**2.5)
	x_4.append(tmp1_3)
	v_x_4.append(tmp1_4)
	y_4.append(tmp1_5)
	v_y_4.append(tmp1_6)
x_3 = []
y_3 = []
v_x_3 = []
v_y_3 = []
dt = 1
x_3.append(0)
y_3.append(0)
theta_1 = 45./180*3.14
v_x_3.append(0.7 * math.cos(theta_1))
v_y_3.append(0.7 * math.sin(theta_1))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp1 = x_3[i] + v_x_3[i] * dt
	tmp2 = v_x_3[i] - 4*(10**(-2))*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_x_3[i]*dt*((1-a*y_3[i]/288)**2.5)
	tmp3 = y_3[i] + v_y_3[i] * dt
	tmp4 = v_y_3[i] - g * dt - 4*(10**(-2))*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_y_3[i]*dt*((1-a*y_3[i]/288)**2.5)
	x_3.append(tmp1)
	v_x_3.append(tmp2)
	y_3.append(tmp3)
	v_y_3.append(tmp4)
x_2 = []
y_2 = []
v_x_2 = []
v_y_2 = []
dt = 1
x_2.append(0)
y_2.append(0)
theta_3 = 50./180*3.14
v_x_2.append(0.7 * math.cos(theta_3))
v_y_2.append(0.7 * math.sin(theta_3))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp5 = x_2[i] + v_x_2[i] * dt
	tmp6 = v_x_2[i] - 4*(10**(-2))*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_x_2[i]*dt*((1-a*y_2[i]/288)**2.5)
	tmp7 = y_2[i] + v_y_2[i] * dt
	tmp8 = v_y_2[i] - g * dt - 4*(10**(-2))*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_y_2[i]*dt*((1-a*y_2[i]/288)**2.5)
	x_2.append(tmp5)
	v_x_2.append(tmp6)
	y_2.append(tmp7)
	v_y_2.append(tmp8)
x_1 = []
y_1 = []
v_x_1 = []
v_y_1 = []
dt = 1
x_1.append(0)
y_1.append(0)
theta_4 = 55./180*3.14
v_x_1.append(0.7 * math.cos(theta_4))
v_y_1.append(0.7 * math.sin(theta_4))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp9 = x_1[i] + v_x_1[i] * dt
	tmp1_0 = v_x_1[i] - 4*(10**(-2))*(((v_x_1[i])*(v_x_1[i])+(v_y_1[i])*(v_y_1[i]))**0.5)*v_x_1[i]*dt*((1-a*y_1[i]/288)**2.5)
	tmp1_1 = y_1[i] + v_y_1[i] * dt
	tmp1_2 = v_y_1[i] - g * dt - 4*(10**(-2))*(((v_x_1[i])*(v_x_1[i])+(v_y_1[i])*(v_y_1[i]))**0.5)*v_y_1[i]*dt*((1-a*y_1[i]/288)**2.5)
	x_1.append(tmp9)
	v_x_1.append(tmp1_0)
	y_1.append(tmp1_1)
	v_y_1.append(tmp1_2)
x_5 = []
y_5 = []
v_x_5 = []
v_y_5 = []
dt = 1
x_5.append(0)
y_5.append(0)
theta_5 = 60./180*3.14
v_x_5.append(0.7 * math.cos(theta_5))
v_y_5.append(0.7 * math.sin(theta_5))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp1_7 = x_5[i] + v_x_5[i] * dt
	tmp1_8 = v_x_5[i] - 4*(10**(-2))*(((v_x_5[i])*(v_x_5[i])+(v_y_5[i])*(v_y_5[i]))**0.5)*v_x_5[i]*dt*((1-a*y_5[i]/288)**2.5)
	tmp1_9 = y_5[i] + v_y_5[i] * dt
	tmp2_0 = v_y_5[i] - g * dt - 4*(10**(-2))*(((v_x_5[i])*(v_x_5[i])+(v_y_5[i])*(v_y_5[i]))**0.5)*v_y_5[i]*dt*((1-a*y_5[i]/288)**2.5)
	x_5.append(tmp1_7)
	v_x_5.append(tmp1_8)
	y_5.append(tmp1_9)
	v_y_5.append(tmp2_0)
x_6 = []
y_6 = []
v_x_6 = []
v_y_6 = []
dt = 1
x_6.append(0)
y_6.append(0)
theta_6 = 65./180*3.14
v_x_6.append(0.7 * math.cos(theta_6))
v_y_6.append(0.7 * math.sin(theta_6))
g = 0.01
a = 6.5
for i in range(int(100/dt)):
	tmp2_1 = x_6[i] + v_x_6[i] * dt
	tmp2_2 = v_x_6[i] - 4*(10**(-2))*(((v_x_6[i])*(v_x_6[i])+(v_y_6[i])*(v_y_6[i]))**0.5)*v_x_6[i]*dt*((1-a*y_6[i]/288)**2.5)
	tmp2_3 = y_6[i] + v_y_6[i] * dt
	tmp2_4 = v_y_6[i] - g * dt - 4*(10**(-2))*(((v_x_6[i])*(v_x_6[i])+(v_y_6[i])*(v_y_6[i]))**0.5)*v_y_6[i]*dt*((1-a*y_6[i]/288)**2.5)
	x_6.append(tmp2_1)
	v_x_6.append(tmp2_2)
	y_6.append(tmp2_3)
	v_y_6.append(tmp2_4)
from pylab import *
figure(figsize=(10,4), dpi=100)
ylabel('y(km)')
xlabel('x(km)')
title('Cannon shell trajectory')
xlim(0,30)
ylim(0,20)
xticks([0,10,20,30])
yticks([0,2,4,6,8,10,12,14])
plot(x_4,y_4,color="blue", linestyle="-",linewidth=2.0,label="40")
plot(x_3,y_3,color="green", linestyle="-",linewidth=2.0,label="41")
plot(x_2,y_2,color="red", linestyle="-",linewidth=2.0,label="42")
plot(x_1,y_1,color="yellow", linestyle="-",linewidth=2.0,label="43")
plot(x_5,y_5,color="purple", linestyle="-",linewidth=2.0,label="44")
plot(x_6,y_6,color="orange", linestyle="-",linewidth=2.0,label="45")
legend(loc='upper right')
show()
