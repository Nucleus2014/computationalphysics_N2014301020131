import math
import matplotlib.pyplot as plt
import numpy as np
#########
y_af=[0]
y_nw=[0]
y_bf=[0]
x=[0]
#########
t=0
L=1.9
dx=0.01
c=250
dt=dx/(4*c)
r=c*dt/dx
M=L/dx
e=7.5*10**-6

for i in range(int(L/dx)):
    x.append(x[i]+dx)
    y_bf.append(math.sin((2*math.pi*(5+0.5)/1.9)*x[i]))
    y_nw.append(math.sin((2*math.pi*(5+0.5)/1.9)*x[i]))
    y_af.append(math.sin((2*math.pi*(5+0.5)/1.9)*x[i]))

for k in range(int(t/dt)):
    for i in range(int(L/dx)):
        l=int(L/dx)
        if i==0:
           y_af[i]=(2-2*r**2-6*e*r**2*M**2)*y_nw[i]-y_bf[i]+r**2*(1+4*e*M**2)*(y_nw[i+1]-y_nw[1])-e*r**2*M**2*(y_nw[i+2]-y_nw[2])
        if i==1:
           y_af[i]=(2-2*r**2-6*e*r**2*M**2)*y_nw[i]-y_bf[i]+r**2*(1+4*e*M**2)*(y_nw[i+1]+y_nw[i-1])-e*r**2*M**2*(y_nw[i+2]-y_nw[1])        
        if i==l-1:
           y_af[i]=(2-2*r**2-6*e*r**2*M**2)*y_nw[i]-y_bf[i]+r**2*(1+4*e*M**2)*(y_nw[i+1]+y_nw[i-1])-e*r**2*M**2*(-y_nw[l-1]+y_nw[i-2])
        if i==l:
           y_af[i]=(2-2*r**2-6*e*r**2*M**2)*y_nw[i]-y_bf[i]+r**2*(1+4*e*M**2)*(-y_nw[l-1]+y_nw[i-1])-e*r**2*M**2*(-y_nw[l-2]+y_nw[i-2])
        if i==0:
           y_af[i]=0
        if i==l:
           y_af[i]=0
        if i>=2:
           if i<=l-2:        
              y_af[i]=(2-2*r**2-6*e*r**2*M**2)*y_nw[i]-y_bf[i]+r**2*(1+4*e*M**2)*(y_nw[i+1]+y_nw[i-1])-e*r**2*M**2*(y_nw[i+2]+y_nw[i-2])   
    for j in range(int(L/dx)):   
        y_nw[j]=y_af[j]
        y_bf[j]=y_nw[j]

########
plt.scatter(x,y_af,marker='+',color='b',label='t=0')
plt.title(u'$varepsilon=7.5*10^{-6}$',fontsize=14)
plt.xlabel(u'x/m',fontsize=14)
plt.ylabel(u'y/m',fontsize=14)
plt.legend(fontsize=12,loc='best')
plt.show()