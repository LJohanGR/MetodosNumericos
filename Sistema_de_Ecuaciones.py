import numpy as np

def sustitucionHaciaAtras(matriz,cifras):
    matriz = matriz
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    valCifras = 10**cifras
    for i in range(0,filas-1):
        pivote = matriz[i,i]
        for j in range(i+1,filas):
            temp = matriz[j,i]/pivote
            # print("temp pivote: ",temp)
            # print("j,: ",round(matriz[j,:]/10))
            temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            # print("temp2", temp2)
            if(any(abs(temp2[1:]))>1):
                # print("Chin")
                temp2 = [round(i)*valCifras for i in temp2]
            else:
                temp2 = matriz[j,:]*valCifras - (matriz[i,:]*temp)*valCifras
                
            # matriz[j,:] = matriz[j,:] - matriz[i,:]*temp
            matriz[j,:] = temp2
    
    
    X = np.zeros(filas,dtype=float)
    for i in range(filas-1,-1,-1):
        suma = 0
        for j in range(i+1,columnas-1):
            suma = suma + matriz[i,j]*X[j]
        temp = matriz[i,columnas-1]
        X[i] = (temp-suma)/matriz[i,i]
    return matriz,X

def maximoColumna(matriz,cifras):
    matriz = matriz
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    valCifras = 10**cifras
    
    for i in range(0,filas-1,1):
        # columna desde diagonal i en adelante
        columna  = abs(matriz[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(matriz[i,:])
            matriz[i,:] = matriz[dondemax+i,:]
            matriz[dondemax+i,:] = temporal
    # AB1 = np.copy(AB)
    print("Matriz acomodada, \n",matriz)
    for i in range(0,filas-1):
        pivote = matriz[i,i]
        for j in range(i+1,filas):
            temp = matriz[j,i]/pivote
            # print("temp pivote: ",temp)
            # print("j,: ",round(matriz[j,:]/10))
            temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            # print("temp2", temp2)
            if(any(abs(temp2[1:]))>1):
                # print("Chin")
                temp2 = [round(i)*valCifras for i in temp2]
            else:
                temp2 = matriz[j,:]*valCifras - (matriz[i,:]*temp)*valCifras
                
            # matriz[j,:] = matriz[j,:] - matriz[i,:]*temp
            matriz[j,:] = temp2
    
    
    X = np.zeros(filas,dtype=float)
    for i in range(filas-1,-1,-1):
        suma = 0
        for j in range(i+1,columnas-1):
            suma = suma + matriz[i,j]*X[j]
        temp = matriz[i,columnas-1]
        X[i] = (temp-suma)/matriz[i,i]
    return matriz,X

def escaladoColumna(matriz,cifras):
    matriz = matriz
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    valCifras = 10**cifras
    
    values = []
    for i in range(0,columnas-1,1):
        # columna desde diagonal i en adelante
        xd = abs(matriz[i][:-1])
        maxarg = np.argmax(xd)
        values.append(xd[0]/xd[maxarg])
    # print(values)
    # temporal=[]
    maxarg = np.argmax(values)
    mat_temp = np.copy(matriz)
    temporal = np.copy(matriz[maxarg])
    mat_temp[0,:] = np.copy(temporal)
    mat_temp[maxarg,:] = np.copy(matriz[0])
    
    matriz = np.copy(mat_temp)
    
    print("Matriz acomodada, \n",matriz)
    for i in range(0,filas-1):
        pivote = matriz[i,i]
        for j in range(i+1,filas):
            temp = matriz[j,i]/pivote
            # print("temp pivote: ",temp)
            # print("j,: ",round(matriz[j,:]/10))
            temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            # print("temp2", temp2)
            if(any(abs(temp2[1:]))>1):
                # print("Chin")
                temp2 = [round(i)*valCifras for i in temp2]
            else:
                temp2 = matriz[j,:]*valCifras - (matriz[i,:]*temp)*valCifras
                
            # matriz[j,:] = matriz[j,:] - matriz[i,:]*temp
            matriz[j,:] = temp2
    
    
    X = np.zeros(filas,dtype=float)
    for i in range(filas-1,-1,-1):
        suma = 0
        for j in range(i+1,columnas-1):
            suma = suma + matriz[i,j]*X[j]
        temp = matriz[i,columnas-1]
        X[i] = (temp-suma)/matriz[i,i]
    return matriz,X

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
#%% Por descomentar
# print("Ingrese el grado del polinomio de su sistema de ecuaciones")
# # n = int(input())

# # matriz = [[int(input()) for i in range(n+1)] for j in range(n)]

# .003 x1 + 59.14 x2 = 59.17 ,
# E2 : 5.291 x1 − 6.130 x2 = 46.78 ,

# matriz = np.array([[0.832, 0.448, 0.193, 1.00],
#                    [0.784, 0.421, -0.207, 0.00],
#                    [0.784, -0.421, 0.279, 0.00]])
# result,X = sustitucionHaciaAtras(matriz, cifras)
# print("Matriz resultante")
# print(result)
# print(X)

# matriz = np.array([[0.832, 0.448, 0.193, 1.00],
#                    [0.784, 0.421, -0.207, 0.00],
#                    [0.784, -0.421, 0.279, 0.00]])

# result,X = maximoColumna(matriz, cifras)
# print("Matriz resultante")
# print(result)
# print(X)
# matriz = np.array([[0.832, 0.448, 0.193, 1.00],
#                    [0.784, 0.421, -0.207, 0.00],
#                    [0.784, -0.421, 0.279, 0.00]])

#%%
def menu():
    while(True):
        print("Ingrese la opción que desea:\n"
              "1: Sustitución hacia atrás\n"
              "2: Pivoteo máximo de columnas\n"
              "3: Pivoteo escalado de columnas\n"
              "0: Salir")
        opc = int(input())
        if(opc==1):
            matriz,cifras = mensaje()
            
            matrizResultante, resultado = sustitucionHaciaAtras(matriz, cifras)
            print("Matriz resultante:")
            print(matrizResultante)
            print("Resultado: ")
            print(resultado)
        elif(opc == 2):
            matriz,cifras = mensaje()
            matrizResultante, resultado = maximoColumna(matriz, cifras)
            print("Matriz resultante:")
            print(matrizResultante)
            print("Resultado: ")
            print(resultado)
        elif(opc == 3):
            matriz,cifras = mensaje()
            matrizResultante, resultado = escaladoColumna(matriz, cifras)
            print("Matriz resultante:")
            print(matrizResultante)
            print("Resultado: ")
            print(resultado)
        elif(opc == 0):
            break;
        else:
            print("Ingrese una opción válida")