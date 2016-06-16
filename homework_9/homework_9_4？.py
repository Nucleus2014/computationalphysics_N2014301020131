import math
import numpy
theta_p = []
F_D = numpy.linspace(1.35,1.5,301)
F_D_p = []
g = 9.8
l = 9.8
q = 0.5
Omega = (g/l)**0.5
Omega_D = 2./3
dt = 0.01
omega.append(0)
theta.append(0.2)
t.append(0)
for n in range(int(300)):
	omega = []
	theta = []
	t = []
	for i in range(int(3000)):
		tmp1 = omega[i]-g*math.sin(theta[i])*dt/l-q*omega[i]*dt+F_D[n]*math.sin(t[i]*Omega_D)*dt
		omega.append(tmp1)
		tmp2 = theta[i]+omega[i+1]*dt
		tmp3 = t[i]+dt
		while abs(tmp2)>math.pi:
			if tmp2>math.pi:
				tmp2=tmp2-2*math.pi
			else:
				tmp2=tmp2+2*math.pi
		theta.append(tmp2)
		for x in range(int(4)):
			if abs(t[i]-2*x*math.pi/Omega_D)<0.5*dt：
				theta_p.append(theta[i])
				F_D_p.append(F_D[n])
		t.append(tmp3)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('The nonlinear, forced pendulum')
ylabel('omega(radians/s)')
xlabel('theta(radians)')
xlim(-1.35,1.5)
ylim(1,3)
scatter(F_D_p,theta_p,c="blue")
show()