import math
omega = []
theta = []
omega_p = []
theta_p = []
t = []
g = 9.8
l = 9.8
F = 1.2
q = 0.5
Omega = (g/l)**0.5
Omega_D = 0.7
dt = 0.04
omega.append(0)
theta.append(0.2)
t.append(0)
omega_p.append(0)
theta_p.append(0.2)
for i in range(int(50000)):
	tmp1 = omega[i]-g*math.sin(theta[i])*dt/l-q*omega[i]*dt+F*math.sin(t[i]*Omega_D)*dt
	omega.append(tmp1)
	tmp2 = theta[i]+omega[i+1]*dt
	tmp3 = t[i]+dt
	t.append(tmp3)
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2=tmp2-2*math.pi
		else:
			tmp2=tmp2+2*math.pi
	theta.append(tmp2)
for i in range(int(50000)):
	for n in range(int(1000)):
		if abs(t[i]-2*n*math.pi/Omega_D)<0.5*dt:
			omega_p.append(omega[i])
			theta_p.append(theta[i])
from pylab import *
figure(figsize=(12,10),dpi=100)
title('The nonlinear, forced pendulum')
ylabel('omega(radians/s)')
xlabel('theta(radians)')
xlim(-4,4)
ylim(-3,3)
xticks([-4,-2,0,2,4])
yticks([-3,-2,-1,0,1,2,3])
scatter(theta_p,omega_p,c="blue",label="Omega_D=0.7")
legend(loc="upper right")
show()