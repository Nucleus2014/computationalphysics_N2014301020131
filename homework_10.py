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
for i in range(int(500000)): # up to 10^6
	tmp1 = x[i]+sigma*(y[i]-x[i])*dt
	tmp2 = y[i]-x[i]*z[i]*dt+r*x[i]*dt-y[i]*dt
	tmp3 = z[i]+x[i]*y[i]*dt-b*z[i]*dt
	x.append(tmp1)
	y.append(tmp2)
	z.append(tmp3)
from pylab import *
figure(figsize=(15,10),dpi=100)
title('Lorenz model')
subplot(121)
ylabel('z')
xlabel('x')
xlim(-20,20)
ylim(0,50)
plot(x,z,c='blue')
subplot(122)
ylabel('z')
xlabel('y')
xlim(-30,30)
ylim(0,50)
plot(y,z,c='blue')
show()