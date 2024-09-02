# Clases
Las clases son una herramienta muy importante cuando se trabaja con códigos de gran envergadura. Las clases le permitirán agrupar y crear objetos con características y propiedades especiales que podrán ser ajustadas según sus necesidades.

En esta carpeta encontrará 4 ejercicios que les permitirá practicar esta habilidad.

## Ejercicio 1
```python
'''
Crea un sistema básico de gestión de animales utilizando herencia de clases. La
idea es tener una clase base Animal y varias clases derivadas que representen
diferentes tipos de animales.

Crea una clase llamada Animal. El constructor de la clase debe aceptar los
siguientes parámetros:
  nombre: El nombre del animal.
  edad: La edad del animal.
Define un método llamado hacer_sonido que retorne un mensaje genérico como
"Este animal hace un sonido."

Crea tres clases derivadas de Animal:
  Perro: Debe tener un método hacer_sonido que retorne "El perro ladra."
  Gato: Debe tener un método hacer_sonido que retorne "El gato maúlla."
  Pajaro: Debe tener un método hacer_sonido que retorne "El pájaro canta."

En cada clase derivada, agrega un método describir que retorne un string con
el formato:
  Para Perro: "Este es un perro llamado [nombre] y tiene [edad] años."
  Para Gato: "Este es un gato llamado [nombre] y tiene [edad] años."
  Para Pajaro: "Este es un pájaro llamado [nombre] y tiene [edad] años."

Crea instancias de cada una de las clases derivadas (Perro, Gato, Pajaro). Llama
a los métodos hacer_sonido y describir para cada instancia y asegúrate de que los 
mensajes sean correctos.
'''
class Animal:
  pass
```

## Ejercicio 2
```python
'''
Crearemos una clase Punto que representará un punto en un plano 2D. Esta clase 
utilizará varias funciones mágicas para permitir operaciones matemáticas y 
comparaciones entre puntos.

Crea una clase llamada Punto que tenga dos atributos:
  x: Coordenada x del punto.
  y: Coordenada y del punto.

Implementa el método __init__ para inicializar las coordenadas x y y del punto.

Implementa la función __str__ para que al imprimir un objeto de tipo Punto, se 
muestre en el formato (x, y).

Implementa la función __add__ para que puedas sumar dos objetos Punto utilizando 
el operador +. La suma de dos puntos debe devolver un nuevo punto cuyas coordenadas 
sean la suma de las coordenadas correspondientes.

Implementa la función __sub__ para que puedas restar dos objetos Punto utilizando 
el operador -. La resta de dos puntos debe devolver un nuevo punto cuyas coordenadas
sean la resta de las coordenadas correspondientes.

Implementa la función __eq__ para que puedas comparar dos objetos Punto utilizando
el operador ==. Dos puntos se consideran iguales si sus coordenadas x e y son
iguales.

Implementa la función __lt__ para que puedas comparar si un punto es menor que otro 
utilizando el operador <. Un punto se considera menor que otro si la suma de sus 
coordenadas es menor que la suma de las coordenadas del otro punto.

Para probar que la implementación es correcta, crea varios objetos Punto y prueba
las operaciones de suma, resta, comparación de igualdad, y comparación de orden.
'''
class Punto:
  pass
```

## Ejercicio 3
```python
'''
Queremos crear una clase llamada Cache que almacene el
resultado de unallamada a una función dentro de un diccionario
interno para su reutilización.

Implementa un constructor para la clase Cache que tome como
único argumento una función genérica f y la almacene
internamente. Además, el constructor también definirá un campo
llamado cache como un diccionario vacío.

Define el operador de llamada (__call__) para la clase Cache.
De esta manera, un objeto Cache puede ser utilizado como una
función que toma un único argumento x y devuelve f(x). Si x ya
está en cache, devuelve cache[x]. De lo contrario, calcula f(x)
y agrégalo al cache como el valor correspondiente al argumento
x, luego devuelve cache[x].

Implementa un método clear que llame al método del diccionario
del mismo nombre en el campo cache.

Las siguientes verificaciones (assert) deberían pasar si el
código es correcto:

c = Cache(math.exp)
assert c.cache == {}
assert c(1) == math.exp(1)
assert c.cache == {1: math.exp(1)}
assert c(1) == math.exp(1)
assert c.cache == {1: math.exp(1)}
assert c(2) == math.exp(2)
assert c.cache == {1: math.exp(1), 2: math.exp(2)}

c = Cache(math.sin)
assert c.cache == {}
assert c(1) == math.sin(1)
assert c.cache == {1: math.sin(1)}
assert c(2) == math.sin(2)
assert c.cache == {1: math.sin(1), 2: math.sin(2)}

d = c.cache
c.clear()
assert c.cache == {}
assert c.cache es d
'''
import math

class Cache:
  pass
```

## Ejercicio 4
```python
'''
  Escriba una clase llamada Matrix, que se inicialice con una lista de listas (al igual que los arreglos de numpy) y que permita:
    - Calcular su traspuesta
    - Imprimir los valores de la matriz a través de la terminal
    - Calcular sumas entre dos objetos de la clase
    - Calcular la multiplicación en dos objetos
'''

class Matrix:
  def __init__(self, array):
    self.array = array
```