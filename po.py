# BIM A+3: Parametric Modelling in BIM
# Programming Assignement #3
# Han Sun

import math

n =int(input("Number of dots?"))
x =[]
y =[]

for i in range(n):
    xi=float(input(f"x[{i+1}]:"))
    yi=float(input(f"y[{i+1}]:"))
    x.append(xi)
    y.append(yi)

print()
print(f"{'x':>10} {'y':>10}")
print("-" * 30)
for i in range(n):
    print(i+1,":", f"{x[i]:>7} {y[i]:>10}")
print("-" * 30)

a=0
sx=0
sy=0
ix=0
iy=0
ixy=0
for i in range(0,n):
    a=a+(x[i]+x[i-1])*(y[i]-y[i-1])
    sx=sx+(x[i]-x[i-1])*(y[i]*y[i]+y[i-1]*y[i]+y[i-1]*y[i-1])
    sy=sy+(y[i]-y[i-1])*(x[i]*x[i]+x[i-1]*x[i]+x[i-1]*x[i-1])
    ix=ix+(x[i]-x[i-1])*(y[i]**3+y[i]**2*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    iy=iy+(y[i]-y[i-1])*(x[i]**3+x[i]**2*x[i-1]+x[i]*x[i-1]**2+x[i-1]**3)
    ixy=ixy+(y[i]-y[i-1])*(y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)+y[i-1]*(3*x[i-1]**2+2*x[i]*x[i-1]+x[i]**2))
Ax=1/2*a
Sx=-1/6*sx
Sy=1/6*sy
Ix=-1/12*ix
Iy=1/12*iy
Ixy=-1/24*ixy
XT=Sy/Ax
YT=Sx/Ax
IXT=Ix-YT**2*Ax
IYT=Iy-XT**2*Ax
IXYT=Ixy+XT*YT*Ax
print("Geometric Characteristics:")
print( )
print(f"Ax={Ax:.2f}")
print(f"Sx={Sx:.2f}")
print(f"Sy={Sy:.2f}")
print(f"Ix={Ix:.2f}")
print(f"Iy={Iy:.2f}")
print(f"Ixy={Ixy:.2f}")
print(f"XT={XT:.2f}")
print(f"YT={YT:.2f}")
print(f"IXT={IXT:.2f}")
print(f"IYT={IYT:.2f}")
print(f"IXYT={IXYT:.2f}")
print( )
print("Good Day!")