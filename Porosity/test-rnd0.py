# Test for RegPore2D.

import matplotlib.pyplot as plt
import pandas as pd
from RecPore2D import RndPore2D as rndp


# ~ i, kk = float(sys.argv[1]), 0
# ~ while i <=0.3:
    # ~ for j in range(50):
a = rndp(lx=128., ly=128., rmin=0.5, rmax=2.0, target_porosity = 0.368, packing='rnd')
a.size = 0.001
pmin = [0.0,   0.0,   0.0 ]
pmax = [128.0, 128.0, 0.0 ]
a.bounding_box = [pmin, pmax]        
#a._pack_rnd()
a.write_mesh(fname='rnd.geo', meshtype='gmsh')

df = pd.read_csv("out.csv")
df.to_csv('plotcircles.csv')        
df["k"] = ""
#        print "len(df): ", len(df)         
for k in range(len(df)):
	df["k"][k] = plt.Circle((df["x"][k], df["y"][k]), df["r"][k], color='black') 
#        print df["k"]

fig, ax = plt.subplots(figsize = ( 16 , 16 ))
ax.set_xlim((0, 128)) 
ax.set_ylim((0, 128))
plt.xticks([])
plt.yticks([])
for k in range(len(df)):
	ax.add_artist(df["k"][k])
#plt.figure(figsize=(128, 128))
my_dpi = 128
#        plt.figure(figsize=(1280/my_dpi, 1280/my_dpi), dpi=my_dpi)
ax.set_aspect('equal')
fig.canvas.draw()
ax.margins(0)
ax.tick_params(which='both', direction='in')

fig.savefig('plotcircles.png', dpi=my_dpi) 
        # ~ print "kk: ", kk
        # ~ kk = kk+1
    # ~ i = i + 0.02
    
# poner en un while, para automatizar la creacion de las imagenes.
# con pandas guardar circles, para luego graficar circles, como se observa en la carpeta prueba.
# luego continuar con tl procedimiento de IA.   

