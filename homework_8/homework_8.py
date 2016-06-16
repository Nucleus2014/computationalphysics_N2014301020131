import math
omega = []
theta = []
t = []
g = 9.8
l = 9.8
F = 1.2
q = 0.5
Omega = (g/l)**0.5
Omega_D = 2/3
dt = 0.04
omega.append(0)
theta.append(0.2)
t.append(0)
for i in range(int(2*math.pi*100/Omega_D)):
	tmp1 = omega[i]-g*math.sin(theta[i])*dt/l-q*omega[i]*dt+F*math.sin(Omega_D*t[i])*dt
	omega.append(tmp1)
	tmp2 = theta[i]+omega[i+1]*dt
	tmp3 = t[i]+dt
	t.append(tmp3)
	if tmp2<math.pi:
		tmp2=tmp2+2*math.pi
	if tmp2>math.pi:
		tmp2=tmp2-2*math.pi
	theta.append(tmp2)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('The nonlinear, forced pendulum')
ylabel('omega(radians/s)')
xlabel('theta(radians)')
xlim(-4,4)
ylim(-2,1)
xticks([-4,-2,0,2,4])
yticks([-2,-1,0,1])
plot(theta,omega,color="blue",linestyle="-",linewidth=2.0,label="times in phase with the drive force")
legend(loc='upper right')
show()