from decimal import Decimal, getcontext

getcontext().prec = 4
S=Decimal(input())
x=Decimal(input())
y=Decimal(input())
p=0
p=Decimal(p)
d=0
d=Decimal(d)
p=S/12/y*(1+y/100)
d=p*y*12-S
print (d)
