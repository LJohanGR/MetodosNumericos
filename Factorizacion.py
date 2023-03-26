import numpy as np

import math 

def verifSimetria(a, tol=1e-8):
    return np.all(np.abs(a-a.T) < tol)

def Cholesky(matriz, cifras,resultados):
    n = len(matriz)
    lower = [[0 for x in range(n)]  
                for y in range(n)] 
    
    upper =[[0 for x in range(n)]  
                for y in range(n)]

    for i in range(n):  
        for j in range(i + 1):  
            sum1 = 0; 
  
            # sum1mation for diagnols 
            if (j == i):  
                for k in range(j): 
                    sum1 += pow(lower[j][k], 2); 
                
                lower[j][j] = float(np.sqrt(matriz[j][j] - sum1)); 
            else: 
                  
                # Evaluating L(i, j) 
                # using L(j, j) 
                for k in range(j): 
                    sum1 += (lower[i][k] *lower[j][k]); 
                if(lower[j][j] > 0): 
                    lower[i][j] = float((matriz[i][j] - sum1) / 
                                               lower[j][j]); 
    for i in range(n):
        for j in range(n):
            upper[j][i] = lower[i][j]
    print("Matriz inferior")
    print(np.asarray(lower))
    print("Matriz Superior")
    print(np.asarray(upper))
    return np.asarray(upper),np.asarray(lower),resultados
 



def sustitucionHaciaAtras(matriz,cifras):
    matriz = matriz
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    valCifras = 10**cifras
    pivotes =[]
    for i in range(0,filas-1):
        pivote = matriz[i,i]
        pivotesTemp =[]
        
        for j in range(i+1,filas):
            temp = matriz[j,i]/pivote
            
            
            pivotesTemp.append(temp)
            # temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            temp2 = matriz[j,:] - (matriz[i,:]*temp)
            
            matriz[j,:] = np.asarray(temp2)
            
        pivotes.append(pivotesTemp)
    
    
    X = np.zeros(filas,dtype=float)
    for i in range(filas-1,-1,-1):
        suma = 0
        for j in range(i+1,columnas-1):
            suma = suma + matriz[i,j]*X[j]
        temp = matriz[i,columnas-1]
        X[i] = (temp-suma)/matriz[i,i]
    # print("Pivotes: ",pivotes)
    return matriz,X,pivotes

def mensaje():
    print("Ingrese la cantidad de cifras significativas a considerar")
    cifras = int(input())
    np.set_printoptions(precision=cifras)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.{n}f}".format(x,n=cifras)})

    print("Ingrese el grado del polinomio de su sistema de ecuaciones")
    n = int(input())
    print("Ingrese los valores de su matriz")
    matriz = np.array([[float(input()) for i in range(n+1)] for j in range(n)])
    print("Su matriz: ")
    print(matriz)
    
    return matriz, cifras
def mensaje2():
    print("Ingrese la cantidad de cifras significativas a considerar")
    cifras = int(input())
    np.set_printoptions(precision=cifras)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.{n}f}".format(x,n=cifras)})
    
    
    print("Ingrese el grado del polinomio de su sistema de ecuaciones")
    n = int(input())
    print("Ingrese los valores de su matriz")
    matriz = np.array([[float(input()) for i in range(n)] for j in range(n)])
    print("Su matriz: ")
    print(matriz)
    print("Ingrese los resultados de su matriz")
    resultados = np.array([[float(input())] for x in range(n)])
    print(resultados)
    return matriz, resultados,cifras

def LU(matriz,pivotes,X):
    nrows, ncolumns = matriz.shape
    k = 1
    U = matriz
    matL = [[1 if x == y else 0 for x in range(nrows)] for y in range(nrows)]
    for i in range(len(pivotes)):
    
        for j in range(len(pivotes[i])):
            matL[j+k][i] = pivotes[i][j]
        k += 1
    L = np.asarray(matL)
    print("Matriz L: ")
    print(L)
    print("Matriz U: ")
    print(U)
    print("Resultados:")
    print(X)
    
def menu():
    while(True):
        print("Elija la opción que desea:",
              "\n1: Factorización LU",
              "\n2: Factorización Cholesky",
              "\n0: Salir")
        opc = int(input())
        if(opc==1):
            matriz,cifras = mensaje()
            matriz2,X,Pivotes = sustitucionHaciaAtras(matriz,cifras)
            LU(matriz2,Pivotes,X)
        if(opc==2):
            matriz,resultados,cifras = mensaje2()
            '''
            cifras = 5
            np.set_printoptions(precision=cifras)
            np.set_printoptions(formatter={'float': lambda x: "{0:0.{n}f}".format(x,n=cifras)})
            matriz = np.array([[6,15,55],
                               [15,55,225],
                               [55,225,979]])
            resultados = np.array([[79],
                                   [295],
                                   [1259]])
            print("Shape")
            print(resultados.shape)
            '''
            
            try:
                if(verifSimetria(matriz)):
                    superior,inferior,results = Cholesky(matriz,cifras,resultados)
                    inferior = np.append(inferior,results,axis = 1)
                    mat, X, pivs = sustitucionHaciaAtras(inferior, cifras)
                    print("Primeros resultados: ")
                    print(X)
                    X = np.reshape(X,(len(X),1))
                    superior = np.append(superior,X,axis = 1)
                    print("Matriz superior evaluada")
                    print(superior)
                    mat2, X2, pivs = sustitucionHaciaAtras(superior, cifras)
                    print("Resultados:")
                    print(X2)
                    '''inf2,X,Pivs = sustitucionHaciaAtras(inferior, cifras)
                    print("X")
                    print(X)'''
                else:
                    print("La matriz no es simétrica")
            except:
                print("La matriz no es simetrica o no es positiva definida")
        if(opc==0):
            break