# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

A1="      ###      "
A2="     #   #     "
A3="    #     #    "
A4="   #       #   "
A5="  #         #  "
A6=" #           # "
A7="#             #"
B1="#############  "
B2="#            # "
C1="  #############"
C2=" #             "
C3="#              "
E1="###############"
G1="#        ######"
G2="  ###########  "
I1="       #       "
J1="#      #       "
J2=" #    #        "
J3="  ####         "
K1="#           #  "
K2="#          #   "
K3="#         #    "
K4="#        #     "
K5="#       #      "
K6="########       "
M1="##           ##"
M2="# #         # #"
M3="#  #       #  #"
M4="#   #     #   #"
M5="#    #   #    #"
M6="#     # #     #"
M7="#      #      #"
N1="##            #"
N2="# #           #"
N3="#  #          #"
N4="#   #         #"
N5="#    #        #"
N6="#     #       #"
N7="#       #     #"
N8="#        #    #"
N9="#         #   #"
N10="#          #  #"
N11="#           # #"
N12="#            ##"
Q1="  ########### #"
S1="             # "
S2="              #"
V1="      # #      "
Z1="            #  "
Z2="           #   "
Z3="          #    "
Z4="         #     "
Z5="        #      "
Z6="      #        "
Z7="     #         "
Z8="    #          "
Z9="   #           "
Z10="  #            "
A=(A1,A2,A3,A4,A5,A6,A7,A7,A7,A7,A7,A7,A7,A7,A7)
B=(B1,B2,A7,A7,A7,A7,B2,B1,B2,A7,A7,A7,A7,B2,B1)
C=(C1,C2,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C2,C1)
D=(B1,B2,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,B2,B1)
E=(E1,C3,C3,C3,C3,C3,C3,E1,C3,C3,C3,C3,C3,C3,E1)
F=(E1,C3,C3,C3,C3,C3,C3,E1,C3,C3,C3,C3,C3,C3,C3)
G=(C1,C2,C3,C3,C3,C3,C3,C3,G1,A7,A7,A7,A7,A6,G2)
H=(A7,A7,A7,A7,A7,A7,A7,E1,A7,A7,A7,A7,A7,A7,A7)
I=(E1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,E1)
J=(E1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,J1,J2,J3)
K=(A7,B2,K1,K2,K3,K4,K5,K6,K5,K4,K3,K2,K1,B2,A7)
L=(C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,C3,E1)
M=(A7,M1,M2,M3,M4,M5,M6,M7,A7,A7,A7,A7,A7,A7,A7)
N=(A7,N1,N2,N3,N4,N5,N6,J1,N7,N8,N9,N10,N11,N12,A7)
O=(G2,A6,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A6,G2)
P=(B1,B2,A7,A7,A7,A7,B2,B1,C3,C3,C3,C3,C3,C3,C3)
Q=(G2,A6,A7,A7,A7,A7,A7,A7,A7,A7,N9,N10,N11,A6,Q1)
R=(G2,A6,A7,A7,A7,A7,B2,B1,K5,K4,K3,K2,K1,B2,A7)
S=(C1,C2,C3,C3,C3,C3,C2,G2,S1,S2,S2,S2,S2,S1,B1)
T=(E1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1,I1)
U=(A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A7,A6,G2)
V=(A7,A7,A7,A7,A7,A7,A7,A7,A6,A5,A4,A3,A2,V1,I1)
W=(A7,A7,A7,A7,A7,A7,A7,M7,M6,M5,M4,M3,M2,M1,A7)
X=(A7,A6,A5,A4,A3,A2,V1,I1,V1,A2,A3,A4,A5,A6,A7)
Y=(A7,A6,A5,A4,A3,A2,V1,I1,I1,I1,I1,I1,I1,I1,I1)
Z=(E1,S1,Z1,Z2,Z3,Z4,Z5,I1,Z6,Z7,Z8,Z9,Z10,C2,E1)
dict={0:A,1:B,2:C,3:D,4:E,5:F,6:G,7:H,8:I,9:J,10:K,11:L,12:M,13:N,14:O,15:P,16:Q,17:R,18:S,19:T,20:U,21:V,22:W,23:X,24:Y,25:Z}
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
new=[]
name=raw_input("please enter your first name:")
for q in range(0,15):
	print H[q],E[q],L[q],L[q],O[q]
nameu=name.upper()
l1=len(nameu)
for i in range(0,l1):
	single=nameu[i]
	for x in alphabet:
		if single==x:
			new.append(dict[alphabet.index(x)])
l2=len(new)
print " "
print " "
for z in range(0,15):
	for y in range(0,l2):
		print new[y][z],
	print " "
choice=input("Do you want to reverse your name?(Y/N)")
for q in range(0,15):
	print H[q],E[q],L[q],L[q],O[q]
if choice==Y:
	new.reverse()	
	print " "
	print " "
	for p in range(0,15):
		for r in range(0,l2):
			print new[r][p],
		print " "
elif choice==N:
	print " "
	print " "
	for z in range(0,15):
		for y in range(0,l2):
			print new[y][z],
		print " "