import torch
import math

dtype = torch.float
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.set_default_device(device)

# Crear Tensores para contener entradas y salidas.
# Por defecto, requires_grad=False, lo que indica que no necesitamos
# calcular gradientes con respecto a estos Tensores durante la retropropagación.
x = torch.linspace(-math.pi, math.pi, 2000, dtype=dtype)
y = torch.sin(x)

# Crear Tensores aleatorios para los pesos. Para un polinomio de tercer grado, necesitamos
# 4 pesos: y = a + b x + c x^2 + d x^3
# Establecer requires_grad=True indica que queremos calcular gradientes con
# respecto a estos Tensores durante la retropropagación.
a = torch.randn((), dtype=dtype, requires_grad=True)
b = torch.randn((), dtype=dtype, requires_grad=True)
c = torch.randn((), dtype=dtype, requires_grad=True)
d = torch.randn((), dtype=dtype, requires_grad=True)

# Escriba, usando el calculo de gradientes con backpropagation de torch, la solucion al problema de minimización de los ejemplos