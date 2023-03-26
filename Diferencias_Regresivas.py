import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
xn = []
fx = []

def fact(x):
    if x<1:
        return 1
    else: return x*fact(x-1)

def regresion(x,p):
    if(x<p):
        return 1
    else: return x * regresion(x-1, p)

def evalu(xp,xn,cambiofx):
    h = stats.mean(np.diff(xn))
    fp = 0
    p = (xp - xn[len(xn)-1])/h

    ps = []
    p1 = []
    p2 = []
    for i in range(-1,n1-1):
        if(i==-1): ps.append(1)
        else:
            temp = regresion(p+i,p)/fact(i+1)
            ps.append(temp)
    
    temp = []
    for i in range(len(ps)):
        # print(cambiofx[i][-1],",",ps[i])
        fp+=cambiofx[i][-1] * ps[i]   
        temp.append(cambiofx[i][-1] * ps[i]   )
    return fp

print("Ingresa la cantidad de datos a ingresar")
n1 = int(input())


for i in range(n1):
    print("Valor de Xn: ",end="")
    xn.append(float(input()))
    print("Valor de f(Xn): ",end="")
    fx.append(float(input()))


#Generacion la tabla de diferencias
cambiofx = []
cambiofx.append(fx)
for i in range(n1):
    if(i<n1-1):
        temp=[]
        for j in range(1,len(cambiofx[i])):
            temp.append(cambiofx[i][j]-cambiofx[i][j-1])
        cambiofx.append(temp)



print("Ingrese el valor que desea obtener")
xp = float(input())

# print(ps)

fp =evalu(xp, xn, cambiofx)
print("El resultado es: ",fp)


x = np.linspace(min(xn),max(xn),len(xn)+5)
y=[]
for i in x:
    y.append(evalu(i, xn, cambiofx))

plt.figure()
plt.plot(x,y)
plt.plot(xp,fp,'o')
plt.show()
