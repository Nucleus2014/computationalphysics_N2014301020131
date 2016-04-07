# exercise 1.1
t1 = []
v1 = []
s = []
dt = 0.1
g = 9.8
v1.append(0.0)
s.append(0.0)
t1.append(0)
end_time = 10
for i in range(int(end_time/dt)):
	tmp=v1[i] - g * dt
	sen=s[i] + tmp * dt
	v1.append(tmp)
	s.append(sen)
	t1.append(dt*(i+1))
# a must command
import matplotlib.pyplot as plt 
plt.ylabel('velocity of a freely falling object/m*s^-1')
plt.xlabel('time/s')
# [xmin, xmax, ymin, ymax]
plt.axis([0,11,-110,0])
plt.plot(t1,v1,'b-',linewidth=3.0,label="The velocity of a freely falling object")
plt.legend(loc='lower left')
t = 10
plt.plot([t, t], [-110, v1[-1]], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [v1[-1], ], 50, color='red')

plt.annotate(r'$v=-98m/s$',
             xy=(t, v1[-1]), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
import matplotlib.pyplot as plt 
plt.ylabel('position of a freely falling object/m')
plt.xlabel('time/s')
plt.plot(t1,s,'g-',linewidth=3.0,label="The position of a freely falling object")
plt.legend(loc='lower left')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
