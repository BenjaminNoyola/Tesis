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
