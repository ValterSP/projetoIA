import numpy as np

import warehouse.warehouse_agent_search
from ga.individual_int_vector import IntVectorIndividual


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.cost = 0
        self.fitness = 0

    def compute_fitness(self) -> float:
        forklift = 0
        all_path = [[] for _ in range(self.problem.forklifts.__len__())]
        forklift_cell = self.problem.forklifts[forklift]
        for i in range(self.num_genes + self.problem.forklifts.__len__()):
            if i != self.num_genes + self.problem.forklifts.__len__() - 1 and self.genome[i] <= self.num_genes:
                goal_cell = self.problem.products[self.genome[i] - 1]
            else:
                goal_cell = self.problem.agent_search.exit
            for pair in self.problem.pairs:
                if pair.cell1 == forklift_cell and pair.cell2 == goal_cell:
                    if len(all_path[forklift]) != 0 and all_path[forklift][-1] == pair.path[0]:
                        all_path[forklift].extend(pair.path[1:])
                    else:
                        all_path[forklift].extend(pair.path)
                    self.cost += pair.value
                    forklift_cell = goal_cell
                    break
                elif pair.cell2 == forklift_cell and pair.cell1 == goal_cell:
                    if len(all_path[forklift]) != 0 and all_path[forklift][-1] == pair.path[::-1][0]:
                        all_path[forklift].extend(pair.path[::-1][1:])
                    else:
                        all_path[forklift].extend(pair.path[::-1])
                    self.cost += pair.value
                    forklift_cell = goal_cell
                    break
            if i != self.num_genes + self.problem.forklifts.__len__() - 1 and self.genome[i] > self.num_genes:
                forklift += 1
                forklift_cell = self.problem.forklifts[forklift]
        maior = 0
        colisao = 0
        if self.problem.forklifts.__len__() != 1:
            menor = all_path[0].__len__()

            for row in all_path:
                if (row.__len__() < menor):
                    menor = row.__len__()
                if row.__len__() > maior:
                    maior = row.__len__()
            for i in range(menor):
                for j in range(self.problem.forklifts.__len__()):
                    for k in range(j + 1, self.problem.forklifts.__len__()):
                        if i != 0 and i != menor - 1:
                            if all_path[j][i] == all_path[k][i] or all_path[j][i - 1] == all_path[k][i + 1]:
                                colisao += 10
                        else:
                            if all_path[j][i] == all_path[k][i]:
                                colisao += 10

        self.fitness = self.cost + maior + colisao
        return self.fitness

    def obtain_all_path(self):
        forklift = 0
        all_path = [[] for _ in range(self.problem.forklifts.__len__())]
        forklift_cell = self.problem.forklifts[forklift]
        goal_cells = [[] for _ in range(self.problem.forklifts.__len__())]
        for i in range(self.num_genes + self.problem.forklifts.__len__()):
            if i != self.num_genes + self.problem.forklifts.__len__() - 1 and self.genome[i] <= self.num_genes:
                goal_cell = self.problem.products[self.genome[i] - 1]
                goal_cells[forklift].append(goal_cell)
            else:
                goal_cell = self.problem.agent_search.exit
            for pair in self.problem.pairs:
                if pair.cell1 == forklift_cell and pair.cell2 == goal_cell:
                    if len(all_path[forklift]) != 0 and all_path[forklift][-1] == pair.path[0]:
                        all_path[forklift].extend(pair.path[1:])
                    else:
                        all_path[forklift].extend(pair.path)
                    forklift_cell = goal_cell
                    break
                elif pair.cell2 == forklift_cell and pair.cell1 == goal_cell:
                    if len(all_path[forklift]) != 0 and all_path[forklift][-1] == pair.path[::-1][0]:
                        all_path[forklift].extend(pair.path[::-1][1:])
                    else:
                        all_path[forklift].extend(pair.path[::-1])
                    forklift_cell = goal_cell
                    break
            if i != self.num_genes + self.problem.forklifts.__len__() - 1 and self.genome[i] > self.num_genes:
                forklift += 1
                forklift_cell = self.problem.forklifts[forklift]
        steps = 0
        maior = 0
        for row in all_path:
            if row.__len__() > maior:
                maior = row.__len__()
            steps += len(row)

        return all_path, maior, goal_cells

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        return new_instance
