# Autor: Benjamín S. Noyola García
# Tema: En este código se implementan condiciones de frontera diferentes
# a las propuestas en el libro de Mohamad, se pueden observar del art de ref 31.

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
	
	#Cálculo de las condiciones de frontera tal y como se indica en la ref 31
	for i in range(lattice_y):
		g_o = 6.0*(T_o-(f[i][0][0]+f[i][0][2]+f[i][0][3]+f[i][0][4]+f[i][0][6]+f[i][0][7]))
		g_e = 6.0*(T_e-(f[i][lattice_x-1][0]+f[i][lattice_x-1][1]+f[i][lattice_x-1][2]+f[i][lattice_x-1][4]+f[i][lattice_x-1][5]+f[i][lattice_x-1][8]))
		f[i][0][1] = w[1]* g_o # vector 1; frontera izquierda
		f[i][0][5] = w[5]* g_o # vector 5
		f[i][0][8] = w[8]* g_o # vector 8
		f[i][lattice_x-1][3] = w[3]*g_e # vector 3; frontera derecha
		f[i][lattice_x-1][6] = w[6]*g_e # vector 6
		f[i][lattice_x-1][7] = w[7]*g_e # vector 7
		
	for j in range(lattice_x):
		g_n = 6.0*(T_n-(f[0][j][0]+f[0][j][1]+f[0][j][2]+f[0][j][3]+f[0][j][5]+f[0][j][6]))
		f[0][j][4] = w[4]* g_n # vector 4; frontera norte
		f[0][j][7] = w[7]* g_n # vector 7
		f[0][j][8] = w[8]* g_n # vector 8
		# Condiciones de frontera adiabáticas
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
savetxt('Temperatura_BC_31.txt', T,fmt='%.4f')
