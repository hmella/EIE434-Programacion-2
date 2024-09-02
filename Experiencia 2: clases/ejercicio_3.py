'''
Queremos crear una clase llamada Cache que almacene el resultado de una llamada a una función dentro de un diccionario interno para su reutilización.

Implementa un constructor para la clase Cache que tome como único argumento una función genérica f y la almacene internamente. Además, el constructor también definirá un campo llamado cache como un diccionario vacío.

Define el operador de llamada (__call__) para la clase Cache. De esta manera, un objeto Cache puede ser utilizado como una función que toma un único argumento x y devuelve f(x). Si x ya está en cache, devuelve cache[x]. De lo contrario, calcula f(x) y agrégalo al cache como el valor correspondiente al argumento x, luego devuelve cache[x].

Implementa un método clear que llame al método del diccionario del mismo nombre en el campo cache.

Las siguientes verificaciones (assert) deberían pasar si el código es correcto:

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