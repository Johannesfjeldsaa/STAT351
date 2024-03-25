"""
Simulating excercise 3b) and 3c) on oblig 1
"""


import numpy as np


def pdf(x):
    return 2*x


def check_normalization(lw, up, n):
    y = [pdf(x) for x in np.linspace(lw, up, n**2)]
    error_tolerance = 10**(-4)

    i = np.trapz(y) / (n**2)
    if 1 - error_tolerance <= i and i <= 1 + error_tolerance:
        return True
    else:
        print(i)
        return False


def exp_val(x_vals, n):
    """
    Finding the expection value of PDF
    """
    y = [x*pdf(x) for x in x_vals]
    return np.trapz(y) / n


def var_val(x_vals, n, exp_val = None):
    """
    Calulates the variance of a PDF
    """
    if exp_val is not None:
        y = [(x**2 * pdf(x)) for x in x_vals]
        E_x2 = np.trapz(y) / n
        return E_x2 - exp_val**2
    else:
        y = [(x ** 2 * pdf(x)) for x in x_vals]
        E_x2 = np.trapz(y) / n
        y_exp = [x*pdf(x) for x in x_vals]
        e_x_all_2 = (np.trapz(y_exp) / n)**2
        return E_x2 - e_x_all_2


def calc(lw, up, n):
    """
    Does the basic calulations.
    :param lw: Lower x-value
    :param up: Upper x-value
    :param n: Resuolution for the numerical integration
    """
    x_vals = np.linspace(start=lw, stop=up, num=n)
    if check_normalization(lw, up, n):
        expection_value = round(exp_val(x_vals, n), 3)
        variance = round(var_val(x_vals, n, expection_value), 3)
        print(f'E(x)   = {expection_value} \n'
              f'var(X) = {variance}')
    else:
        raise ValueError("Function is not normalized and can not "
                         "be used for prob. calculations.")

if __name__ == "__main__":
    lw = 0
    up = 1
    n = 1000

    calc(lw, up, n)