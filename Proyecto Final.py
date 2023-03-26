import numpy as np
import matplotlib.pyplot as plt
import Taylor2
import Raices3
import Sistema_de_Ecuaciones
import InterpolacionF
import Factorizacion
import Integracion

while(True):
    print("Elija la opción que desea\n"
          +"1-  Act. 2: Polinomios de Taylor y MacLaurin\n"
          +"2-  Act. 3: Calcular Raíces\n"
          +"3-  Act. 4: Interpolacion\n"
          +"4-  Act. 5: Solucion de Ecuaciones Lineales\n"
          +"5-  Act. 6: Factorización\n"
          +"6-  Act. 7: Integracion")
    opc = int(input())
    if(opc == 1):
        Taylor2.menu()
    elif(opc == 2):
        Raices3.menu()
    elif(opc == 3):
        InterpolacionF.menu()
    elif(opc == 4):
        Sistema_de_Ecuaciones.menu()
    elif(opc == 5):
        Factorizacion.menu()
    elif(opc == 6):
        Integracion.menu()
    elif(opc == 0):
        break
    else:
        print("Ingrese una opción válida")