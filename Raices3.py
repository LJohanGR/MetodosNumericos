import numpy as np
import matplotlib.pyplot as plt

def opcA(x):
    val = x**3 + 4*(x**2) - 10
    return  val

def opcB(x):
    val = x**3 - 2*(x**2) - 5
    return val

def opcC(x):
    val = x**3 + 3*(x**2) - 1
    return val

def opcD(x):
    val = x - np.cos(x)
    return val

def opcE(x):
    val = np.exp(x) + 2-x + 2*np.cos(x) - 6
    return val

def opcdA(x):
    val = 3*(x**2) + 8*x
    return  val

def opcdB(x):
    val = 3*(x**2) - 4*x
    return val

def opcdC(x):
    val = 3*(x**2) + 6*x
    return val

def opcdD(x):
    val = 1 + np.sin(x)
    return val

def opcdE(x):
    val = np.exp(x) - 2*np.sin(x) -1
    return val

def opElec(op,x):
    if op == 1:
        val = opcA(x)
    elif op==2:
        val = opcB(x)
    elif op==3:
        val = opcC(x)
    elif op==4:
        val = opcD(x)
    elif op==5:
        val = opcE(x)
    return val

def opdElec(op,x):
    if op == 1:
        val = opcdA(x)
    elif op==2:
        val = opcdB(x)
    elif op==3:
        val = opcdC(x)
    elif op==4:
        val = opcdD(x)
    elif op==5:
        val = opcdE(x)
    return val

def imprimirFunc():
        print("Funciones disponibles:\n"
              +"1: x\u00b3 + 4x\u00b2 - 10\n"
              +"2: x\u00b3 -2x\u00b2 - 5\n"
              +"3: x\u00b3 + 3x\u00b2 - 1\n"
              +"4: x - cos(x)\n"
              +"5: eˣ + 2-x + 2cos(x)-6")
         
def biseccion(numpuntos, a, b, TOL, op):
    x = np.linspace(a-1,b+1,numpuntos)
    y = opElec(op, x)
    # a,b = [1,3]
    resultados = {}
    print("Ingrese num de iteraciones")
    nIter = int(input())
    # TOL = TOL
    val = False
    for i in range(nIter):
        
        # if(i == 0):
        #     a = 1
        #     b = 3
        
        if((b-a)<0.3):        
            x = np.linspace(a-((b-a)/2),b+((b-a)/2),numpuntos)
            y = opElec(op, x)
            
        p = a + (b-a)/2
        fa = opElec(op, a)
        fb = opElec(op, b)
        fp = opElec(op, p)
        
        plt.figure()
        plt.plot(x,y)
        plt.plot(x,y, 'b', color='k', label='Exponente (e^x)') #aproximaciones.
        plt.axvline(x=a, color='r', label='a')
        plt.axvline(x=b, color='b', label='b')   
        plt.axvline(x=p, color='g', label='p')   
        plt.axhline(y=0, color='k', label='p')   
        
        resultados[i]=[i+1,a,b,p,fa,fb,fp]
        
        if(p==0 or (b-a)/2 < TOL):
            val = True
            break
        else:
            if((fa*fp)>0):
                a = p
            else:
                b = p  
    print ("{:<4} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('i','a','b','p','f(a)','f(b)','f(p)'))
    for k, v in resultados.items():
        i, a, b, p, fa, fb, fp = v
        print ("{:<2} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(i, a, b, p, fa, fb, fp))
    if(val):
        print("Se encontró la raíz en p = ",p)
    else:
        print("Se llegó al Máximo de iteraciones, el valor más cercano es: ",p)
    
def newtonRaphson(numpuntos, a, b, TOL, p0, op):
    numpuntos = 50
    x = np.linspace(a-1,b+1,numpuntos)
    y = opElec(op,x)
    resultados = {}
    print("Ingrese num de iteraciones")
    nIter = int(input())
        
    plt.figure()
    plt.plot(x,y)
    plt.plot(x,y, 'b', color='b', label='f(x)') #aproximaciones.
    plt.axhline(y=0, color='k')
    val = False
    for i in range(nIter):
        p = p0 - (opElec(op, p0)/opdElec(op, p0))
        # p = p0 - opcA(p0)/opcdA(p0)
        
        plt.plot(x,opdElec(op, p0)*(x-p0)+opElec(op, p0),  label=f"i = {i+1}") #aproximaciones.
        
        resultados[i]=[i+1,p,p0,opElec(op, p0),opdElec(op, p0),np.abs(p - p0)]
        
        if(np.abs(p - p0) < TOL):
            val = True
            break
        else:
            p0 = p
    plt.legend() #legendas de las gráficas
    plt.show()
    print ("{:<4} {:<10} {:<10} {:<10} {:<10} {:<10}".format('i','p','p0','f(p0)','f\'(p0)','|p-p0|'))
    for k, v in resultados.items():
        i, p, p0, fp0, fdp0, dif = v
        print ("{:<2} {:<10.6f}  {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}".format(i, p,  p0, fp0, fdp0, dif))
    if(val):
        print("Se encontró la raíz en p = ",p)
    else:
        print("Se llegó al Máximo de iteraciones, el valor más cercano es: ",p)
def secante(numpuntos,a,b,TOL,p0,p1,op):
    x = np.linspace(a,b,numpuntos)
    y = opElec(op, x)     
    resultados = {}
    print("Ingrese num de iteraciones")
    nIter = int(input())

    plt.figure()
    plt.plot(x,y)
    plt.plot(x,y, 'b', color='b', label='f(x)') #aproximaciones.
    plt.axhline(y=0, color='k')
    for i in range(1,nIter):
        var = False
        q0 = opElec(op, p0)
        q1 = opElec(op, p1)
        p = p1 - ( (q1*(p1-p0)) / (q1-q0) )
        # p = p0 - opcA(p0)/opcdA(p0)
        
        if(p0>p):
            plt.plot(x,( (opElec(op, p0)-opElec(op, p))/(p0-p) )*(x-p)+opElec(op, p), label=f"i={i+1}") #aproximaciones.
        else:
            plt.plot(x,( (opElec(op, p)-opElec(op, p0))/(p-p0) )*(x-p0)+opElec(op, p0), label=f"i={i+1}") #aproximaciones.
            
        
           
        
        resultados[i]=[i,p,p0,p1,q0,q1,opElec(op, p),np.abs(p - p0)]
        
        if(np.abs(p - p1) < TOL):
            val = True
            break
        else:
            p0 = p1
            q0 = q1
            p1 = p
            q1 = opElec(op, p) 
    plt.legend() #legendas de las gráficas
    plt.show()
    print ("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format('i','p','p0','p1','q0','q1','f(p)','|p-p0|'))
    for k, v in resultados.items():
        i, p, p0, p1, q0,q1,fp, dif = v
        print ("{:<4} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(i, p, p0, p1, q0,q1,fp, dif))
    if(val):
        print("Se encontró la raíz en p = ",p)
    else:
        print("Se llegó al Máximo de iteraciones, el valor más cercano es: ",p)

def reglaFalsa(numpuntos,a,b,TOL,p0,p1,op):
    x = np.linspace(a,b,numpuntos)
    y = opElec(op, x)     
    resultados = {}
    print("Ingrese num de iteraciones")
    nIter = int(input())

    plt.figure()
    plt.plot(x,y)
    plt.plot(x,y, 'b', color='b', label='f(x)') #aproximaciones.
    plt.axhline(y=0, color='k')
    
    val = False
    for i in range(1,nIter):
        q0 = opElec(op, p0)
        q1 = opElec(op, p1)
        p = p1 - ( (q1*(p1-p0)) / (q1-q0) )
   
        if(p0>p):
            plt.plot(x,( (opElec(op, p0)-opElec(op, p))/(p0-p) )*(x-p)+opElec(op, p), label=f"i={i+1}") #aproximaciones.
        else:
            plt.plot(x,( (opElec(op, p)-opElec(op, p0))/(p-p0) )*(x-p0)+opElec(op, p0), label=f"i={i+1}") #aproximaciones.
             
        
        resultados[i]=[i,p,p0,p1,q0,q1,opElec(op, p),np.abs(p - p0)]
        
        q = opcA(p)
        
        if(np.abs(p - p0) < TOL):
            val = True
            break
        else:
            if((q*q1)<0):
                p0 = p
                q0 = q
            else:
                p1 = p
                q1 = q
    plt.legend() #legendas de las gráficas
    plt.show()
    print ("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format('i','p','p0','p1','q0','q1','f(p)','|p-p0|'))
    for k, v in resultados.items():
        i, p, p0, p1, q0,q1,fp, dif = v
        print ("{:<4} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(i, p, p0, p1, q0,q1,fp, dif))
    if(val):
         print("Se encontró la raíz en p = ",p)
    else:
         print("Se llegó al Máximo de iteraciones, el valor más cercano es: ",p)
def menu():
    while(True):
        print("Opciones:\n"
              +"1: Bisección\n"
              +"2: Newton Raphson\n"
              +"3: Secante\n"
              +"4: Regla falsa\n"
              +"0: Salir")
        try:
            opc = int(input())
        except:
            print("Ingrese un valor númerico entre 1 y 4 para elegir y 0 para salir.")    
        if(opc == 1):
            imprimirFunc()
            try:
                opc2 = int(input())
            except:
                print("Ingrese un valor númerico entre 1 y 5 para elegir y 0 para regresar.") 
            if(opc2 == 1):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                biseccion(numPuntos, 1, 3, TOL,1)
            elif(opc2 == 2):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                biseccion(numPuntos, 1, 4, TOL,2)
            elif(opc2 == 3):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                biseccion(numPuntos, -4, 0, TOL,3)
            elif(opc2 == 4):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                biseccion(numPuntos, 0, np.pi/2, TOL,4)
            elif(opc2 == 5):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                biseccion(numPuntos, 1, 2.5, TOL,5)
        elif(opc==2):
            imprimirFunc()
            try:
                opc2 = int(input())
            except:
                print("Ingrese un valor númerico entre 1 y 5 para elegir y 0 para regresar.") 
            if(opc2 == 1):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                newtonRaphson(numPuntos, 1, 3, TOL,p0,1)
            elif(opc2 == 2):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                newtonRaphson(numPuntos, 1, 4, TOL,p0,2)
            elif(opc2 == 3):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                newtonRaphson(numPuntos, -4, 0, TOL,p0,3)
            elif(opc2 == 4):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                newtonRaphson(numPuntos, 0, np.pi/2, TOL,p0,4)
            elif(opc2 == 5):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                newtonRaphson(numPuntos, 1, 2.5, TOL,p0,5)
        elif(opc==3):
            imprimirFunc()
            try:
                opc2 = int(input())
            except:
                print("Ingrese un valor númerico entre 1 y 5 para elegir y 0 para regresar.") 
            if(opc2 == 1):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                secante(numPuntos, 1, 3, TOL,p0,p1,1)
            elif(opc2 == 2):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                secante(numPuntos, 1, 4, TOL,p0,p1,2)
            elif(opc2 == 3):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                secante(numPuntos, -4, 0, TOL,p0,p1,3)
            elif(opc2 == 4):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                secante(numPuntos, 0, np.pi/2, TOL,p0,p1,4)
            elif(opc2 == 5):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                secante(numPuntos, 1, 2.5, TOL,p0,p1,5)                    
        elif(opc==4):
            imprimirFunc()
            try:
                opc2 = int(input())
            except:
                print("Ingrese un valor númerico entre 1 y 5 para elegir y 0 para regresar.") 
            if(opc2 == 1):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                reglaFalsa(numPuntos, 1, 3, TOL,p0,p1,1)
            elif(opc2 == 2):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                reglaFalsa(numPuntos, 1, 4, TOL,p0,p1,2)
            elif(opc2 == 3):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                reglaFalsa(numPuntos, -4, 0, TOL,p0,p1,3)
            elif(opc2 == 4):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                reglaFalsa(numPuntos, 0, np.pi/2, TOL,p0,p1,4)
            elif(opc2 == 5):
                print("Ingrese el numero de puntos: ")
                numPuntos = int(input())
                print("Ingrese la tolerancia en punto decimal:")
                TOL = float(input())
                print("Ingrese p0")
                p0 = float(input())
                print("Ingrese p1")
                p1 = float(input())
                reglaFalsa(numPuntos, 1, 2.5, TOL,p0,p1,5)
        elif(opc==0):
            break
        else:
            print("Valor no válido")