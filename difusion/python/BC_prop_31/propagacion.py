#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema: 

from numpy import *

lattice_y=4
lattice_x=5
T_b =0 #1.0
T_i =0 #-1.0
g = zeros([lattice_y,lattice_x,9]) #9 funciones de distribución por cada lattice
w = zeros([9])
for i in range(9):
	if i == 0:
		w[i] = 4./9.
	elif (i >= 1 and i <= 4):
		w[i] = 1./9.
	else:
		w[i] = 1./36.
#~ for i in range(lattice_y):
	#~ for j in range(lattice_x):
		#~ for k in range(9):
			#~ g[i][j][k]=k

g[3][4][5] = 507 #######################==

print"Al comienzo: \n",  g

#.(5)...Paso de propagación.........
# propagación de vectores que no estan en la frontera

g_0_0_5=g[0][0][5]
g_0_0_7=g[0][0][7]
g_0_latx_6 = g[0][lattice_x-1][6]
g_0_latx_8 = g[0][lattice_x-1][8]
g_laty_0_6 = g[lattice_y-1][0][6]
g_laty_0_8 = g[lattice_y-1][0][8]
g_laty_latx_5=g[lattice_y-1][lattice_x-1][5]
g_laty_latx_7=g[lattice_y-1][lattice_x-1][7]

for i in range (lattice_y):
	for j in range (lattice_x-1,0,-1): #propagación de todos los elementos horizontales
		g[i][j][1] = g[i][j-1][1] #vector 1
	for	j in range (lattice_x-1):
		g[i][j][3] = g[i][j+1][3] #vector 3


for i in range (lattice_y-1): #propagación de todos los elementos verticales
	for j in range (lattice_x): 
		g[i][j][2] = g[i+1][j][2] #vector 2
	
for i in range (lattice_y-1,0,-1): 
	for j in range (lattice_x):			
		g[i][j][4] = g[i-1][j][4] #vector 4

#propagación de todos los elementos diagonales
for i in range (lattice_y-1):
	for j in range (lattice_x-1,0,-1): 
		g[i][j][5] = g[i+1][j-1][5]   #vector 5

for i in range (lattice_y-1):
	for j in range (lattice_x-1): 
		g[i][j][6] = g[i+1][j+1][6]   #vector 6

for i in range (lattice_y-1,0,-1):
	for j in range (lattice_x-1):
		g[i][j][7] = g[i-1][j+1][7]   #vector 7

for i in range (lattice_y-1,0,-1):
	for j in range (lattice_x-1,0,-1): 
		g[i][j][8] = g[i-1][j-1][8]   #vector 8


g[0][0][5]=g_0_0_7
g[0][0][7]=g_0_0_5
g[0][lattice_x-1][6]=g_0_latx_8
g[0][lattice_x-1][8]=g_0_latx_6
g[lattice_y-1][0][6]=g_laty_0_8
g[lattice_y-1][0][8]=g_laty_0_6
g[lattice_y-1][lattice_x-1][5]=g_laty_latx_7
g[lattice_y-1][lattice_x-1][7]=g_laty_latx_5

print"\n después de la propagación y antes de la condición de frontera \n",  g

#~ #condición de frontera Bounce-Back
#~ for i in range(lattice_x):
	#~ g[0][i][8] = g2[0][i][6]
	#~ g[0][i][4] = g2[0][i][2]
	#~ g[0][i][7] = g2[0][i][5]
	#~ g[lattice_y-1][i][5] = g2[lattice_y-1][i][7]
	#~ g[lattice_y-1][i][2] = g2[lattice_y-1][i][4]
	#~ g[lattice_y-1][i][6] = g2[lattice_y-1][i][8]
#~ 
#~ for i in range(lattice_y):
	#~ g[i][0][8] = g2[i][0][6]
	#~ g[i][0][1] = g2[i][0][3]
	#~ g[i][0][5] = g2[i][0][7]
	#~ g[i][lattice_x-1][7] = g2[i][lattice_x-1][5]
	#~ g[i][lattice_x-1][3] = g2[i][lattice_x-1][1]
	#~ g[i][lattice_x-1][6] = g2[i][lattice_x-1][8]
	
###.(1)..condiciones de frontera (periodicas en las superior e inferior)w...
##for i in range(lattice_x):
	##g[0][i][4] = g2[lattice_y-1][i][4] #vector 4; superior
	##g[0][i][7] = g2[lattice_y-1][i][7] #vector 7
	##g[0][i][8] = g2[lattice_y-1][i][8] #vector 8
	##g[lattice_y-1][i][2] = g2[0][i][2] #vector 2; inferior
	##g[lattice_y-1][i][5] = g2[0][i][5] #vector 5;
	##g[lattice_y-1][i][6] = g2[0][i][6] #vector 6;

##k=0
##while k < lattice_y: # Vectores en la frontera lateral
	##g_b = 6.0*(T_b-(g2[k][0][0]+g2[k][0][2]+g2[k][0][3]+g2[k][0][4]+g2[k][0][6]+g2[k][0][7]))
	##g_i = 6.0*(T_i-(g2[k][lattice_x-1][0]+g2[k][lattice_x-1][1]+g2[k][lattice_x-1][2]+g2[k][lattice_x-1][4]+g2[k][lattice_x-1][5]+g2[k][lattice_x-1][8]))
	##g[k][0][1] = w[1]* g_b # vector 1; frontera izquierda
	##g[k][0][5] = w[5]* g_b # vector 5
	##g[k][0][8] = w[8]* g_b # vector 8
	##g[k][lattice_x-1][3] = w[3]*g_i # vector 3; frontera derecha
	##g[k][lattice_x-1][6] = w[6]*g_i # vector 6
	##g[k][lattice_x-1][7] = w[7]*g_i # vector 7
	##k += 1
#print"\n después de la condición de frontera \n",  g
