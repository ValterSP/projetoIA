
from abc import abstractmethod

import numpy as np

from ga.genetic_algorithm import GeneticAlgorithm
from ga.problem import Problem
from ga.individual import Individual

class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = GeneticAlgorithm.rand.sample(range(1, num_genes + self.problem.forklifts.__len__()), num_genes + self.problem.forklifts.__len__()-1)

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
