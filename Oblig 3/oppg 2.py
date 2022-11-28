import pandas as pd

#       c)

data = [{'y': -1.15, 'u': -1, 'v': -1},
        {'y': -0.05, 'u': 1, 'v': -1},
        {'y': 0.15, 'u': -1, 'v': 1},
        {'y': 1.05, 'u': 1, 'v': 1}]

data = pd.DataFrame(data)

beta_1 = sum(data['u'] * data['y']) / sum(data['u']**2)
beta_2 = sum(data['v'] * data['y']) / sum(data['v']**2)

print(f'Beta_1 = {beta_1} \n'
      f'Beta_2 = {beta_2}')