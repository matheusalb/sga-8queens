from dna.DNA import DNA


class Board:

    crossover_prob = None
    mutation_prob = None

    def __init__(self, dna=None, fitness='default'):
        self._DNA = DNA() if dna is None else dna
        self.phenotype = self._DNA.generate_phenotype()
        self.fitness = self._calculate_fitness()
        self.fitness_type = fitness

    @staticmethod
    def check_collision(l1, c1, l2, c2):
        return l1 == l2 or c1 == c2 or abs(l1 - l2) == abs(c1 - c2)

    def _calculate_fitness(self):
        collisions = 0
        queens = self.phenotype
        for i in range(len(queens)):
            for j in range(i+1, len(queens)):
                if Board.check_collision(i, queens[i], j, queens[j]):
                    collisions += 1
        if self.fitness_type == 'default':
            return 1/(1+collisions)
        elif self.fitness_type == 'linear':
            return (28 - collisions)

    @classmethod
    def reproduce(cls, board_1, board_2):
        dna_1, dna_2 = DNA.crossover(
            board_1._DNA, board_2._DNA, cls.crossover_prob)

        dna_1.mutate(cls.mutation_prob)
        dna_2.mutate(cls.crossover_prob)

        return [cls(dna_1), cls(dna_2)]
