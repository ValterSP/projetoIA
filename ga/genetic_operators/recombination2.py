from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
import random

class Recombination2(Recombination):
    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        #Crossover Order:

        num_genes = ind1.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        # Create the first child by copying the selected segment from ind1
        child1 = [-1] * len(ind1.genome)
        child1[cut1:cut2 + 1] = ind1.genome[cut1:cut2 + 1]

        # Fill in the remaining genes from ind2, preserving the order
        ind2_index = 0
        for i in range(len(ind1.genome)):
            if child1[i] == -1:
                while ind2.genome[ind2_index] in child1:
                    ind2_index += 1
                child1[i] = ind2.genome[ind2_index]
                ind2_index += 1

        # Create the second child by copying the selected segment from ind2
        child2 = [-1] * len(ind1.genome)
        child2[cut1:cut2 + 1] = ind2.genome[cut1:cut2 + 1]

        # Fill in the remaining genes from ind1, preserving the order
        ind1_index = 0
        for i in range(len(ind1.genome)):
            if child2[i] == -1:
                while ind1.genome[ind1_index] in child2:
                    ind1_index += 1
                child2[i] = ind1.genome[ind1_index]
                ind1_index += 1

        ind1.genome = child1
        ind2.genome = child2


    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
