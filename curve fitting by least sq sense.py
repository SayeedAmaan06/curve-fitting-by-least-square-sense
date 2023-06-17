import numpy as np

#input of lists(values) a and b 
a = np.array([float(x) for x in input().split()])
b = np.array([float(x) for x in input().split()])
#input from user to choose the curve fitting equation
c = int(input("Choose the Equation \n 1. y = ax+b \n 2. y = ax^2+bx+c \n 3. y = ax^b \n enter the choice: "))

#adding the elements of lists a and b
sumx = sum(a)
sumy = sum(b)

if c==1:
    #squaring elements in list a and adding them
    sumsqx= sum(a**2)

    #multiplying elements of list a with list b and adding them
    sumxy = sum(a*b)

    #finding solution for equations with 2 variables
    eqcoeff = np.array([[sumx,len(a)],[sumsqx,sumx]])
    eqcon = np.array([sumy,sumxy])
    sol = np.linalg.solve(eqcoeff,eqcon)
    print(f"y = {sol[0]} x + {sol[1]}")

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

    #finding solution for equations with 3 variables
    eqcoeff = np.array([[sumsqx,sumx,len(a)],[sumcubex,sumsqx,sumx],[sumquadx,sumcubex,sumsqx]])
    eqcon = np.array([sumy,sumxy,sumsqxy])
    sol = np.linalg.solve(eqcoeff,eqcon)
    print(f"y = {sol[0]} x^2 + {sol[1]} x + {sol[2]}")
    

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

    #finding solution for equations with 2 variables
    eqcoeff = np.array([[sumX,len(a)],[sumsqX,sumX]])
    eqcon = np.array([sumY,sumXY])
    sol = np.linalg.solve(eqcoeff,eqcon)
    #printing the values in the form of y=ax^b
    print(f"The Equation is : \n y = {np.exp(sol[0])} x^{sol[1]}")
    