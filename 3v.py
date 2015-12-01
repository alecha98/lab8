from decimal import Decimal, getcontext

getcontext().prec = 4
S=Decimal(input())
x=Decimal(input())
y=Decimal(input())
S0=S
p=0
p=Decimal(p)
p=S0/12/y*(1+y/100)
d=0
s=Decimal(d)
while S>0:
    if (S>S0/12/y):
        print(S,p,p-S0/12/y,S0/12/y,sep=' ')
        S=S-p

    else:
        print(S,S*(1+y/100),S*y/100,S,sep=' ')
        S=S-p
