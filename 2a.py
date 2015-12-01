x=[0]*32

def f(y,z):
    return 108-(815-1500/z)/y
x[0]=4
x[1]=4.25
for i in range (2,31):
    x[i]=f(x[i-1],x[i-2])
print (x[30])
