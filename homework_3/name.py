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
for i in range(0,15):
    print L[i],U[i]
