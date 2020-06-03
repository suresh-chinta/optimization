# optimization of a function using non derative based method
# Based on the information available @ http://www.scholarpedia.org/article/Nelder-Mead_algorithm

import numpy as np
import pandas as pd

def square_norm(vec):
    return(sum(vec * vec))

def get_centroid(arr):
    n = len(arr)
    c = np.mean(arr[0:n-1], axis = 0)
    return(c)

def get_reflection_point(x, c, cost_func = square_norm, alpha = 1):
    x_r = c + alpha * (c - x)
    return((x_r, cost_func(x_r)))

def get_expansion_point(x, c, cost_func = square_norm, lam = 2):
    x_e = c + lam * (x - c)
    return(x_e, cost_func(x_e))

def get_contraction_point(x, c, cost_func = square_norm, beta = 1/2):
    x_c = c + beta * (x - c)
    return((x_c, cost_func(x_c)))

def sort_vertices(vertices, cost_func = square_norm):    
    costs = [cost_func(vertix) for vertix in vertices] 
    sorted_vertices = [vertices[i] for i in  np.argsort(costs)]
    sorted_costs = [costs[i] for i in np.argsort(costs)]        
    return(sorted_vertices, sorted_costs)

def nelder_meat_simplex(initial_vertices, cost_func = square_norm, limit = 1000):
    current_vertices = initial_vertices
    delta = 0.5
    all_vertices = []
    
    for i in range(1, limit):        
        sorted_vertices, sorted_costs = sort_vertices(current_vertices)
        all_vertices.append(sorted_vertices)
        centroid = get_centroid(sorted_vertices)        
        reflection_point, f_r = get_reflection_point(sorted_vertices[-1], centroid)
        
        f_l = sorted_costs[0]
        f_h = sorted_costs[-1]
        f_s = sorted_costs[-2]
       
        # not better than current best
        if (f_l <= f_r < f_s):
            sorted_vertices[-1] = reflection_point
            current_vertices = sorted_vertices
            continue
        # less than current best cost, reflection or expansion
        elif (f_r < f_l):
            expanson_pt, f_e = get_expansion_point(centroid, reflection_point)  
            if (f_e < f_r):
                sorted_vertices[-1] = expanson_pt 
                current_vertices = sorted_vertices
            else:
                sorted_vertices[-1] = reflection_point
                current_vertices = sorted_vertices
            continue  
        # between h and s, reflection or contraction
        elif (f_r >= f_s):
            # outside case
            if (f_r < f_h):
                contraction_pt, f_c = get_contraction_point(centroid, reflection_point)
                if (f_c <= f_r):
                    sorted_vertices[-1] = contraction_pt 
                    current_vertices = sorted_vertices
                else: #shrink
                    for j in range(1, len(current_vertices) -1):
                        current_vertices[j] = current_vertices[0] + delta * (current_vertices[j] - current_vertices[0])                
                continue
            # inside case
            elif (f_r >= f_h):
                contraction_pt, f_c = get_contraction_point(centroid, f_h)
                if (f_c < f_h):
                    sorted_vertices[-1] = contraction_pt 
                    current_vertices = sorted_vertices
                else: #shrink
                    for j in range(1, len(current_vertices) -1):
                        current_vertices[j] = current_vertices[0] + delta * (current_vertices[j] - current_vertices[0])                
                
                continue
    
    return((current_vertices[0], all_vertices))

x1 = np.array([10.0,20.0, 5.0])
x2 = np.array([11.0,20.0, 5.0])
x3 = np.array([10.0,21.0, 5.0])
x4= np.array([10.0,20.0, 6.0])
best_solution, search_space = nelder_meat_simplex(np.array([x1, x2, x3, x4]), limit = 500)

x1 = np.array([10.0,25.0])
x2 = np.array([11.0,20.0])
x3 = np.array([10.0,21.0])
best_solution, search_space = nelder_meat_simplex(np.array([x1, x2, x3]), limit = 90)

# Plot the travel in search space.
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(10, 5)
ax = plt.axes(xlim=(-5, 22), ylim=(-5, 22))
PolyColour = ['g','b','k','m','r']
for i in range(0, 90):
    t1 = plt.Polygon((search_space[i]), closed = True, color = PolyColour[i % 5])
    ax.axes.add_patch(t1)
plt.show()
