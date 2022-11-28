import matplotlib.pyplot as plt
import numpy as np


def a_f(x):
    if -1 < x < 1:
        return (1+x) / 2
    else:
        return 0

def b_f(x):
    if -1 < x < 1:
        return 1/2
    else:
        return 0

def c_f(x):
    if -1 < x < 1:
        return (1-x) / 2
    else:
        return 0



if __name__ == '__main__':
    x_vals = np.linspace(-2, 2, 10000)

    y_vals_a = [a_f(x) for x in x_vals]
    y_vals_b = [b_f(x) for x in x_vals]
    y_vals_c = [c_f(x) for x in x_vals]
    y_vals = [{'y_vals': y_vals_a, 'label': r'$y = \frac{1+x}{2}$'},
              {'y_vals': y_vals_b, 'label': r'$y = \frac{1}{2}$'},
              {'y_vals': y_vals_c, 'label': r'$y = \frac{1-x}{2}$'}]


    fig, ax = plt.subplots()

    for dict in y_vals:
        ax.plot(x_vals, dict['y_vals'], label=dict['label'])

    ax.legend()
    plt.show()
