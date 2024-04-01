from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
import random

class Recombination3(Recombination):
    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:

        child1 = [-1] * len(ind1.genome)
        child2 = [-1] * len(ind1.genome)
        num_genes = len(ind1.genome)
        cycle = []
        index = 0
        cycle.append(ind1.genome[index])

        while True:
            found_cycle = False  # Flag variable to track if a cycle has been found

            for i in range(num_genes):
                if ind1.genome[index] == ind2.genome[i]:
                    if not cycle.__contains__(ind2.genome[i]):
                        cycle.append(ind2.genome[i])
                    index = i
                    if index == 0:
                        found_cycle = True  # Set the flag to indicate a cycle has been found
                        break

            if found_cycle:
                break  # Exit the while loop

        for i in range(num_genes):
            if cycle.__contains__(ind1.genome[i]):
                child1[i] = ind1.genome[i]
                child2[i] = ind2.genome[i]

        for i in range(num_genes):
            if not child1.__contains__(ind2.genome[i]):
                index = i
                break

        index_initial = index
        cycle.clear()
        cycle.append(ind2.genome[index])
        while True:
            found_cycle = False  # Flag variable to track if a cycle has been found
            for i in range(num_genes):
                if ind2.genome[index] == ind1.genome[i]:
                    if not cycle.__contains__(ind1.genome[i]):
                        cycle.append(ind1.genome[i])
                    index = i
                    if index == index_initial:
                        found_cycle = True  # Set the flag to indicate a cycle has been found
                        break

            if found_cycle:
                break  # Exit the while loop

        for i in range(num_genes):
            if cycle.__contains__(ind2.genome[i]):
                child1[i] = ind2.genome[i]
                child2[i] = ind1.genome[i]

        for i in range(num_genes):
            if child1[i] == -1:
                child1[i] = ind2.genome[i]
            if child2[i] == -1:
                child2[i] = ind1.genome[i]

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"
