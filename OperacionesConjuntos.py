#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math 
import copy
 
def Union(lista_1, lista_2):
    resultado = []
    resultado.extend(lista_1 + lista_2)
    for i in resultado:
        if resultado.count(i) > 1:
            resultado.remove(i)
    return list(resultado)

def Intersec(lista_1, lista_2):
    resultado = []
    for i in lista_1:
        if i in lista_2:
            resultado.append(i)
    return list(resultado)

def Menos(lista_1, lista_2):
    resultado = copy.copy(lista_1)
    for i in lista_1:
        if i in lista_2:
            resultado.remove(i)
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

def Vacio_Esta_En(lista):
    x = [True for i in lista if len(i) == 0]
    if any(x):
        return True
    else:
        return False
    
def Obtener_Complemento(lista, lista_elemento):
    for elemento in lista_elemento:
        if elemento in lista:
            return Menos(lista, lista_elemento)
    else:
        print("Obtine una lista vacía")
        return [[]]

def Criterio_Complemento(lista):
    complementos = []
    aux = []
        
    for i in range(0, len(lista)):
        aux.append([lista[i]])
    
    for a in aux:
        complementos.append(Obtener_Complemento(lista, a))
    
    P = Potencia_De(lista)
    verdades = [True for i in range(0, len(complementos)) if complementos[i] in P]
    return any(verdades)

def Es_SigmaAlgebra(lista):
    if not Vacio_Esta_En(lista):
        print("No es sigma-álgebra")
        return False
    else:
        if Criterio_Complemento(lista):       
            return True
        else:
            False
    
    
if __name__== '__main__': 
    lista = [[],['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']];
    x = Es_SigmaAlgebra(lista)
    print(x) 

    