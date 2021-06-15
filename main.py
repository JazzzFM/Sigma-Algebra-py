#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from OperacionesConjuntos import *
from contextlib import redirect_stdout
import time

if __name__== '__main__': 
    print("Programa que dado un n, construye todas las álgebras sobre el conjunto {0,1,...,n-1} donde n es un número dado pequeño. \n")
    print("Ingrese un número natural: ")  
    input_a = input()
    input_a = int(input_a)
    print("\n")

    inicio=time.time()    
    a = Construir_SigmaAlgebras(input_a)
    fin=time.time()
    print("\n")
    print("Tiempo de ejecucion:\n")
    print(fin-inicio)
    print("\n")
    print(a)