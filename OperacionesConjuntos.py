#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math 
import copy
from tqdm import tqdm
import time
from itertools import combinations

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

def Sublists(lista):
    resultado = []
    for i in range(len(lista) + 1):
        for j in range(i + 1, len(lista) + 1):
            resultado.append(lista[i:j])
    return resultado

def Uniques(lista):
    unicos = []
    for element in lista:
        if element not in unicos:
            unicos.append(element)
    return unicos

# Criterios para sigma-álgebra

def Vacio_Esta_En(lista):
    x = [True for elemento in lista if len(elemento) == 0]
    return any(x)

def Criterio_Complemento(lista, n):
    lista_total = list(range(n))
    complementos = [Obtener_Complemento(lista_total, a) for a in lista]
    verdades = [Esta_En(c, lista) for c in complementos] 
    return all(verdades)
        
def Criterio_Union(lista):
    uniones = []
    for i in range(len(lista)):
        for j in range(i):
            aux_1 = copy.copy(lista[j])
            aux_2 = copy.copy(lista[i])
            aux = Union(aux_1, aux_2)
            uniones.append(aux)
    verdades = []
    for i in range(len(uniones)):
        if Esta_En(uniones[i], lista):
            verdades.append(True)
        else:
            verdades.append(False)
    return all(verdades)

def Es_SigmaAlgebra(lista, n):
    if not Vacio_Esta_En(lista):
        None
        return False
    else:
        if Criterio_Complemento(lista, n) and Criterio_Union(lista):
            return True
        else:
            if not Criterio_Complemento(lista, n):
                None
            if  not Criterio_Union(lista):
                None
            return False
        
#  Construir todas las álgebras sobre el conjunto {0,1,...,n-1} donde n es un número dado pequeño.

def Construir_SigmaAlgebras(n):
    conjunto_inicial = list(range(n))
    Potencia = Potencia_De(conjunto_inicial)
    SigmaAlgebras = []
    infimo = []
      
    #############################
      
    infimo.append([])
    infimo.append(conjunto_inicial)
    
    ##########################
    # Cota inferior pues: {\empty, X} \subset F \subset \pow(X) 
    
    SigmaAlgebras.append(infimo)
    
    ########################
    
    Potencia_copy = copy.copy(Potencia)
    Potencia_copy.remove(conjunto_inicial)
    Potencia_copy.remove([])
    
    ###########################################
    
    lists = Sublists(Potencia_copy)
    Subsets = Uniques(sum(lists, []))
    
    All_Comb = []
    
    for i in range(0, len(Subsets)+1):
        All_Comb.append(list(combinations(Subsets, i)))
    
    Candidato = []
                   
    for i in tqdm(range(0, len(All_Comb)), desc = "Ejecutando…", ascii = False, ncols = 75):
        for j in All_Comb[i]:
            Candidato_copy = copy.copy(Candidato)
            Candidato_copy.append([])
            Candidato_copy.append(conjunto_inicial)
            aux = list(j)
            Candidato_copy = Candidato_copy + (aux)
            if Es_SigmaAlgebra(Candidato_copy, n) and Candidato_copy != conjunto_inicial:
                SigmaAlgebras.append(Candidato_copy)

    print("Completo. \n") 
              
    for i in tqdm(range(0, len(SigmaAlgebras)), desc="Ejecutando…", ascii=False, ncols=75):
        print(SigmaAlgebras[i]) 
           
    print("Completo. \n") 
       
    print("El numero de sigma algebras son: ")
    print(len(SigmaAlgebras))
    
    return SigmaAlgebras