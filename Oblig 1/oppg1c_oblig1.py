#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


prob_colorblind = 0.0541


# In[ ]:


def draw_person(prob):
    return np.random.rand() < prob


# In[ ]:


population_stat = []
for population in range(100000):
    colorblind_persons = 0
    for sample in range(100):
        if draw_person(prob_colorblind):
            colorblind_persons += 1
    population_stat.append(colorblind_persons)


# In[ ]:


print(np.average(population_stat))
plt.hist(population_stat)
plt.show()

