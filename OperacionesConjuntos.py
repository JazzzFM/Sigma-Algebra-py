#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math 
import copy
 
#######################################
# Operaciones con conjuntos

def Union(lista_1, lista_2):
    resultado = copy.copy(lista_1)
    for j in lista_2:
            if j in lista_1:
                None
            else:
                resultado.append(j) 
    return list(resultado)

def Intersec(lista_1, lista_2):
    resultado = []
    for i in lista_1:
        if i in lista_2:
            resultado.append(i)
    return list(resultado)

def Menos(lista_1, lista_2):
    resultado = []
    for i in lista_1:
        if i in lista_2:
           None
        else:
            resultado.append(i)   
    return list(resultado)

def Dif_Simetric(lista_1, lista_2):
    resultado = []
    resultado_1 = Menos(lista_1, lista_2)
    resultado_2 = Menos(lista_2, lista_1)
    resultado = Union(resultado_1, resultado_2)
    return resultado

def Potencia_De(lista):
    resultado = [[]]
    for x in lista:
        resultado.extend([subset + [x] for subset in resultado])
    return resultado


def Obtener_Complemento(lista, lista_elemento):
    if len(lista_elemento) == 0:
        return lista
    else:
        return Menos(lista, lista_elemento)

def Tienen_Mismos_Elementos(lista_1, lista_2):
    return set(lista_1) == set(lista_2) and len(lista_1) == len(lista_2)

def Esta_En(lista_1, lista_2):
    verdades = []
    for elemento in lista_2:
        if lista_1 == elemento or Tienen_Mismos_Elementos(lista_1, elemento):
            verdades.append(True)
        else:
            verdades.append(False)
    return any(verdades)

#############################################
# Criterios para sigma-álgebra

def Vacio_Esta_En(lista):
    x = [True for elemento in lista if len(elemento) == 0]
    return any(x)

def Criterio_Complemento(lista):
    complementos = []
    aux = [] 
    for i in range(0, len(lista)):
        aux.append(lista[i])

    Total = max(lista, key = lambda i: len(i))
    
    for a in aux:
        complementos.append(Obtener_Complemento(Total, a))            
    verdades = []
    
    for i in range(0, len(complementos)):
        if Esta_En(complementos[i], lista):
            verdades.append(True)
        else:
            verdades.append(False)
    return all(verdades)
        
def Criterio_Union(lista):
    uniones = []
    for i in range(0, len(lista)):
        for j in range(0, i):
            aux_1 = copy.copy(lista[j])
            aux_2 = copy.copy(lista[i])
            aux = Union(aux_1, aux_2)
            uniones.append(aux)
    verdades = []
    for i in range(0, len(uniones)):
        if Esta_En(uniones[i], lista):
            verdades.append(True)
        else:
            verdades.append(False)
    return all(verdades)

def Es_SigmaAlgebra(lista):
    if not Vacio_Esta_En(lista):
        print("No es sigma-álgebra, pues el vacío no está en en la familia. \n")
        return False
    else:
        if Criterio_Complemento(lista) and Criterio_Union(lista):
            return True
        else:
            if not Criterio_Complemento(lista):
                print("No es sigma-álgebra, pues no cumple el criterio de que cada elemento de la familia, su complemento está en la familia. \n")
            if not Criterio_Union(lista):
                print("No es sigma-álgebra, pues no cumple el criterio de que cada colección finita de la familia, su unión está en la familia. \n")
            return False
    
########################################
# Test 
if __name__== '__main__': 
    lista = [[],['a'],['b'],['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']];
    y = Es_SigmaAlgebra(lista)
    print(y)  
    
