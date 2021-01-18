#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín Salomón Noyola García
# Tema: Gráfico 2D.

import numpy as np
from StringIO import StringIO 
import matplotlib.pyplot as plt


# Aqui importamos la matriz que deseamos graficar a partir del archivo de texto: "solucion.Res"

#pfile=open('Temp.txt','r') 
#pfile=open('velx.txt','r') 
#pfile=open('vely.txt','r') 
#pfile=open('rho.txt','r') 
pfile=open('strf.txt','r') 
data=pfile.read()
pfile.close()
data=np.genfromtxt(StringIO(data))
#n=len(data)
#print n
#cont=0
#for i in range(n):
 #   for j in range(n):
#        data[i,j]=data[n-1-cont,n-1-cont]
#    cont+=1
#data=np.transpose(data)
#Aquí graficamos el contorno de Isotermas; Esta es la solución contenida en forma matricial 
#en el archivo de texto importado anteriormente y guardado en "data".

fig = plt.figure(1) 
plt.title('Contorno de Isotermas')
plt.xlabel('Y')
plt.ylabel('X')
cs1 = plt.contourf((data), 50) # Pintamos 100 niveles con relleno
plt.colorbar()
plt.show()
