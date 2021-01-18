#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema: 

from numpy import *
import matplotlib.pyplot as plt
 
#...Definición de parámetros...#

T_n=0.0
T_o=5.0
T_e=0.0
dx=1.0
dy=dx
dt=1.0
tw=1.0
alpha=0.25
csq=(dx**2.)/(dt**2.)
omega=1.0/(3.*alpha/(csq*dt)+0.5)
pasos=400
lattice_x=100  #####################################################
lattice_y=100  #####################################################

#listas:
T = zeros([lattice_y,lattice_x]) # se guardan las temperaturas en una matriz
f = zeros([lattice_y,lattice_x,9]) #9 funciones de distribución por cada lattice
w = zeros([9])# lista de pesos, no fue necesario crear una lista para la f_eq

# definición de los pesos en cada dirección:
for i in range(9):
	if i == 0:
		w[i] = 4./9.
	elif (i >= 1 and i <= 4):
		w[i] = 1./9.
	else:
		w[i] = 1./36.

# condiciones iniciales
for i in range (lattice_y):
	T[i][0] = T_o
	T[i][lattice_x-1] = T_e
	
for j in range(lattice_x):
	T[0][j]=T_n

# cálculo de la función de distribución al inicio
for i in range(lattice_y):
	for j in range(lattice_x):
		for k in range(9):
			f[i][j][k] = w[k]*T[i][j]


for kk in range(pasos):
	
	#cálculo de la temperatura macroscópica en cada lattice
	T = f.sum(axis=2)
	
	#....Paso de colisión
	for i in range(lattice_y):
		for j in range(lattice_x):
			for k in range(9):
				feq=w[k]*T[i][j]  #Se aplica la colisión
				f[i][j][k] = omega*feq+(1.-omega)*f[i][j][k]

	#....Propagación
	# propagación de vectores que no estan en la frontera
	for i in range (lattice_y):
		for j in range (lattice_x-1,0,-1): #propagación de todos los elementos horizontales
			f[i][j][1] = f[i][j-1][1] #vector 1
		for	j in range (lattice_x-1):
			f[i][j][3] = f[i][j+1][3] #vector 3
	
	
	for i in range (lattice_y-1): #propagación de todos los elementos verticales
		for j in range (lattice_x): 
			f[i][j][2] = f[i+1][j][2] #vector 2
		
	for i in range (lattice_y-1,0,-1): 
		for j in range (lattice_x):			
			f[i][j][4] = f[i-1][j][4] #vector 4
	
	#propagación de todos los elementos diagonales
	for i in range (lattice_y-1):
		for j in range (lattice_x-1,0,-1): 
			f[i][j][5] = f[i+1][j-1][5]   #vector 5
	
	for i in range (lattice_y-1):
		for j in range (lattice_x-1): 
			f[i][j][6] = f[i+1][j+1][6]   #vector 6
	
	for i in range (lattice_y-1,0,-1):
		for j in range (lattice_x-1):
			f[i][j][7] = f[i-1][j+1][7]   #vector 7
	
	for i in range (lattice_y-1,0,-1):
		for j in range (lattice_x-1,0,-1): 
			f[i][j][8] = f[i-1][j-1][8]   #vector 8
	
	#condiciones de frontera
	for j in range(lattice_y):
		f[j][0][1]=w[1]*T_o+w[3]*T_o-f[j][0][3] #CF lado Oeste
		f[j][0][5]=w[5]*T_o+w[7]*T_o-f[j][0][7]
		f[j][0][8]=w[8]*T_o+w[6]*T_o-f[j][0][6]
		f[j][lattice_x-1][3]=w[1]*T_e+w[3]*T_e-f[j][lattice_x-1][1] #CF lado Este
		f[j][lattice_x-1][6]=w[8]*T_e+w[6]*T_e-f[j][lattice_x-1][8]
		f[j][lattice_x-1][7]=w[5]*T_e+w[7]*T_e-f[j][lattice_x-1][5]
	
	for j in range(lattice_x):
		f[0][j][4]=w[2]*T_n+w[4]*T_n-f[0][j][2]	# CF lado Norte
		f[0][j][7]=w[5]*T_n+w[7]*T_n-f[0][j][5]
		f[0][j][8]=w[6]*T_n+w[8]*T_n-f[0][j][6]
		
		f[lattice_y-1][j][1]=f[lattice_y-2][j][1] #CF lado Sur
		f[lattice_y-1][j][2]=f[lattice_y-2][j][2]
		f[lattice_y-1][j][3]=f[lattice_y-2][j][3]
		f[lattice_y-1][j][4]=f[lattice_y-2][j][4]
		f[lattice_y-1][j][5]=f[lattice_y-2][j][5]
		f[lattice_y-1][j][6]=f[lattice_y-2][j][6]
		f[lattice_y-1][j][7]=f[lattice_y-2][j][7]
		f[lattice_y-1][j][8]=f[lattice_y-2][j][8]

T = f.sum(axis=2)
print T
savetxt('Temperatura_gral.txt', T,fmt='%.4f')
