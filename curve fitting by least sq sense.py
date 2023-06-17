from sympy import symbols, Eq, solve
import numpy as np

#input of lists(values) a and b 
a = np.array([float(x) for x in input().split()])
b = np.array([float(x) for x in input().split()])
#input from user to choose the curve fitting equation
c = int(input("Choose the Equation \n 1. y = ax+b \n 2. y = ax^2+bx+c \n 3. y = ax^b \n enter the choice: "))

#adding the elements of lists a and b
sumx = sum(a)
sumy = sum(b)

#function to find solution for equation with 2 variables
def soleq(a1,b1,c1,a2,b2,c2):
        x, y = symbols('x,y')
        #defining the equations
        eq1 = Eq(((a1*x)+(b1*y)), c1)
        print("Equation 1:")
        print(eq1)
        eq2 = Eq(((a2*x)+(b2*y)), c2)
        print("Equation 2")
        print(eq2)
        print("Values of 2 unknown variable are as follows:")
        sol = solve((eq1, eq2), (x, y))
        #printing the values in the form of y=mx+c
        print(f"y = {sol[x]} x + {sol[y]}")
        s = [float(sol[x]),sol[y]]
        return s

if c==1:
    #squaring elements in list a and adding them
    sumsqx= sum(a**2)

    #multiplying elements of list a with list b and adding them
    sumxy = sum(a*b)

    #using the function to get the desired solution
    soleq(sumx,len(a),sumy,sumsqx,sumx,sumxy)

elif c==2:
    #squaring elements in list a and adding them
    sumsqx= sum(a**2)

    #finding the sumation a^3 and a^4 
    sumcubex= sum(a**3)
    sumquadx= sum(a**4)

    #multiplying elements of list a with list b and adding them
    sumxy = sum(a*b)

    #multiplying elements of list sqa with list b and adding them
    sumsqxy = sum((a**2)*b)

    #function to find solution for equation with 3 variables
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
        #printing the values in the form of y=ax^2+bx+c
        print(f"y = {sol[x]} x^2 + {sol[y]} x + {sol[z]}")
    solequ(sumsqx,sumx,len(a),sumy,sumcubex,sumsqx,sumx,sumxy,sumquadx,sumcubex,sumsqx,sumsqxy)

elif c==3:
    #finding the logarithmic values of elements in list a and b
    logx = np.log(a)
    sumX = sum(logx)
    logy = np.log(b)
    sumY = sum(logy)

    #squaring elements in list logX and adding them
    sumsqX = sum(logx**2)

    #multiplying elements of list logX with list logY and adding them
    sumXY = sum(logx*logy)

    #using the funciton to get the desired solution
    sol = soleq(sumX,len(a),sumY,sumsqX,sumX,sumXY)

    #printing the values in the form of y=ax^b
    print(f"The Equation is : \n y = {np.exp(sol[0])} x^{sol[1]}")
    