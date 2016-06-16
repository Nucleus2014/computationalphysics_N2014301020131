import math
x = []
y = []
z = []
sigma = 10
b = 8./3
r = 25
x.append(1)
y.append(0)
z.append(0)
dt = 0.0001
x_p = []
y_p = []
z_p = []
for i in range(int(500000)): # up to 10^6
	if abs(x[i])<1000*dt:
		y_p.append(y[i])
		z_p.append(z[i])
	tmp1 = x[i]+sigma*(y[i]-x[i])*dt
	tmp2 = y[i]-x[i]*z[i]*dt+r*x[i]*dt-y[i]*dt
	tmp3 = z[i]+x[i]*y[i]*dt-b*z[i]*dt
	x.append(tmp1)
	y.append(tmp2)
	z.append(tmp3)
x_1 = []
y_1 = []
z_1 = []
x_1.append(1)
y_1.append(0)
z_1.append(0)
x_p_1 = []
y_p_1 = []
z_p_1 = []
for i in range(int(500000)): # up to 10^6
	if abs(y[i])<500*dt:
		x_p_1.append(x_1[i])
		z_p_1.append(z_1[i])
	tmp1 = x_1[i]+sigma*(y_1[i]-x_1[i])*dt
	tmp2 = y_1[i]-x_1[i]*z_1[i]*dt+r*x_1[i]*dt-y_1[i]*dt
	tmp3 = z_1[i]+x_1[i]*y_1[i]*dt-b*z_1[i]*dt
	x_1.append(tmp1)
	y_1.append(tmp2)
	z_1.append(tmp3)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('Lorenz model')
subplot(121)
xlim(-10,10)
ylim(-10,30)
ylabel('z')
xlabel('y')
plot(y_p,z_p,c='blue')
subplot(122)
xlim(-20,20)
ylim(0,40)
ylabel('z')
xlabel('x')
plot(x_p_1,z_p_1,c='blue')
show()