# -*- coding: utf-8 -*-
"""
Created on Wed May 6 14:52:32 2020

@author: arutk
"""
import random
import functions_classes as fc
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, fun, no_arg_function):
        self.x = []
        [self.x.append(random.uniform(fun.domain_min, fun.domain_max)) for i in range(no_arg_function)]
        
        self.v = []
        [self.v.append(random.uniform(-v_max/3, v_max/3)) for i in range(no_arg_function)]
        
        self.personal_best = []
        self.f_x = 1000


def particleSwarmOptimalization(fun, no_arg_function):
    swarm, global_best = swarmInitialize(fun, no_arg_function)
    global_bests = []
    mean_f_x = []
    no_iter = 0

    while no_iter < max_steps and (fun.fitness_function(global_best) - fun.global_minimum) > 0.001:
        for particle in swarm:
            if particle.f_x < fun.fitness_function(particle.personal_best):
                particle.personal_best = particle.x
            if fun.fitness_function(particle.personal_best) < fun.fitness_function(global_best):
                global_best = particle.personal_best

        global_bests.append(fun.fitness_function(global_best))
        mean_f_x_value = get_mean_fx_population(swarm)
        mean_f_x.append(mean_f_x_value)

        for particle in swarm:
            for i in range(no_arg_function):                
                particle.v[i] = omega * particle.v[i] + fi_cognitive * random.uniform(0,1) * (particle.personal_best[i] - particle.x[i]) + fi_social * random.uniform(0,1) * (global_best[i] - particle.x[i])
                particle.x[i] = particle.x[i] + particle.v[i]
            particle.f_x = fun.fitness_function(particle.x)
        no_iter += 1
    return swarm, global_best, no_iter, global_bests, mean_f_x

def swarmInitialize(fun, no_arg_function):
    swarm = []
    for i in range(swarm_size):
        particle = Particle(fun, no_arg_function)
        particle.personal_best = particle.x
        particle.f_x = fun.fitness_function(particle.x)
        swarm.append(particle)
        if i == 0:
            global_best = particle.personal_best
        if fun.fitness_function(particle.personal_best) < fun.fitness_function(global_best):
            global_best = particle.personal_best
    return swarm, global_best

def get_mean_fx_population(swarm):
    mean_f_x_values = []
    for par in swarm:
        mean_f_x_values.append(par.f_x)
    mean_f_x = np.mean(mean_f_x_values)
    return mean_f_x

def main():
    print('\nFunctions: \n1 - RASTRIGIN \n2 - GRIEWANK \n3 - SPHERE \n4 - ZAKHAROV \n5 - EASOM \n6 - SYBLINSKI-TANG')
    chosen_function = int(input('Write function number: '))  
        
    if chosen_function == 5:
        no_arg_function = 2
    else:
        no_arg_function = int(input('Write no. of arguments of the function (min. 2): '))
        
    if chosen_function == 1:
        fun = fc.Rastrigin()
    elif chosen_function == 2:
        fun = fc.Griewank()
    elif chosen_function == 3:
        fun = fc.Sphere()
    elif chosen_function == 4:
        fun = fc.Zakharov()
    elif chosen_function == 5:
        fun = fc.Easom()
    else:
        fun = fc.StyblinskiTang(no_arg_function)  

    swarm, global_best, no_iter, global_bests, mean_f_x = particleSwarmOptimalization(fun, no_arg_function)  

    print(f'\nGlobal optimum: {global_best}')
    print(f'\nValue of global optimum: {fun.fitness_function(global_best)}')
    print(f'\nNumber of iteration, in which the solution was found: {no_iter}')

    # plotting the first graph
    x = range(no_iter)
    plt.plot(x, global_bests)
    graph_title = f'Wykres zmiennosci wartosci global best od nr iteracji. \nNr funkcji: {chosen_function}. Liczba argumentów funkcji: {no_arg_function}'
    plt.title(graph_title)
    plot_name = f'./graphs/Graph_best.No_function_{chosen_function}_arg_{no_arg_function}.png'
    plt.savefig(plot_name)
    plt.show()

    # plotting the second graph
    x = range(no_iter)
    plt.plot(x, mean_f_x)
    graph_title2 = f'Wykres zmiennosci sredniej wartosci cząstki w roju od nr iteracji. \nNr funkcji: {chosen_function}. Liczba argumentów funkcji: {no_arg_function}
    plt.title(graph_title2)
    plot_name2 = f'./graphs/Graph_mean.No_function_{chosen_function}_arg_{no_arg_function}.png'
    plt.savefig(plot_name2)
    plt.show()`

if __name__ == "__main__":
    swarm_size = 30 # suggested 10 to 1000
    v_max = 1.8 # max volume of the particle
    fi_cognitive = 0.9
    fi_social = 0.6 
    omega = 0.5 # influences the value of particle volume
    max_steps = 1000 # max iterations in while loop
    
    main()