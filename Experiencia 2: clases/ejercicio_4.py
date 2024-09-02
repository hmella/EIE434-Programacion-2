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