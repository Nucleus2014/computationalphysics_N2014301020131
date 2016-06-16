import numpy
V_0 = [[0 for col in range(21)] for row in range(21)]
for x in range(20):
	V_0[1][x]=0
for i in range(1,20):
	V_0[i][0] = 0
	V_0[i][1] = 0.14
	V_0[i][2] = 0.28
	V_0[i][3] = 0.42
	V_0[i][4] = 0.7
	V_0[i][5] = 0.84
	V_0[i][6] = 0.98
	V_0[i][7] = 1.0
	V_0[i][8] = 0.67
	V_0[i][9] = 0.33
	V_0[i][10] = 0
	V_0[i][11] = -0.33
	V_0[i][12] = -0.67
	V_0[i][13] = -1
	V_0[i][14] = -0.86
	V_0[i][15] = -0.72
	V_0[i][16] = -0.57
	V_0[i][17] = -0.43
	V_0[i][18] = -0.3
	V_0[i][19] = -0.16
	V_0[i][20] = 0
for i in range(20):
	V_0[20][i] = 0
Delta = 0
for i in range(1,20):
	for j in range(1,20):
		tmp1 = [[0 for col in range(21)] for row in range(21)]
		tmp1[i][j] = (V_0[i-1][j]+V_0[i+1][j]+V_0[i][j-1]+V_0[i][j+1])/4
		Delta = Delta+abs(V_0[i][j]-tmp1[i][j])
V_0=tmp1
print Delta
while Delta>0.02:
	for i in range(1,20):
		for j in range(1,20):
			tmp1 = [[0 for col in range(21)] for row in range(21)]
			tmp1[i][j] = (V_0[i-1][j]+V_0[i+1][j]+V_0[i][j-1]+V_0[i][j+1])/4
	Delta = 0
	for i in range(1,20):
		for j in range(1,20):
			Delta=Delta+abs(V_0[i][j]-tmp1[i][j])
	print Delta
	V_0=tmp1
a1 = [0]*21
a2 = [0.1]*21
a3 = [0.2]*21
a4 = [0.3]*21
a5 = [0.4]*21
a6 = [0.5]*21
a7 = [0.6]*21
a8 = [0.7]*21
a9 = [0.8]*21
a10 = [0.9]*21
a11 = [1.0]*21
from pylab import *
figure(figsize=(20,10),dpi=100)
title('Electric potential near two metal plates')
ylabel('y')
xlabel('x')
ylim(0,1.2)
xlim(0,1.2)
yticks([0,1])
xticks([0,1])
scatter(V_0[10],a1)
scatter(V_0[11],a2)
scatter(V_0[12],a3)
scatter(V_0[13],a4)
scatter(V_0[14],a5)
scatter(V_0[15],a6)
scatter(V_0[16],a7)
scatter(V_0[17],a8)
scatter(V_0[18],a9)
scatter(V_0[19],a10)
scatter(V_0[20],a11)
show()