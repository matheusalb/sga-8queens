from DNA import DNA
import textwrap
import numpy as np

class Board:
    
    prob_crossover = None
    prob_mutation = None
    
    def __init__(self, dna=None):
        self._DNA = DNA() if dna is None else dna
        self.fitness = self._calculate_fitness()
        
    def phenotype(self):
        genes = textwrap.wrap(self._DNA.genes, 3)
        return map(lambda g: int(g, 2), genes)
        
    def _calculate_fitness(self):
        pass
    
    @classmethod
    def reproduce(cls, board_1, board_2):
        
        dna_1, dna_2 = DNA.crossover_cut_crossfill(board_1._DNA, board_2._DNA)
            
        dna_1.mutate_swap(cls.prob_mutation)
        dna_2.mutate_swap(cls.prob_mutation)
        
        return cls(dna_1), cls(dna_2)
