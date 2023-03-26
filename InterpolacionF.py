import numpy as np
import matplotlib.pyplot as plt
import statistics as stats

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

# 0x208N for numbers, +, -, =, (, ) (N goes from 0 to F)
# 0x209N for letters
def Extract(lst):
    return list(next(zip(*lst)))
def LagrangeEval (X,Pxi,Pxs,Fxs):
    val = X
    val2 = Pxi
    tempNum = [(val-y) for y in Pxs]
    tempDen = [(val2-y) for y in Pxs]
    return np.prod(tempNum)/np.prod(tempDen) * Fxs

def LagrangePlot(X,n,values,Pxs,Fxs):
    lValues=[]
    if n > values: n = values-1
    for i in range(n+1):
        temp = Pxs.copy()
        temp.pop(i)
        lValues.append(LagrangeEval(X,Pxs[i],temp[:n],Fxs[i]))
    return lValues

def difDiv(Px,Fx):
    result = [x/y for x,y in zip(Fx,Px)]
    return result
def difDivPlot(Pxs,Fxs,X,values,):
    vals = []
    cambiofx = []
    cambiopx = []
    cambiofx.append(Fxs)
    cambiopx.append(Pxs)
    result = 0
    vals.append(Fxs)
    for i in range(values):
        if(i<values-1):
            temp=[]
            temp2=[]
            for j in range(1,len(cambiofx[i])):
                temp.append(cambiofx[i][j]-cambiofx[i][j-1])
                if(j+i<len(Pxs)):
                    # print(Pxs[j+i],"-",Pxs[j-1]," i=",i," j = ",j)
                    if(len(cambiopx)>1):    
                        prod = Extract(cambiopx)
                        temp2.append((Pxs[j+i]-Pxs[j-1])*prod[-1])
                    else: temp2.append((Pxs[j+i]-Pxs[j-1]))
                   
            cambiofx.append(temp)
            cambiopx.append(temp2)
            vals.append(difDiv(cambiopx[-1], cambiofx[-1]))
    for i in range(values):
        if (i == 0):
            result+=vals[i][0]
        else:
            result+=vals[i][0]*(np.prod([X-y for y in Pxs[:i]]))
    return result
def fact(x):
    if x<1:
        return 1
    else: return x*fact(x-1)

def regresion(x,p):
    if(x<p):
        return 1
    else: return x * regresion(x-1, p)
    
def progresion(x,p):
    if(x>p):
        return 1
    else: return x * progresion(x+1, p)
    
def neville(Fxs,Pxs,values,X):
    cambioFx = []
    cambioPx = []
    cambioFx.append(Fxs)
    cambioPx.append(Pxs)
    for i in range(0,values):
        temp = []
        for j in range(1,values-i):
            # print(Pxs[j+i],"-",Pxs[j-1])
            val = (Pxs[j+i]-X)*cambioFx[i][j-1] - (Pxs[j-1]-X)*cambioFx[i][j]
            val2 = Pxs[j+i] - Pxs[j-1]
            # print(val/val2)
            temp.append(val/val2)
        if(len(temp)>0):
            cambioFx.append(temp)
    return cambioFx[-1][0]
            # num.append((Pxs[j+i]-X))
    
def evalu(xp,xn,cambiofx,N):
    h = stats.mean(np.diff(xn))
    fp = 0
    p = (xp - xn[len(xn)-1])/h

    ps = []
    for i in range(-1,N-1):
        if(i==-1): ps.append(1)
        else:
            # print("Reg: ",regresion(p+i,p))
            temp = regresion(p+i,p)/fact(i+1)
            ps.append(temp)
    # print(ps)
    temp = []
    for i in range(len(ps)):
        # print(cambiofx[i][-1],",",ps[i])
        # print("PSi: ",ps[i])
        fp+=cambiofx[i][-1] * ps[i]   
        temp.append(cambiofx[i][-1] * ps[i]   )
    return fp

def evalu2(xp,xn,cambiofx,N):
    h = stats.mean(np.diff(xn))
    fp = 0
    p = (xp - xn[0])/h
    ps = []
    for i in range(-1,N-1):
        if(i==-1): ps.append(1)
        else:
            # print("Reg: ",progresion(p-i,p))
            temp = progresion(p-i,p)/fact(i+1)
            ps.append(temp)
    
    temp = []
    for i in range(len(ps)):
        fp+=cambiofx[i][0] * ps[i]   
        # print("PSi: ",ps[i])
        temp.append(cambiofx[i][0] * ps[i]   )
    return fp

def Lagrange():
    values = int(input("Ingrese la cantidad de valores de Px: "))
    Pxs = []
    Fxs = []
    lagrangeValues = []
    
    for i in range(values):
        Pxs.append(float(input("Ingrese el valor de P_i: ")))
        Fxs.append(float(input("Ingrese el valor de F(xi): ")))
    while(True):
        print("Ingrese el grado del polinomio, puede ser ",(values-1)," como máximo: ",end="")
        n = int(input())
        X = float(input("Ingrese el valor de Px que desea obtener: "))
        
        lagrangeValues = LagrangePlot(X,n,values,Pxs,Fxs)
        
        # print("Lagrange val ",lagrangeValues)
        resultado = sum(lagrangeValues)
        print("El resultado es: ",resultado)
        Xs = np.linspace(min(Pxs),max(Pxs),len(Pxs)+10)
        Ys = []
        for i in Xs:
            Ys.append(sum(LagrangePlot(i,n,values,Pxs,Fxs)))
       
        plt.figure()
        plt.plot(Xs,Ys)
        plt.plot(X,resultado,'o')
        plt.title("Lagrange")
        plt.show()
        print("Desea ingresar otro número?\n",
              "Presione 0 para salir y 1 para continuar")
        if(int(input())==0):
            break

def DifDivididas():
    values = int(input("Ingrese la cantidad de valores de Px: "))
    Pxs = []
    Fxs = []
    result = 0
    
    for i in range(values):
        Pxs.append(float(input("Ingrese el valor de P_i: ")))
        Fxs.append(float(input("Ingrese el valor de F(xi): ")))
    while(True):
        X = float(input("Ingrese el valor de Px que desea obtener: "))
        
        result = difDivPlot(Pxs, Fxs, X, values)
        print("El resultado es: ",result)    
        Xs = np.linspace(min(Pxs),max(Pxs),len(Pxs)+10)
        Ys = []
        for i in Xs:
            Ys.append(difDivPlot(Pxs, Fxs, i, values))
       
        plt.figure()
        plt.plot(Xs,Ys)
        plt.plot(X,result,'o')
        plt.title("Diferencias Divididas")
        plt.show()
        print("Desea ingresar otro número?\n",
              "Presione 0 para salir y 1 para continuar")
        if(int(input())==0):
            break

def Neville():
    values = int(input("Ingrese la cantidad de valores de Px: "))
    Pxs = []
    Fxs = []
    result = 0
    
    for i in range(values):
        Pxs.append(float(input("Ingrese el valor de P_i: ")))
        Fxs.append(float(input("Ingrese el valor de F(xi): ")))
    while(True):
        X = float(input("Ingrese el valor de Px que desea obtener: "))
        result = neville(Fxs, Pxs, values, X)
        print("El valor es: ",result)
        
        Xs = np.linspace(min(Pxs),max(Pxs),len(Pxs)+10)
        Ys = []
        for i in Xs:
            Ys.append(neville(Fxs, Pxs, values, i))
       
        plt.figure()
        plt.plot(Xs,Ys)
        plt.plot(X,result,'o')
        plt.title("Neville")
        plt.show()
        print("Desea ingresar otro número?\n",
              "Presione 0 para salir y 1 para continuar")
        if(int(input())==0):
            break

def difProgresivas():
    
    print("Ingresa la cantidad de datos a ingresar")
    N = int(input())
    xn = []
    fx = []
    
    for i in range(N):
        print("Valor de Xn: ",end="")
        xn.append(float(input()))
        print("Valor de f(Xn): ",end="")
        fx.append(float(input()))
    
    
    #Generacion la tabla de diferencias
    cambiofx = []
    cambiofx.append(fx)
    for i in range(N):
        if(i<N-1):
            temp=[]
            for j in range(1,len(cambiofx[i])):
                temp.append(cambiofx[i][j]-cambiofx[i][j-1])
            cambiofx.append(temp)
    
    
    while(True):
        print("Ingrese el valor que desea obtener")
        xp = float(input())
        
        # print(ps)
        
        fp =evalu2(xp, xn, cambiofx,N)
        print("El resultado es: ",fp)
        
        
        x = np.linspace(min(xn),max(xn),len(xn)+10)
        y=[]
        for i in x:
            y.append(evalu2(i, xn, cambiofx,N))
        
        plt.figure()
        plt.plot(x,y)
        plt.plot(xp,fp,'o')
        plt.title("Diferencias Progresivas")
        plt.show()
        print("Desea ingresar otro número?\n",
              "Presione 0 para salir y 1 para continuar")
        if(int(input())==0):
            break

def difRegresivas():
    
    print("Ingresa la cantidad de datos a ingresar",end="")
    N = int(input())
    xn = []
    fx = []
    
    for i in range(N):
        print("Valor de Xn: ",end="")
        xn.append(float(input()))
        print("Valor de f(Xn): ",end="")
        fx.append(float(input()))
    
    
    #Generacion la tabla de diferencias
    cambiofx = []
    cambiofx.append(fx)
    for i in range(N):
        if(i<N-1):
            temp=[]
            for j in range(1,len(cambiofx[i])):
                temp.append(cambiofx[i][j]-cambiofx[i][j-1])
            cambiofx.append(temp)
    
    # print(cambiofx)
    while(True):
        print("Ingrese el valor que desea obtener")
        xp = float(input())
        
        # print(ps)
        
        fp =evalu(xp, xn, cambiofx,N)
        print("El resultado es: ",fp)
        
        
        x = np.linspace(min(xn),max(xn),len(xn)+10)
        y=[]
        for i in x:
            y.append(evalu(i, xn, cambiofx,N))
        
        plt.figure()
        plt.plot(x,y)
        plt.plot(xp,fp,'o')
        plt.title("Diferencias Regresivas")
        plt.show()
        print("Desea ingresar otro número?\n",
              "Presione 0 para salir y 1 para continuar")
        if(int(input())==0):
            break
def menu():
    while(True):
        print("Elija el método que desee usar:\n",
              "1: Lagrange\n",
              "2: Diferencias Divididas\n",
              "3: Interpolacion de Neville\n",
              "4: Diferencias Progresivas\n",
              "5: Diferencias Regresivas\n",
              "0: Salir")
        elec = int(input())
        if(elec==1):
            Lagrange()
        elif(elec==2):
            DifDivididas()
        elif(elec==3):
            Neville()
        elif(elec==4):
            difProgresivas()
        elif(elec==5):
            difRegresivas()
        elif(elec==0):
            break
        else:
            print("Opcion no valida, intente nuevamente")