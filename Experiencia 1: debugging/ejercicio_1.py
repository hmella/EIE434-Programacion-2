'''
  Este script contiene 4 errores comunes de programación. Por cada error que encuentre, escriba la línea y una breve descripción del problema
'''
instruction = input("ESTRELLAS o RAYAS? ")
num = input("Cuantas? ")
if (instruction == "ESTRELLAS"):
    print("*" * num)
else if (instruction == "RAYAS"):    
    print("=" + num)
else
    print("No es una eleccion valida.")