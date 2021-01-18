#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín Salomón Noyola García
# Tema: Gráfico 2D.
from StringIO import StringIO 
import numpy as np
import matplotlib.pyplot as plt

# Aqui importamos la matriz que deseamos graficar a partir del archivo de texto: "solucion.Res"

pfile=open('velx.txt','r') 
data=pfile.read()
pfile.close()
U=np.genfromtxt(StringIO(data))

pfile=open('vely.txt','r') 
data_2=pfile.read()
pfile.close()
V=np.genfromtxt(StringIO(data_2))


Y, X = np.mgrid[0:101:101j, 0:101:101j]

speed = np.sqrt(U*U + V*V)



fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, color='r')

#ax.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5,
#          interpolation='nearest', cmap=plt.cm.gray)

plt.show()
