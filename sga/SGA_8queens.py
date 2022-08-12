from board.Board import Board
import numpy as np


class SGA_8queens:
    def __init__(
            self, population_size, n_generations, crossover_probability,
            mutation_probability):
        self.population = []
        self.population_size = population_size
        self.n_generations = n_generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.best = None
        self.solution = []
        Board.crossover_prob = self.crossover_probability
        Board.mutation_prob = self.mutation_probability

        self._initialize_population()

    def _initialize_population(self):
        for i in range(self.population_size):
            self.population.append(Board())
            if self.population[-1].fitness == 1:
                self.solution.append(self.population[-1])
                self.best = self.solution[-1]

    def _parent_selection_ranking(self, n_parents=2, n_choice=5):
        choices = np.random.choice(
            self.population_size, n_choice, replace=False)

        ranking = list(map(lambda i: self.population[i], choices))
        ranking.sort(reverse=True, key=lambda b: b.fitness)

        return ranking[0:n_parents]

    def _survivor_selection(self, offspring):
        selection = self.population + offspring
        selection.sort(reverse=True, key=lambda b: b.fitness)
        return selection[0:self.population_size]

    def _run_generation(self):
        parents = self._parent_selection_ranking()
        offspring = Board.reproduce(*parents)
        self.population = self._survivor_selection(offspring)
        self.best = self.population[0]
        # Verifica se é solução
        for child in offspring:
            if child.fitness == 1:
                self.solution.append(child)

    def fit(self):
        converged = False
        final_i = 0
        n_converged = len(self.solution)

        if n_converged == 0:
            for i in range(self.n_generations):
                self._run_generation()
                print("Best individual of generation " + str(i) + " ",
                      self.best.phenotype)
                print("Fitness:", self.best.fitness)

                if len(self.solution) > 0:
                    converged = True
                    final_i = i
                    n_converged = len(self.solution)
                    break
        else:
            converged = True

        return self.population, final_i, converged, n_converged, self.best