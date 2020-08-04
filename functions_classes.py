# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:12:12 2020

@author: arutk
"""
import math

class Rastrigin:
    def __init__(self):
        self.domain_min = -5.12
        self.domain_max = 5.12
        self.global_minimum = 0
    
    def fitness_function(self, arguments):
        number_of_arguments = len(arguments)
        summ = 0 
        for argument in arguments:
            summ += argument**2 - 10 * math.cos(2 * math.pi * argument)
        return 10 * number_of_arguments + summ

class Griewank: 
    def __init__(self):
        self.domain_min = -600 
        self.domain_max = 600
        self.global_minimum = 0
   
    def fitness_function(self, arguments):
        # with localcontext() as ctx:
        #     ctx.prec = 100  # 100 digits precision
        summ = 0
        prod = 1
        i = 1
        for argument in arguments:
            summ += argument**2/4000
            prod *= math.cos(argument/(math.sqrt(i)))
            i += 1
        return summ - prod + 1
    
class Sphere:    
    def __init__(self):
        self.domain_min = -5.12
        self.domain_max = 5.12
        self.global_minimum = 0
        
    def fitness_function(self, arguments):
        summ = 0
        for argument in arguments:
            summ += argument**2
        return summ
    
class Zakharov:
    def __init__(self):
        self.domain_min = -5
        self.domain_max = 10
        self.global_minimum = 0
        
    def fitness_function(self, arguments):
        sum1 = 0
        sum2 = 2
        i = 1
        for argument in arguments:
            sum1 += argument**2
            sum2 += 0.5 * i * argument
            i += 1
        return sum1 + sum2**2 + sum2**4
    
class Easom:    
    def __init__(self):
        self.domain_min = -100
        self.domain_max = 100
        self.global_minimum = -1
        
    def fitness_function(self, arguments):
        arg1, arg2 = arguments
        fact1 = -1 * math.cos(arg1) * math.cos(arg2)
        fact2 = math.exp(-1 * (arg1 - math.pi)**2 - (arg2 - math.pi)**2)
        return abs(fact1 * fact2)
    
class StyblinskiTang:    
    def __init__(self, no_arg_function):
        self.domain_min = -5
        self.domain_max = 5
        self.global_minimum = -39.16599 * no_arg_function
        
    def fitness_function(self, arguments):
        summ = 0
        for argument in arguments:
            summ += argument**4 - 16*(argument**2) + (5 * argument)
        return 0.5 * summ

    