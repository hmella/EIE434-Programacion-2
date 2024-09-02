# Clases
Las clases son una herramienta muy importante cuando se trabaja con códigos de gran envergadura. Las clases le permitirán agrupar y crear objetos con características y propiedades especiales que podrán ser ajustadas según sus necesidades.

En esta carpeta encontrará 3 ejercicios que les permitirá practicar esta habilidad.

## Ejercicio 1
```python
'''
  Este script contiene 4 errores comunes de programación. 
  Por cada error que encuentre, escriba la línea y una breve descripción 
  del problema
'''
instruction = input("ESTRELLAS o RAYAS? ")
num = input("Cuantas? ")
if (instruction == "ESTRELLAS"):
    print("*" * num)
else if (instruction == "RAYAS"):    
    print("=" + num)
else
    print("No es una eleccion valida.")
```

## Ejercicio 2
```python
''' 
  Crea un diccionario de estos autores y
  el año en que fallecieron. Imprime la colección en el siguiente formato:

      Charles Dickens murió en 1870.

  Charles Dickens, 1870
  William Thackeray, 1863
  Anthony Trollope, 1882
  Gerard Manley Hopkins, 1889
'''

authores = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"

for autor fecha in autores.items{}:
    print "%s" % autores + " Murio en " + "%d." % Fecha
}
```

## Ejercicio 3
```python
'''
Un viajero en el tiempo ha aparecido de repente en tu sala!

Crea una variable que represente el año de origen del viajero
(por ejemplo, año = 2000)
y saluda a nuestro extraño visitante con un mensaje diferente
si proviene del pasado lejano (antes de 1900),
de la era actual (1900-2020) o del futuro lejano (más allá de 2020).
'''

year == int.input("Hola! cual es tu año de origen? '))

if year <= 1900
    print ('Shaaaa, ese es el pasado!')
elif year > 1900 && year < 2020:
    print ("Ese es el presente!")
elif:
    print ("La media vola, ese es el futuro!!")
```

## Ejercicio 4
```python
import numpy as np
from funciones import *

A = np.array([[1.0, 2.0], [2.0, 1.0]])
B = np.array([1.0], [1.0])
c = matmul(A, B)
print(c)
```