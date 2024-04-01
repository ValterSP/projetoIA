from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        index1 = GeneticAlgorithm.rand.randint(0, ind.num_genes - 1)
        index2 = GeneticAlgorithm.rand.randint(0, ind.num_genes - 1)

        ind.genome[index1], ind.genome[index2] = ind.genome[index2], ind.genome[index1]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
