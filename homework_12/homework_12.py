import math
theta_1 = []
omega_1 = []
t_1 = []
v_x_1 = []
v_y_1 = []
x1 = []
y1 = []
theta_1.append(0)
omega_1.append(0)
t_1.append(0)
v_x_1.append(0)
e=0
v_min = 2* math.pi * ((1-e)/((1+e)))**0.5
v_y_1.append(v_min)
dt = 0.0001
x1.append(1.0)
y1.append(0)
for i in range(int(100000)):
	tmp1 = omega_1[i]-dt*3*12*math.pi*(x1[i]*math.sin(theta_1[i])-y1[i]*math.cos(theta_1[i]))*(x1[i]*math.cos(theta_1[i])+y1[i]*math.sin(theta_1[i]))/((x1[i]**2+y1[i]**2)**0.5**5)
	omega_1.append(tmp1)
	tmp2 = theta_1[i]+omega_1[i+1]*dt
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2 = tmp2 - 2*math.pi
		else:
			tmp2 = tmp2 + 2*math.pi
	theta_1.append(tmp2)
	tmp3 = v_x_1[i]-4*math.pi**2*x1[i]*dt/((x1[i]**2+y1[i]**2)**0.5**3)
	v_x_1.append(tmp3)
	tmp4 = x1[i]+v_x_1[i+1]*dt
	tmp5 = v_y_1[i]-4*math.pi**2*y1[i]*dt/((x1[i]**2+y1[i]**2)**0.5**3)
	v_y_1.append(tmp5)
	tmp6 = y1[i]+v_y_1[i+1]*dt
	x1.append(tmp4)
	y1.append(tmp6)
	tmp7 = t_1[i] + dt
	t_1.append(tmp7)
print len(t_1)
print len(theta_1)
theta_2 = []
omega_2 = []
t_2 = []
v_x_2 = []
v_y_2 = []
x2 = []
y2 = []
theta_2.append(0)
omega_2.append(0)
t_2.append(0)
v_x_2.append(0)
v_y_2.append(1.0)
x2.append(1.0)
y2.append(0)
for i in range(int(100000)):
	tmp1 = omega_2[i]-dt*3*12*math.pi*(x2[i]*math.sin(theta_2[i])-y2[i]*math.cos(theta_2[i]))*(x2[i]*math.cos(theta_2[i])+y2[i]*math.sin(theta_2[i]))/((x2[i]**2+y2[i]**2)**0.5**5)
	omega_2.append(tmp1)
	tmp2 = theta_2[i]+omega_2[i+1]*dt
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2 = tmp2 - 2*math.pi
		else:
			tmp2 = tmp2 + 2*math.pi
	theta_2.append(tmp2)
	tmp3 = v_x_2[i]-4*math.pi**2*x2[i]*dt/((x2[i]**2+y2[i]**2)**0.5**3)
	v_x_2.append(tmp3)
	tmp4 = x2[i]+v_x_2[i+1]*dt
	tmp5 = v_y_2[i]-4*math.pi**2*y2[i]*dt/((x2[i]**2+y2[i]**2)**0.5**3)
	v_y_2.append(tmp5)
	tmp6 = y2[i]+v_y_2[i+1]*dt
	x2.append(tmp4)
	y2.append(tmp6)
	tmp7 = t_2[i] + dt
	t_2.append(tmp7)
from pylab import *
figure(figsize=(10,10),dpi=100)
title('Hyperion')
subplot(221)
title('Circular orbit')
xlim(0,8)
ylim(-4,4)
ylabel('$\theta $')
xlabel('time')
plot(t_1,theta_1,c='blue')
subplot(222)
title('Circular orbit')
xlim(0,8)
ylim(0,15)
ylabel('$\omega $')
xlabel('time')
plot(t_1,omega_1,c='blue')
subplot(223)
xlim(0,10)
ylim(-4,4)
ylabel('$\theta $')
xlabel('time')
plot(t_2,theta_2,c='blue')
subplot(224)
xlim(0,10)
ylim(-20,60)
ylabel('$\omega $')
xlabel('time')
plot(t_2,omega_2,c='blue',label='Elliptical orbit')#e=0.95
legend(loc='upper right')
show()