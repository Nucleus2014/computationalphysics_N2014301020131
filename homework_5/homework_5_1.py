N1 = []
t1 = []
dt = 0.01
N1.append(1000.0)
t1.append(0)
a = 10
for i in range(int(10/dt)):
	tmp1 = N1[i]+a * N1[i] * dt
	N1.append(tmp1)
	t1.append(dt*(i+1))
from pylab import *
figure(figsize=(10,8), dpi=100)
ylabel('the number of individuals in a population')
xlabel('time/s')
plot(t1,N1,color="blue", linestyle="-",linewidth=3.0,label="When b=0.01,N(0)=1000")
legend(loc='upper right')
show()
