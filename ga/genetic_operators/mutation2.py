from ga import individual
from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # Inverter ordem de genes
        array = []
        cut1 = GeneticAlgorithm.rand.randint(0, ind.num_genes)
        cut2 = GeneticAlgorithm.rand.randint(0, ind.num_genes)
        if cut1 > cut2:
            cut1, cut2 = cut2, cut1

        for i in range(cut1, cut2):
            array.append(ind.genome[i])

        array.reverse()

        for i in range(cut1, cut2):
            ind.genome[i] = array[i - cut1]

        pass

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
