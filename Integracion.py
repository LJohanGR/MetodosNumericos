import numpy as np
import matplotlib.pyplot as plt


def mensajeIntegracion():
    print("Seleccione el tipo de integración que desea utilizar")
    print("1: Trapecio simple")
    print("2: Trapecio compuesto")
    print("3: Regla de Simpson de 1/3 simple")
    print("4: Regla de Simpson de 1/3 compuesto")
    print("5: Regla de Simpson de 3/8 simple")
    print("6: Regla de Simpson de 3/8 compuesto")
    print("0: Salir")

def mensajeFunciones():
    print("1: 3𝑥^4 − 4𝑥^3 − 12𝑥^2 + 5")
    print("2: cos(x)")
    print("3: x ln(x)")
    print("4: 𝑒^(2𝑥) 𝑠𝑒𝑛(3x)")
    print("5: x/(x^2 + 4)")
    print("0: Menú anterior")


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

def LagrangeSimpson(X,Pxs,Fxs,n):
    # print("Lagrange val ",lagrangeValues)
    Xs = np.linspace(min(Pxs),max(Pxs),len(Pxs)+10)
    Ys = []
    for i in Xs:
        Ys.append(sum(LagrangePlot(i,n,len(Pxs),Pxs,Fxs)))
    
    plt.fill(Xs,Ys,alpha=0.2)
   


def funciones(func,x):
    if(func == 1):
        return 3*(x**4) - 4*(x**3) - 12*(x**2) + 5
    elif(func == 2):
        return np.cos(x)
    elif(func == 3):
        return x * np.log(x)
    elif(func == 4):
        return np.exp(2*x) * np.sin(3*x)
    elif(func == 5):
        return x/(x**2 + 4)

def mensajeIntervalos(opc):
    print("Ingrese intervalo a")
    a = float(input())
    print("Ingrese intervalo b")
    b = float(input())
    if(a>b):
        a,b = b,a
    if(opc == 2 or opc == 4 or opc == 6):
        print("Ingrese la cantidad de subintervalos")
        n = int(input())
        return a,b,n
    return a,b,0


def evaluar(opc,func,a,b,n):
    if(opc == 1):
        return ((b-a) * (( funciones(func, a)+funciones(func, b) )/2) )
    if(opc == 2):
        h = (b-a)/n
        a2 = a + h
        temp = 0
        for i in range(n):
            temp += ((a2-a) * (( funciones(func, a)+funciones(func, a2) )/2) )
            a,a2 = a2, a2+h
        return temp
    if(opc == 3):
        return (b-a)/6 * (funciones(func, a) + 4*(funciones(func, ((a+b)/2))) + funciones(func, b))
    if(opc == 4):
        h = (b-a)/(n)
        a2 = a + h
        temp = 0
        for i in range(n):
            temp += (a2-a)/6 * (funciones(func, a) + 4*(funciones(func, ((a+a2)/2))) + funciones(func, a2))
            a,a2 = a2,a2+h
        return temp
    if(opc == 5):    
        return (b-a)/8 * (funciones(func, a) + 3*(funciones(func, ((b-a)/3)+a)) + 3*(funciones(func, (2*(b-a)/3)+a)) + funciones(func, b))
    if(opc == 6):
        h = (b-a)/n
        a2 = a + h
        temp = 0
        for i in range(n):
            temp += (a2-a)/8 * (funciones(func, a) + 3*(funciones(func, ((a2-a)/3)+a)) + 3*(funciones(func, (2*(a2-a)/3)+a)) + funciones(func, a2))
            a,a2 = a2,a2+h
        return temp

def graficar(opc,func,a,b,n):
    numPuntos = 30
    x = np.linspace(a, b, numPuntos)
    y = [funciones(func, X) for X in x]
    plt.plot(x,y)
    if(opc == 1):
        if(func == 3):
            x2 = [a,(a+b)/2,b]
            y2 = [funciones(func, X) for X in x2]
            plt.fill(x2,y2,alpha=0.2)
        elif(func==1 or func ==4):
            x2 = [a,(a+b)/3,2*(a+b)/3,b]
            y2 = [funciones(func, X) for X in x2]
            plt.fill(x2,y2,alpha=0.2)
        else:
            x2 = [a,(a+b)/3,2*(a+b)/3,b]
            y2 = [funciones(func, X) for X in x2]
            plt.fill(x2,y2,alpha=0.2)
    if(opc == 2):
        x2=[]
        h = (b-a)/n
        x2.append(a)
        for x in range(n):
            a+=h
            x2.append(a)
        y2 = [funciones(func, X) for X in x2]
        plt.fill(x2,y2,alpha=0.2)
    if(opc == 3):
        x2 = [a,(a+b)/2,b]
        y2 = [funciones(func, X) for X in x2]
        plt.fill(x2,y2,alpha=0.2)
    if(opc == 4):
        x2=[]
        h = (b-a)/n
        x2.append(a)
        for x in range(n):
            a+=h
            x2.append(a)
        y2 = [funciones(func, X) for X in x2]
        LagrangeSimpson(x2[len(x2)//2]+0.1,x2, y2, n)
    if(opc == 5):
        x2 = []
        h = (b-a)/4
        x2.append(a)
        for x in range(4):
            a+=h
            x2.append(a)
        y2 = [funciones(func, X) for X in x2]
        LagrangeSimpson(x2[len(x2)//2]+0.1,x2, y2, 3)
    if(opc == 6):
        x2 = []
        h = (b-a)/(n+3)
        x2.append(a)
        for x in range(n+3):
           a+=h
           x2.append(a)
        y2 = [funciones(func, X) for X in x2]
        LagrangeSimpson(x2[len(x2)//2]+0.1,x2, y2, n+2)
def menu():
    while(True):
        mensajeIntegracion()
        opc = int(input())
        if(opc == 0):
            break
        
        if(opc>0 and opc<7):
            mensajeFunciones()
            func = int(input())
            if(opc!=0):
                a,b,n = mensajeIntervalos(opc)
                resultado = evaluar(opc, func, a, b, n)
                print("El resultado es: ", resultado)
                plt.figure()
                graficar(opc, func, a, b, n)
                plt.show()
        else:
            print("Opcion no válida, intente nuevamente")
        
    
    
    