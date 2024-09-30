import numpy as np
import math
import matplotlib.pyplot as plt

# Crea set de datos random para el input y output
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# Inicializa pesos de manera aleatoria
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Problema forward: calcular y (predicción)
    # y = a + b x + c x^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Calcular función de perdida
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
      plt.plot(x, y)
      plt.plot(x, y_pred)
      plt.show()
      print(t, loss)

    # Backpropagation para calcular los gradientes de a, b, c y d con respecto a la función de perdida
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Actualiza pesos
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')