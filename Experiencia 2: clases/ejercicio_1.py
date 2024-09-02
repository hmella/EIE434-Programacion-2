'''
Crea un sistema básico de gestión de animales utilizando herencia de clases. La idea es tener una clase base Animal y varias clases derivadas que representen diferentes tipos de animales.

Crea una clase llamada Animal. El constructor de la clase debe aceptar los siguientes parámetros:
  nombre: El nombre del animal.
  edad: La edad del animal.
Define un método llamado hacer_sonido que retorne un mensaje genérico como "Este animal hace un sonido."

Crea tres clases derivadas de Animal:
  Perro: Debe tener un método hacer_sonido que retorne "El perro ladra."
  Gato: Debe tener un método hacer_sonido que retorne "El gato maúlla."
  Pajaro: Debe tener un método hacer_sonido que retorne "El pájaro canta."

En cada clase derivada, agrega un método describir que retorne una cadena de texto con el formato:
  Para Perro: "Este es un perro llamado [nombre] y tiene [edad] años."
  Para Gato: "Este es un gato llamado [nombre] y tiene [edad] años."
  Para Pajaro: "Este es un pájaro llamado [nombre] y tiene [edad] años."

Crea instancias de cada una de las clases derivadas (Perro, Gato, Pajaro). Llama a los métodos hacer_sonido y describir para cada instancia y asegúrate de que los mensajes sean correctos.
'''
class Animal:
  pass