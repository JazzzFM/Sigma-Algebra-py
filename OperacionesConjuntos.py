#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math 
 
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
    resultado = lista_1
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

def Es_SigmaAlgebra(lista):
    if not Vacio_Esta_En(lista):
        print("No es sigma-álgebra")
        return False
    else:
        verdades = []
        for elemento in lista:
            elemento_lista = list(elemento)
            complemento = Menos(lista, elemento_lista)
            if complemento in lista:
                print("revisando si el elemento esta en la lista")
                verdades.append(True)
            else:
                verdades.append(False)
    return any(verdades)
    
if __name__== '__main__': 
    lista_2 = [[],['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']];
    x = Es_SigmaAlgebra(lista_2)
    print(x)
    