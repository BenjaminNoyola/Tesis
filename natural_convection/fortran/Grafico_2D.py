#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín Salomón Noyola García
# Tema: Gráfico 2D.

import numpy as np
from StringIO import StringIO 
import matplotlib.pyplot as plt


# Aqui importamos la matriz que deseamos graficar a partir del archivo de texto: "solucion.Res"

#~ pfile=open('T_7.txt','r') 
#~ pfile=open('den_7.txt','r') 
#~ pfile=open('nor_u_7.txt','r') 
#~ pfile=open('vel_ux_7.txt','r') 
#~ pfile=open('u','r')
pfile=open('strf','r')
data=pfile.read()
pfile.close()
data=np.genfromtxt(StringIO(data))


#Aquí graficamos el contorno de Isotermas; Esta es la solución contenida en forma matricial 
#en el archivo de texto importado anteriormente y guardado en "data".

fig = plt.figure(1) 
plt.title('Streamlines')
plt.xlabel('Y')
plt.ylabel('X')
cs1 = plt.contourf((data), 50) # Pintamos 100 niveles con relleno
plt.colorbar()
plt.savefig("STR.png")
plt.show()
