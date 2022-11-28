import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
    return a * x ** (a - 1)


fig, ax = plt.subplots()

x_vals = np.linspace(0.8, 1, 1000)
for a in np.linspace(0,100, 10):
    y_vals = [f(x, a) for x in x_vals]
    ax.plot(x_vals, y_vals, label='y = {cons}x^({cons}-1)'.format(cons=round(a, 2)))

plt.legend()
plt.show()