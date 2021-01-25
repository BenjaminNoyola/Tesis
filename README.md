# Implementación de la solución de un problema de convección natural y difusión

Estas implementaciones están basadas en el líbro de [A. A. Mohamad, Lattice Boltzmann Method, Springen, 2011]


## Ejecución del problema de convección natural
Acceder a la carpeta de natural_convection para encontrar la implementación en python y Fortran

### Implementación en python
ejecutar el código dentro de la carpeta "python" o "python_nopy" el resultado será el mismo:

    "python natural_convection.py"


### Implementación en fortran
ejecutar dentro de la carpeta "fortran"

    "gfortran -o ejecutable natural_convection.f90"
    "./ejecutable"

### Grafico de resultados
En cualquiera de las carpetas anteriores se encuantra un archivo llamado "Grafico_2D.py" se ejecuta de la siguiente manera:

    "python Grafico_2D.py"


## Ejecución del problema de difusión
Acceder a la carpeta de difusion para encontrar la implementación en python y Fortran

### Implementación en python
ejecutar el código dentro de la carpeta "python":

    "python difusion.py"


### Implementación en fortran
ejecutar dentro de la carpeta "fortran"

    "gfortran -o ejecutable difusion.f90"
    "./ejecutable"

# Generación de imágenes con porosidad no homogénea


Ingresa al directorio /Porosity y se ejecuta el siguiente comando:

    "python Calculate_Porosity.py"

Si se requieren obtener nuevas simulaciones, entonces modificar los parámetros:

    "a = rndp(lx=128., ly=128., rmin=0.5, rmax=2.0, target_porosity = 0.368, packing='rnd')"

donde "lx" es la dimensión x de la resolución de la imagen, "ly" es la dimensión y de la imagen, "rmin" es el radio 
mínimo de la partícula, al generarse aleatoriamente, "rmax" es el radio máximo. "target_porosity" es la porosidad 
buscada en la imagen, "packing" es la técnica de generación de la porosidad, "rnd" se refiere a que se hará un empacado 
aleatorio para obtener la imagen porosa.
