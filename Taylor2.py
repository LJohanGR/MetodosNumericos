import numpy as np
import matplotlib.pyplot as plt


def fact(i):
    if(i < 1):
        return 1
    else:
        return i * (fact(i-1))

def taylorEuler(x,i):
    val = 0
    for exp in range(i):
        val = (x**exp)/(fact(exp)) + val
        # print("x^",i," /",i,"!",end=" ")
    return val

def taylorEulerInv(x,i):
    val = 0
    for exp in range(i):
        val = ((-x)**exp)/(fact(exp)) + val
        # print("x^",i," /",i,"!",end=" ")
    return val

def taylorSen(x,e):
    val = 0
    for i in range(e):
        val += ( ((-1)**i) * (x**(2*i + 1))/(fact(2*i +1)) )
    return val

def taylorCos(x,e):
    val = 0
    for i in range(e):
        val += ( ((-1)**i) * (x**(2*i))/(fact(2*i)) )
    return val

def taylorSenh(x,e):
    val = 0
    for i in range(e):
        val += ( (x**((2*i)+1))/(fact((2*i)+1)) )
    return val

def taylorCosh(x,e):
    val = 0
    for i in range(e):
        val += ( (x**((2*i)))/(fact((2*i))) )
    return val

def taylorLn(x,e):
    val = 0
    if(e<=2):
        return x
    for i in range(1,e):
        val += ( (-1)**(i+1) * ( (x**i)/i ) )
            
    return val
def menu():
    while(True):
        print("Elija la opción:\n"
              "1: e^x\n"
              "2: e^-x\n"
              "3: Sen(x)\n"
              "4: Cos(x)\n"
              "5: Senh(x)\n"
              "6: Cosh(x)\n"
              "7: ln(1+x)\n"
              "0: Salir")
        opc = int(input())
        if(opc==1):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = np.exp(x)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='Exponente (e^x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorEuler(x,i), label=f"Polinomio grado {i}")#sol exacta
            
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestra todas las gráfica en una sola imagen
            
        elif (opc==2): 
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = np.exp(-x)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='Exponente (e^-x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorEulerInv(x,i), label=f"Polinomio grado {i}")#sol exacta
        
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestra todas las gráfica en una sola imagen
        
        elif (opc==3):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = np.sin(x)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='Sen(x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorSen(x,i), label=f"Polinomio grado {i}")#sol exacta
            
            
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestr
            
        elif (opc==4):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = np.cos(x)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='Cos(x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorCos(x,i), label=f"Polinomio grado {i}")#sol exacta
            
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestr
        elif (opc==5):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = ((np.exp(x)-np.exp(-x))/2)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='SenH(x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorSenh(x,i), label=f"Polinomio grado {i}")#sol exacta
            
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestr
        elif (opc==6):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = ((np.exp(x)+np.exp(-x))/2)
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='CosH(x)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorCosh(x,i), label=f"Polinomio grado {i}")#sol exacta
              
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestr
        elif (opc==7):
            print("Ingrese el intervalo a")
            a = int(input())
            print("Ingrese el intervalo b")
            b = int(input())
            print("Ingrese el número de puntos")
            numpuntos = int(input())
            #Aqui va el rango, en este caso de -4 a 2, cambiarpor a y b
            
            
            print("Ingrese la cantidad de polinomios que desea visualizar")
            n = int(input())
            print("Ingrese los grados del polinomio:")
            nexp = [int(input()) for x in range(n)]
            x = np.linspace(a, b, numpuntos)
            y = (np.log(x+1))
            plt.figure()
            plt.plot(x,y)
            plt.plot(x,y, 'b', label='ln(x+1)') #aproximaciones
            for i in nexp:
                plt.plot(x,taylorLn(x,i), label=f"Polinomio grado {i}")#sol exacta
            
            plt.legend() #legendas de las gráficas
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')     
            plt.show() #muestr
        elif (opc==0):
            break
        else: print("Intente de nuevo")
menu()