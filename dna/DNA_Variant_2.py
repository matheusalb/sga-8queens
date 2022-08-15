import textwrap
import numpy as np

from DNA_base import DNA_base

class DNA_Variant_2(DNA_base):
    n_genes = 8

    def __init__(self, genes=None):
        '''
            Genótipo -> Permutação de Inteiros
        '''
        if genes is None:
            permutation = np.random.permutation(self.n_genes)
        
            self.genes = permutation
        else:
            self.genes = genes

    @classmethod
    def crossover(cls, dna_1, dna_2, crossover_prob):
        pass

    def mutate(self, mutation_prob):
        '''
            Mutação por Inversão
        '''
        if (np.random.rand() < mutation_prob):
            i = np.random.randint(0, self.n_genes)
            j = np.random.randint(0, self.n_genes)
            while (j == i):
                j = np.random.randint(0, self.n_genes)

            i, j = min(i,j), max(i,j)
            print(i, j)
            self.genes = np.concatenate((self.genes[0:i], np.flip(self.genes[i:j+1]), 
                                        self.genes[j+1:]))
            
    def generate_phenotype(self):
        return self.genes


dna = DNA_Variant_2()

print(dna.genes)
dna.mutate(1)
print(dna.genes)
