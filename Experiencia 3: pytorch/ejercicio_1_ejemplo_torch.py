import torch
import math

dtype = torch.float
# device = torch.device("cpu")  # Dispositivo para ejecutar en CPU
device = torch.device("cuda:0") # Descomenta esto para ejecutar en GPU

# Crear datos de entrada y salida aleatorios
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Inicializar pesos aleatoriamente
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):
    # Paso hacia adelante: calcular y predicho
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Calcular y mostrar la pérdida (loss)
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # Retropropagar para calcular los gradientes de a, b, c, d con respecto a la pérdida
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Actualizar pesos utilizando descenso de gradiente
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


print(f'Resultado: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')
