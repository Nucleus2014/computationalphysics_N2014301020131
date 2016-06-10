import math
omega = []
theta = []
t = []
g = 9.8
l = 1.0
dt = 0.04
omega.append(0)
theta.append(1.5)
t.append(0)
for i in range(int(100/dt)):
	tmp1 = omega[i]-g*math.sin(theta[i])*dt/l
	omega.append(tmp1)
	tmp2 = theta[i]+omega[i+1]*dt
	tmp3 = t[i]+dt
	theta.append(tmp2)
	t.append(tmp3)
omega_1 = []
theta_1 = []
t_1 = []
omega_1.append(0)
theta_1.append(2.5)
t_1.append(0)
for i in range(int(100/dt)):
	tmp1 = omega_1[i]-g*math.sin(theta_1[i])*dt/l
	omega_1.append(tmp1)
	tmp2 = theta_1[i]+omega_1[i+1]*dt
	tmp3 = t_1[i]+dt
	theta_1.append(tmp2)
	t_1.append(tmp3)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('The nonlinear pendulum')
ylabel('theta(radians)')
xlabel('time(s)')
xlim(0,10)
ylim(-4,4)
xticks([0,2,4,6,8,10])
yticks([-4,-2,0,2,4])
plot(t,theta,color="blue",linestyle="-",linewidth=2.0,label="theta_0=1.5")
plot(t_1,theta_1,color="green",linestyle="--",linewidth=2.0,label="theta_0=2.5")
legend(loc='upper right')
show()