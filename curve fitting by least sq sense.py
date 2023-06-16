from sympy import symbols, Eq, solve
from operator import mul
import math

a = [float(x) for x in input().split()]
b = [float(x) for x in input().split()]
c = int(input("Choose the Equation \n 1. y = ax+b \n 2. y = ax^2+bx+c 3. y = ax^b\n enter the choice: "))

sumx = sum(a)
sumy = sum(b)
def soleq(a1,b1,c1,a2,b2,c2):
        x, y = symbols('x,y')
        eq1 = Eq(((a1*x)+(b1*y)), c1)
        print("Equation 1:")
        print(eq1)
        eq2 = Eq(((a2*x)+(b2*y)), c2)
        print("Equation 2")
        print(eq2)
        print("Values of 2 unknown variable are as follows:")
        sol = solve((eq1, eq2), (x, y))
        print(f"y = {sol[x]} x + {sol[y]}")
        s = [sol[x],sol[y]]
        return s
if c==1:
    sumsqx= sum(list(map(mul,a,a)))
    sumxy = sum(list(map(mul, a,b)))

    soleq(sumx,len(a),sumy,sumsqx,sumx,sumxy)
elif c==2:
    sqa = list(map(mul,a,a))
    sumsqx= sum(sqa)
    sumcubex= sum(list(map(mul,sqa,a)))
    sumquadx= sum(list(map(mul,sqa,sqa)))
    sumxy = sum(list(map(mul, a,b)))
    sumsqxy = sum(list(map(mul,sqa,b)))
    def solequ(a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3):
        x, y, z = symbols('x,y,z')
  
# defining equations
        eq1 = Eq(((a1*x)+(b1*y)+(c1*z)), d1)
        print("Equation 1:")
        print(eq1)
    
        eq2 =Eq(((a2*x)+(b2*y)+(c2*z)), d2)
        print("Equation 2")
        print(eq2)
  
        eq3 = Eq(((a3*x)+(b3*y)+(c3*z)), d3)
        print("Equation 3")
        print(eq3)

        print("Values of 3 unknown variable are as follows:")
        sol = solve((eq1, eq2, eq3), (x, y, z))
        print(f"y = {sol[x]} x^2 + {sol[y]} x + {sol[z]}")
    solequ(sumsqx,sumx,len(a),sumy,sumcubex,sumsqx,sumx,sumxy,sumquadx,sumcubex,sumsqx,sumsqxy)
elif c==3:
    logx = [math.log(i) for i in a]
    sumX = sum(logx)
    logy = [math.log(i) for i in b]
    sumY = sum(logy)
    sumsqX = sum(list(map(mul,logx,logx)))
    sumXY = sum(list(map(mul,logx,logy)))
    sol = soleq(sumX,len(a),sumY,sumsqX,sumX,sumXY)
    print(f"the equation is : \n y = {math.exp(sol[0])} x^{sol[1]}")
    