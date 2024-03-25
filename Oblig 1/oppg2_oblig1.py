"""
Simulates task 2b) and 2c) in oblig 1 STAT351
"""


def prob(x_i):
    return (1/6) * x_i


def expection_value(pop):
    return sum([x_i * prob(x_i) for x_i in pop])


def varians(pop, mu):
    return sum([(x_i-mu)**2 * prob(x_i) for x_i in pop])


if __name__ == "__main__":
    pop = [1, 2, 3]

    mu = expection_value(pop)
    sigma2 = varians(pop, mu)

    print(f'E(x)   = {mu} \n'
          f'var(X) = {sigma2}')
