# No wind and having effect of backspin
import math
x = []
y = []
z = []
v_x = []
v_y = []
v_z = []
dt = 0.01
x.append(0)
y.append(1)
z.append(0)
theta = 35./180*3.14  # v_y,v_z initial speed are quite small
v_x.append(50 * math.cos(theta)*0.44704) # Initial speed is 50,80,110mph/60/60
v_y.append(50 * math.sin(theta)*0.44704)
v_z.append(0)
g = 10
v_d = 35
omega = 2*math.pi*33.33  # rad/s
S = 4.1*(10**(-4))  # S=S_0/m
for i in range(int(100/dt)):
	tmp1 = x[i] + v_x[i] * dt
	tmp2 = v_x[i] - (0.0039 + (1+math.exp((((v_x[i])**2+(v_y[i])**2+(v_z[i])**2)**0.5-v_d)*0.2))**(-1)*0.0058)*(((v_x[i])**2+(v_y[i])**2+(v_z[i])**2)**0.5)*v_x[i]*dt
	tmp3 = y[i] + v_y[i] * dt
	tmp4 = v_y[i] - g * dt
	tmp5 = z[i]+v_z[i]*dt
	tmp6 = v_z[i]-S*v_x[i]*omega*dt
	x.append(tmp1)
	v_x.append(tmp2)
	y.append(tmp3)
	v_y.append(tmp4)
	z.append(tmp5)
	v_z.append(tmp6)
x_2 = []
y_2 = []
z_2 = []
v_x_2 = []
v_y_2 = []
v_z_2 = []
x_2.append(0)
y_2.append(1)
z_2.append(0)
v_x_2.append(80 * math.cos(theta)*0.44704)
v_y_2.append(80 * math.sin(theta)*0.44704)
v_z_2.append(0)
for i in range(int(100/dt)):
	B = 0.0039 + (1+math.exp((((v_x_2[i])**2+(v_y_2[i])**2+(v_z_2[i])**2)**0.5-v_d)/5))**(-1)*0.0058
	tmp7 = x_2[i] + v_x_2[i] * dt
	tmp8 = v_x_2[i] - B*(((v_x_2[i])**2+(v_y_2[i])**2+(v_z_2[i])**2)**0.5)*v_x_2[i]*dt
	tmp9 = y_2[i] + v_y_2[i] * dt
	tmp1_0 = v_y_2[i] - g * dt
	tmp1_1 = z_2[i]+v_z_2[i]*dt
	tmp1_2 = v_z_2[i]-S*v_x_2[i]*omega*dt
	x_2.append(tmp7)
	v_x_2.append(tmp8)
	y_2.append(tmp9)
	v_y_2.append(tmp1_0)
	z_2.append(tmp1_1)
	v_z_2.append(tmp1_2)
x_3 = []
y_3 = []
z_3 = []
v_x_3 = []
v_y_3 = []
v_z_3 = []
x_3.append(0)
y_3.append(1)
z_3.append(0)
v_x_3.append(110 * math.cos(theta)*0.44704)
v_y_3.append(110 * math.sin(theta)*0.44704)
v_z_3.append(0)
for i in range(int(100/dt)):
	B = 0.0039 + (1+math.exp((((v_x_3[i])**2+(v_y_3[i])**2+(v_z_3[i])**2)**0.5-v_d)/5))**(-1)*0.0058
	tmp1_3 = x_3[i] + v_x_3[i] * dt
	tmp1_4 = v_x_3[i] - B*(((v_x_3[i])**2+(v_y_3[i])**2+(v_z_3[i])**2)**0.5)*v_x_3[i]*dt
	tmp1_5 = y_3[i] + v_y_3[i] * dt
	tmp1_6 = v_y_3[i] - g * dt
	tmp1_7 = z_3[i]+v_z_3[i]*dt
	tmp1_8 = v_z_3[i]-S*v_x_3[i]*omega*dt
	x_3.append(tmp1_3)
	v_x_3.append(tmp1_4)
	y_3.append(tmp1_5)
	v_y_3.append(tmp1_6)
	z_3.append(tmp1_7)
	v_z_3.append(tmp1_8)
from pylab import *
figure(figsize=(12,10), dpi=100)
subplot(211)
ylabel('z(m)')
xlabel('x(m)')
title('Trajectory of a batted baseball')
xlim(0,150)
ylim(-50,50)
xticks([0,50,100,150])
yticks([-50,-40,-30,-20,-10,0,10,20,30,40,50])
plot(x,z,color="blue", linestyle="--",linewidth=2.0,label="v=50mph")
plot(x_2,z_2,color="green", linestyle="--",linewidth=2.0,label="v=80mph")
plot(x_3,z_3,color="red", linestyle="-",linewidth=2.0,label="v=110mph")
legend(loc='upper right')
subplot(212)
ylabel('y(m)')
xlabel('x(m)')
title('Trajectory of a batted baseball')
xlim(0,150)
ylim(0,50)
xticks([0,50,100,150])
yticks([0,10,20,30,40,50])
plot(x,y,color="blue", linestyle="--",linewidth=2.0,label="v=50mph")
plot(x_2,y_2,color="green", linestyle="--",linewidth=2.0,label="v=80mph")
plot(x_3,y_3,color="red", linestyle="-",linewidth=2.0,label="v=110mph")
legend(loc='upper right')
show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure(figsize=(12,10), dpi=100)
ax = fig.gca(projection='3d')
ax.set_xlim3d(0,150)
ax.set_ylim3d(-50,50)
ax.plot(x,y,z,label='v_0=50mph')
ax.plot(x_2,z_2,y_2,label='v_0=80mph')
ax.plot(x_3,z_3,y_3,label='v_0=110mph')
ax.legend()
plt.xlabel('x(m)')
plt.ylabel('z(m)')
plt.title('The effect of backspin')
plt.show()
