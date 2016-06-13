import math
x = []
y = []
z = []
sigma = 10
b = 8./3
r = 163
x.append(1)
y.append(0)
z.append(0)
dt = 0.0001
t = []
t.append(0)
for i in range(int(500000)): # up to 10^6
	tmp1 = x[i]+sigma*(y[i]-x[i])*dt
	tmp2 = y[i]-x[i]*z[i]*dt+r*x[i]*dt-y[i]*dt
	tmp3 = z[i]+x[i]*y[i]*dt-b*z[i]*dt
	tmp4 = t[i]+dt
	x.append(tmp1)
	y.append(tmp2)
	z.append(tmp3)
	t.append(tmp4)
x_1 = []
y_1 = []
z_1 = []
x_1.append(1)
y_1.append(0)
z_1.append(0)
t_1 = []
t_1.append(0)
r_1 = 165
for i in range(int(500000)): # up to 10^6
	tmp1 = x_1[i]+sigma*(y_1[i]-x_1[i])*dt
	tmp2 = y_1[i]-x_1[i]*z_1[i]*dt+r_1*x_1[i]*dt-y_1[i]*dt
	tmp3 = z_1[i]+x_1[i]*y_1[i]*dt-b*z_1[i]*dt
	tmp4 = t_1[i]+dt
	x_1.append(tmp1)
	y_1.append(tmp2)
	z_1.append(tmp3)
	t_1.append(tmp4)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('Lorenz model')
subplot(211)
xlim(0,30)
ylim(0,400)
ylabel('z')
xlabel('time')
plot(t,z,c='blue',label='r=163')
legend(loc='upper right')
subplot(212)
xlim(0,30)
ylim(0,400)
ylabel('z')
xlabel('time')
plot(t_1,z_1,c='blue',label='r=165')
legend(loc='upper right')
show()