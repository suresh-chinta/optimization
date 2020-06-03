# function to be optimized
def square_norm(vec):
    return(sum(vec * vec))

# function to be optimized
def antonio_obj(x):
    return (-1*(1 + np.cos(0.04*x)**2)*(np.exp(-x**2/20000)))

# start somewhere
def get_random_start():
    return(rand.uniform(0.1, 1.0, 1)[0] * 10)

# retrieve a random neighbour to current point
def get_random_neighbour(x, T):
    return(x + (rand.uniform(-1.0, 10.0, 1)[0]))

# retrieve random number for stocatic decision
def get_next_random():
    return(rand.uniform(0.0, 1.0, 1)[0])

def simulated_annealing(cost_func, initial_solution) :
    
    initial_cost = cost_func(initial_solution)
    current_solution = initial_solution
    current_cost = cost_func(current_solution)

    for k in range(1, 100):

        T = 50/(1 + np.log(k+1))
        new_solution = get_random_neighbour(current_solution, T)
        new_cost = cost_func(new_solution)

        if current_cost > new_cost or np.exp(-(new_cost - current_cost)/T) >= get_next_random():        
            print(f'new_cost : {np.round(new_cost,4)}  current_cost : {np.round(current_cost,4)}  new_point : {np.round(new_solution,2)} new temperature : {round(T,2)} iteration {k}')
            current_solution = new_solution
            current_cost = new_cost           

            
def plot_cost_func(cost_func, domain = [-500,500], n = 1000):
    points = np.linspace(domain, n)
    ValFitness = np.array([cost_func(i) for i in points])
    plt.plot(points,ValFitness)
    
plot_cost_func(antonio_obj)

# not optimizing, need to tune neighbour generation
simulated_annealing(antonio_obj, 300)
