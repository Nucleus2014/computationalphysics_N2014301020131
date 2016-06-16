# No wind and no effect of backspin
import math
x = []
y = []
v_x = []
v_y = []
dt = 0.01
x.append(0)
y.append(0)
theta = 35./180*3.14  # Assume that the initial angle is 35
v_x.append(50 * math.cos(theta)*0.44704) # Initial speed is 50,80,110mph/60/60
v_y.append(50 * math.sin(theta)*0.44704)
g = 10
v_d = 35
for i in range(int(100/dt)):
	tmp1 = x[i] + v_x[i] * dt
	tmp2 = v_x[i] - (0.0039 + (1+math.exp((((v_x[i])**2+(v_y[i])**2)**0.5-v_d)*0.2))**(-1)*0.0058)*(((v_x[i])**2+(v_y[i])**2)**0.5)*v_x[i]*dt
	tmp3 = y[i] + v_y[i] * dt
	tmp4 = v_y[i] - g * dt - (0.0039 + (1+math.exp((((v_x[i])**2+(v_y[i])**2)**0.5-v_d)*0.2))**(-1)*0.0058)*(((v_x[i])**2+(v_y[i])**2)**0.5)*v_y[i]*dt
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
v_x_2.append(80 * math.cos(theta)*0.44704)
v_y_2.append(80 * math.sin(theta)*0.44704)
for i in range(int(100/dt)):
	B = 0.0039 + (1+math.exp((((v_x_2[i])**2+(v_y_2[i])**2)**0.5-v_d)/5))**(-1)*0.0058
	tmp5 = x_2[i] + v_x_2[i] * dt
	tmp6 = v_x_2[i] - B*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_x_2[i]*dt
	tmp7 = y_2[i] + v_y_2[i] * dt
	tmp8 = v_y_2[i] - g * dt - B*(((v_x_2[i])*(v_x_2[i])+(v_y_2[i])*(v_y_2[i]))**0.5)*v_y_2[i]*dt
	x_2.append(tmp5)
	v_x_2.append(tmp6)
	y_2.append(tmp7)
	v_y_2.append(tmp8)
x_3 = []
y_3 = []
v_x_3 = []
v_y_3 = []
x_3.append(0)
y_3.append(0)
v_x_3.append(110 * math.cos(theta)*0.44704)
v_y_3.append(110 * math.sin(theta)*0.44704)
for i in range(int(100/dt)):
	B = 0.0039 + (1+math.exp((((v_x_3[i])**2+(v_y_3[i])**2)**0.5-v_d)/5))**(-1)*0.0058
	tmp9 = x_3[i] + v_x_3[i] * dt
	tmp1_0 = v_x_3[i] - B*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_x_3[i]*dt
	tmp1_1 = y_3[i] + v_y_3[i] * dt
	tmp1_2 = v_y_3[i] - g * dt - B*(((v_x_3[i])*(v_x_3[i])+(v_y_3[i])*(v_y_3[i]))**0.5)*v_y_3[i]*dt
	x_3.append(tmp9)
	v_x_3.append(tmp1_0)
	y_3.append(tmp1_1)
	v_y_3.append(tmp1_2)
from pylab import *
figure(figsize=(12,10), dpi=100)
ylabel('y(m)')
xlabel('x(m)')
title('Trajectory of a batted baseball')
xlim(0,150)
ylim(0,30)
xticks([0,50,100,150])
yticks([0,10,20,30])
plot(x,y,color="blue", linestyle="--",linewidth=2.0,label="v=50mph")
plot(x_2,y_2,color="green", linestyle="--",linewidth=2.0,label="v=80mph")
plot(x_3,y_3,color="red", linestyle="-",linewidth=2.0,label="v=110mph")
legend(loc='upper right')
show()