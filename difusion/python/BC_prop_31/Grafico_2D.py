#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín Salomón Noyola García
# Tema: Gráfico 2D.

import numpy as np
from StringIO import StringIO 
import matplotlib.pyplot as plt


# Aqui importamos la matriz que deseamos graficar a partir del archivo de texto: "solucion.Res"

#pfile=open('Temperatura_BC_31.txt','r')
pfile=open('Temperatura_gral.txt','r') 
#pfile=open('Temperatura_gral_otro_alg.txt','r')

data=pfile.read()
pfile.close()
data=np.genfromtxt(StringIO(data))

mat=np.zeros([100,100])
lista=np.zeros([100])
dominio=np.linspace(0,99,100)

k=0
for i in range(99,-1,-1):
	for j in range(100):
		mat[k][j]=data[i][j]
	k=k+1	
print data
print mat

#Aquí graficamos el contorno de Isotermas; Esta es la solución contenida en forma matricial 
#en el archivo de texto importado anteriormente y guardado en "data".

fig = plt.figure(1) 
plt.title('Contorno de Isotermas')
plt.xlabel('y')
plt.ylabel('x')
cs1 = plt.contourf((mat), 500) # Pintamos 100 niveles con relleno
plt.colorbar()
plt.show()

k=0
for i in range(100):
	lista[i]=data[99-k][i]
	k=+1

plt.plot(dominio, lista, 'r',lw=3)   # 'y' en los rángos indicados con linspace(frontera izq, frontera der, puntos)
plt.grid(True)
plt.grid(color='b', alpha=0.5, linestyle='solid', linewidth=2.0) # intentar con dashed o solid. cambiar el ancho de línea con linewith
plt.xlim(0, 50)
plt.title(u'Perfil de temperatura en Línea media ')
plt.ylabel('Temperatura')
plt.xlabel('x')
plt.show()
