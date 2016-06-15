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
theta_2 = []
omega_2 = []
t_2 = []
v_x_2 = []
v_y_2 = []
x2 = []
y2 = []
theta_2.append(0.01)
omega_2.append(0)
t_2.append(0)
v_x_2.append(0)
v_y_2.append(v_min)
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
delta = []
delta.append(0.01)
for i in range(int(100000)):
	tmp1 = abs(theta_1[i]-theta_2[i])
	delta.append(tmp1)


theta_3 = []
omega_3 = []
t_3 = []
v_x_3 = []
v_y_3 = []
x3 = []
y3 = []
theta_3.append(0)
omega_3.append(0)
t_3.append(0)
v_x_3.append(0)
v_y_3.append(1.0)
x3.append(5.0)
y3.append(0)
for i in range(int(100000)):
	tmp1 = omega_3[i]-dt*3*12*math.pi*(x3[i]*math.sin(theta_3[i])-y3[i]*math.cos(theta_3[i]))*(x3[i]*math.cos(theta_3[i])+y3[i]*math.sin(theta_3[i]))/((x3[i]**2+y3[i]**2)**0.5**5)
	omega_3.append(tmp1)
	tmp2 = theta_3[i]+omega_3[i+1]*dt
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2 = tmp2 - 2*math.pi
		else:
			tmp2 = tmp2 + 2*math.pi
	theta_3.append(tmp2)
	tmp3 = v_x_3[i]-4*math.pi**2*x3[i]*dt/((x3[i]**2+y3[i]**2)**0.5**3)
	v_x_3.append(tmp3)
	tmp4 = x3[i]+v_x_3[i+1]*dt
	tmp5 = v_y_3[i]-4*math.pi**2*y3[i]*dt/((x3[i]**2+y3[i]**2)**0.5**3)
	v_y_3.append(tmp5)
	tmp6 = y3[i]+v_y_3[i+1]*dt
	x3.append(tmp4)
	y3.append(tmp6)
	tmp7 = t_3[i] + dt
	t_3.append(tmp7)
theta_4 = []
omega_4 = []
t_4 = []
v_x_4 = []
v_y_4 = []
x4 = []
y4 = []
theta_4.append(0.01)
omega_4.append(0)
t_4.append(0)
v_x_4.append(0)
v_y_4.append(5.0)
x4.append(1.0)
y4.append(0)
for i in range(int(100000)):
	tmp1 = omega_4[i]-dt*3*12*math.pi*(x4[i]*math.sin(theta_4[i])-y4[i]*math.cos(theta_4[i]))*(x4[i]*math.cos(theta_4[i])+y4[i]*math.sin(theta_4[i]))/((x4[i]**2+y4[i]**2)**0.5**5)
	omega_4.append(tmp1)
	tmp2 = theta_4[i]+omega_4[i+1]*dt
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2 = tmp2 - 2*math.pi
		else:
			tmp2 = tmp2 + 2*math.pi
	theta_4.append(tmp2)
	tmp3 = v_x_4[i]-4*math.pi**2*x4[i]*dt/((x4[i]**2+y4[i]**2)**0.5**3)
	v_x_4.append(tmp3)
	tmp4 = x4[i]+v_x_4[i+1]*dt
	tmp5 = v_y_4[i]-4*math.pi**2*y4[i]*dt/((x4[i]**2+y4[i]**2)**0.5**3)
	v_y_4.append(tmp5)
	tmp6 = y4[i]+v_y_4[i+1]*dt
	x4.append(tmp4)
	y4.append(tmp6)
	tmp7 = t_4[i] + dt
	t_4.append(tmp7)
delta_1 = []
delta_1.append(0.01)
for i in range(int(100000)):
	tmp1 = abs(theta_3[i]-theta_4[i])
	delta_1.append(tmp1)

from pylab import *
figure(figsize=(20,10),dpi=100)
title('Hyperion')
subplot(121)
title('Circular orbit')
xlim(0,10)
ylim(0.0001,0.02)
yticks([0.0001,0.001,0.01,0.02])
ylabel('$\delta \theta $')
xlabel('time')
scatter(t_1,delta,c='blue',s=0.1)
subplot(122)
title('Elliptical orbit')
xlim(0,10)
ylim(0.0001,5,8)
yticks([0.0001,0.001,0.01,0.1,1,5,8])
ylabel('$\delta \theta $')
xlabel('time')
plot(t_1,delta_1,c='blue')
show()