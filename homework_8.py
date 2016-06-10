import math
omega = []
theta = []
t = []
g = 9.8
l = 1.0
F = 0.2
q = 0.5
Omega = (g/l)**0.5
Omega_D = 1.0
dt = 0.04
omega.append(0)
theta.append(0.2)
t.append(0)
for i in range(int(100/dt)):
	tmp1 = omega[i]-g*theta[i]*dt/l-q*omega[i]*dt+F*math.sin(Omega_D*t[i])*dt
	omega.append(tmp1)
	tmp2 = theta[i]+omega[i+1]*dt
	tmp3 = t[i]+dt
	theta.append(tmp2)
	t.append(tmp3)
omega_1 = []
theta_1 = []
t_1 = []
Omega_D = 2.0
omega_1.append(0)
theta_1.append(0.2)
t_1.append(0)
for i in range(int(100/dt)):
	tmp1 = omega_1[i]-g*theta_1[i]*dt/l-q*omega_1[i]*dt+F*math.sin(Omega_D*t_1[i])*dt
	omega_1.append(tmp1)
	tmp2 = theta_1[i]+omega_1[i+1]*dt
	tmp3 = t_1[i]+dt
	theta_1.append(tmp2)
	t_1.append(tmp3)
omega_2 = []
theta_2 = []
t_2 = []
Omega_D = (Omega**2-q**2*0.5)**0.5
omega_2.append(0)
theta_2.append(0.2)
t_2.append(0)
for i in range(int(100/dt)):
	tmp1 = omega_2[i]-g*theta_2[i]*dt/l-q*omega_2[i]*dt+F*math.sin(Omega_D*t_2[i])*dt
	omega_2.append(tmp1)
	tmp2 = theta_2[i]+omega_2[i+1]*dt
	tmp3 = t_2[i]+dt
	theta_2.append(tmp2)
	t_2.append(tmp3)
omega_3 = []
theta_3 = []
t_3 = []
Omega_D = 5.0
omega_3.append(0)
theta_3.append(0.2)
t_3.append(0)
for i in range(int(100/dt)):
	tmp1 = omega_3[i]-g*theta_3[i]*dt/l-q*omega_3[i]*dt+F*math.sin(Omega_D*t_3[i])*dt
	omega_3.append(tmp1)
	tmp2 = theta_3[i]+omega_3[i+1]*dt
	tmp3 = t_3[i]+dt
	theta_3.append(tmp2)
	t_3.append(tmp3)
from pylab import *
figure(figsize=(12,10),dpi=100)
title('The linear, forced pendulum')
subplot(221)
ylabel('theta(radians)')
xlabel('time(s)')
xlim(0,20)
ylim(-0.2,0.2)
xticks([0,5,10,15,20])
yticks([-0.2,-0.1,0,0.1,0.2])
plot(t,theta,color="blue",linestyle="-",linewidth=2.0,label="Omega_D=1.0")
legend(loc='upper right')
subplot(222)
ylabel('theta(radians)')
xlabel('time(s)')
xlim(0,20)
ylim(-0.2,0.2)
xticks([0,5,10,15,20])
yticks([-0.2,-0.1,0,0.1,0.2])
plot(t_1,theta_1,color="blue",linestyle="-",linewidth=2.0,label="Omega_D=2.0")
legend(loc='upper right')
subplot(223)
ylabel('theta(radians)')
xlabel('time(s)')
xlim(0,20)
ylim(-0.2,0.2)
xticks([0,5,10,15,20])
yticks([-0.2,-0.1,0,0.1,0.2])
plot(t_2,theta_2,color="blue",linestyle="-",linewidth=2.0,label="Omega_D=Resonant frequency")
legend(loc='upper right')
subplot(224)
ylabel('theta(radians)')
xlabel('time(s)')
xlim(0,20)
ylim(-0.2,0.2)
xticks([0,5,10,15,20])
yticks([-0.2,-0.1,0,0.1,0.2])
plot(t_3,theta_3,color="blue",linestyle="-",linewidth=2.0,label="Omega_D=5.0")
legend(loc='upper right')
show()