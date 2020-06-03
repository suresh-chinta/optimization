#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import numpy.random as rand
import matplotlib.pyplot as plt


# In[21]:


def square_norm(vec):
    return(sum(vec * vec))


# In[48]:


def antonio_obj(x):
    return (1 + np.cos(0.04*x)**2)*(np.exp(-x**2/20000))


# In[49]:


def get_random_start():
    return(rand.uniform(0.1, 1.0, 1)[0] * 10)


# In[52]:


def get_random_neighbour(x, T):
    return(x + (rand.uniform(-1.0, 10.0, 1)[0]))


# In[53]:


def get_next_random():
    return(rand.uniform(0.0, 1.0, 1)[0])


# In[75]:


cost_func = antonio_obj
initial_solution = np.array([5])
initial_cost = cost_func(initial_solution)
current_solution = initial_solution
current_cost = cost_func(current_solution)

#new_cost : [0.05] new_point : [256.28] new temperature : 2.2553064631951623 current_cost : [0.05] iteration 30
#new_cost : [0.1] new_point : [242.67] new temperature : 2.2553064631951623 current_cost : [0.1] iteration 30

for k in range(1, 100):
    
    T = 50/(1 + np.log(k+1))
    new_solution = get_random_neighbour(current_solution, T)
    new_cost = cost_func(new_solution)
    
    
    if current_cost > new_cost or np.exp(-(new_cost - current_cost)/T) >= get_next_random():        
        print(f'new_cost : {np.round(new_cost,4)}  current_cost : {np.round(current_cost,4)}  new_point : {np.round(new_solution,2)} new temperature : {round(T,2)} iteration {k}')
        current_solution = new_solution
        current_cost = new_cost


# In[74]:


points = np.linspace(-500,500,1000)
ValFitness = np.array([antonio_obj(i) for i in points])
plt.plot(points,ValFitness)

