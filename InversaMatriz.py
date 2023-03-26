import numpy as np

def sustAtras(matrizX,matrizIdentX):
    matriz = np.copy(matrizX.astype(float))
    matrizIdent = np.copy(matrizIdentX.astype(float))
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    valCifras = 10**cifras
    pivotes =[]
    for i in range(filas-1,-1,-1):
        pivote = matriz[i,i]
        
        
        #matriz[i,:] = np.asarray(matriz[i]/pivote)
        #matrizIdent[i,:] = np.asarray(matrizIdent[i]/pivote)
        
        if pivote == 0:
            if(i+1<=filas-1):
                filaTemp=np.copy(matriz[i,:])
                matriz[i,:] = matriz[i+1,:]
                matriz[1+i,:] = filaTemp
                pivote = matriz[i,i]
            else:
                print("no hay solución a la matriz")
        for j in range(i-1,-1,-1):
            temp = matriz[j,i]/pivote
          
            
            # temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            temp2 = matriz[j,:] - (matriz[i,:]*temp)
            
            temp3 = np.copy(matrizIdent[j,:] - (matrizIdent[i,:]*temp))
            
            matrizIdent[j] = np.copy(temp3)
            matriz[j,:] = np.asarray(temp2)
            print("Comparación")
            print(np.concatenate((matriz,matrizIdent ), axis=1))
            
            
    for i in range(0,filas):
        pivote = matriz[i,i]
        matriz[i,:] = np.asarray(matriz[i]/pivote)
        matrizIdent[i,:] = np.asarray(matrizIdent[i]/pivote)
        
    return matriz,matrizIdent

        
        
def sustitucionHaciaAtras(matrizX,matIdent,cifras,resultados):
    matriz = np.copy(matrizX.astype(float))
    matrizIdent = np.copy(matIdent.astype(float))
    tam = np.shape(matriz)
    filas = tam[0]
    columnas = tam[1]
    pivotes =[]
    
    print("Comparación")
    print(np.concatenate((matriz,matrizIdent ), axis=1))
    
    for i in range(0,filas-1):
        pivote = matriz[i,i]
        pivotesTemp =[]
        #matriz[i,:] = matriz[i,:]/pivote
        if pivote == 0:
            if(i+1<=filas-1):
                filaTemp=np.copy(matriz[i,:])
                matriz[i,:] = matriz[i+1,:]
                matriz[1+i,:] = filaTemp
                pivote = matriz[i,i]
            else:
                print("no hay solución a la matriz")
        for j in range(i+1,filas):
            temp = matriz[j,i]/pivote
            
            
            
            pivotesTemp.append(temp)
            # temp2 = matriz[j,:]/valCifras - (matriz[i,:]*temp)/valCifras
            temp2 = matriz[j,:] - (matriz[i,:]*temp)
            
            temp3 = np.copy(matrizIdent[j,:] - (matrizIdent[i,:]*temp))
            
            matrizIdent[j] = np.copy(temp3)
            matriz[j,:] = np.asarray(temp2)
            
            print("Comparación")
            print(np.concatenate((matriz,matrizIdent ), axis=1))
            
            
            
            
            
        pivotes.append(pivotesTemp)
    
    
    matxd,matidentxd = sustAtras(matriz,matrizIdent)
    
    
    results = []
    for i in range(filas):
        temp=0
        for j in range(filas):
            temp += matidentxd[i,j]*resultados[j]
        results.append(temp)
    
   
    # print("Pivotes: ",pivotes)
    return matxd,matidentxd,results
def mensaje2():
    print("Ingrese la cantidad de cifras significativas a considerar")
    cifras = int(input())
    np.set_printoptions(precision=cifras)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.{n}f}".format(x,n=cifras)})
    
    
    print("Ingrese el grado del polinomio de su sistema de ecuaciones")
    n = int(input())
    print("Ingrese los valores de su matriz")
    matriz = np.array([[float(input()) for i in range(n)] for j in range(n)])
    
    matIdentidad = np.identity(n,dtype=float)
    print("Su matriz: ")
    print(matriz)
    print("Ingrese los resultados de su matriz")
    resultados = np.array([[float(input())] for x in range(n)])
    print(resultados)
    return matriz, resultados,cifras,matIdentidad


'''
matriz = np.array([[2,-1,0],
                  [-1,2,-1],
                  [0,-1,2]])
matIdent = np.array([[1,0,0],
                     [0,1,0],
                     [0,0,1]])
'''
'''
4x1 + x2 − x3 = 7
x1 + 3x2 − x3 = 8
−x1 − x2 + 5x3 + 2x4 = −4
2x3 + 4x4 = 6



matriz = np.array([[4,1,-1,0],
                  [1,3,-1,0],
                  [-1,-1,5,2],
                  [0,0,2,4]])

matIdent = np.array([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

'''
matriz,resultados,cifras,matIdent = mensaje2()
print("Matriz inicial")
print(matriz)
matrizresult, matIdentResult, results= sustitucionHaciaAtras(matriz,matIdent, cifras,resultados)

print("Matriz inicial")
print(matriz)
print("Matriz resultante")
print(matrizresult)
print("Mat Ident")
print(matIdentResult)
print("Sol")
print(results)