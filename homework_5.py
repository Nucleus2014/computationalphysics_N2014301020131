N1 = []
t1 = []
N2 = []
dt = 0.01
N1.append(1.0)
N2.append(1.0)
t1.append(0)
a = 10
for i in range(int(10/dt)):
	tmp1 = N1[i]+a * N1[i] * dt
	N1.append(tmp1)
	tmp2 = N2[i]+(a*N2[i]-3*N2[i]*N2[i])*dt
	N2.append(tmp2)
	t1.append(dt*(i+1))
from pylab import *
figure(figsize=(10,8), dpi=100)
plt.xticks([0, 0.04, 0.1, 0.2, 0.3, 0.4, 0.5,0.6,0.7,0.8])
xlim(0,0.8)
ylim(0,10)
ylabel('the number of individuals in a population')
xlabel('time/s')
plot(t1,N1,color="blue", linestyle="-",linewidth=3.0,label="When b=0")
plot(t1,N2,color="red", linestyle="-",linewidth=3.0,label="When small N(0)")
legend(loc='upper right')
t1 = 0.04
plt.plot([t1, t1], [0, N1[4]], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t1, ], [N1[4], ], 50, color='blue')
plt.annotate(r'$1.2950361347$',
             xy=(t1, N1[4]), xycoords='data',
             xytext=(+1, +40), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$1.4641$',
             xy=(t1, N2[4]), xycoords='data',
             xytext=(+40, +1), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t1, t1],[0, N2[4]], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t1, ],[N2[4], ], 50, color='red')
show()

