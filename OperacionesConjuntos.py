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
    if len(lista_elemento) == 0:
        return lista
    else:
        return Menos(lista, lista_elemento)

def Criterio_Complemento(lista):
    complementos = []
    aux = [] 
    for i in range(0, len(lista)):
        aux.append(lista[i])
    Conjunto = max(lista, key = lambda i: len(i))
    for a in aux:
        complementos.append(Obtener_Complemento(Conjunto, a))            
    verdades = []
    for i in range(0, len(complementos)):
        if complementos[i] in lista:
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
        print(uniones[i])
        if uniones[i] in lista:
            print(True)
            verdades.append(True)
        else:
            print(False)
            verdades.append(False)
    print(verdades)
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
    
if __name__== '__main__': 
    lista = [[],['a'],['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']];
    #x = Es_SigmaAlgebra(lista)
    y = Es_SigmaAlgebra(lista)
    print(y) 
    
