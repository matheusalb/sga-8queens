from operator import mod
import textwrap
import numpy as np

from DNA_base import DNA_base

class DNA_Variant_7(DNA_base):
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

    @staticmethod
    def __insert_values(genes, insert, i, j):
        size = len(genes)
        j = mod(j+1, size)
        
        for v in insert:
            if i == j:
                break
            if v not in genes:
                genes[j] = v
                j = mod(j+1, size)

        return genes

    @classmethod
    def crossover(cls, dna_1, dna_2, crossover_prob):
        '''
            Cruzamento Cícilico 
        '''
        if (np.random.rand() < crossover_prob):
            genes_1, genes_2 = DNA_Variant_7.CX_crossover(dna_1.genes.tolist(), dna_2.genes.tolist())
        else:
            genes_1 = dna_1.genes[:]
            genes_2 = dna_2.genes[:]

        return cls(genes_1), cls(genes_2)
    
    @staticmethod
    def CX_crossover(parent1, parent2):
        '''
        
        '''
        cycles = [-1]*DNA_Variant_7.n_genes
        cycle_no = 1
        cyclestart = (i for i,v in enumerate(cycles) if v < 0)

        for pos in cyclestart:

            while cycles[pos] < 0:
                cycles[pos] = cycle_no
                pos = parent1.index(parent2[pos])

            cycle_no += 1

        child1 = [parent1[i] if n%2 else parent2[i] for i,n in enumerate(cycles)]
        child2 = [parent2[i] if n%2 else parent1[i] for i,n in enumerate(cycles)]

        return np.array(child1), np.array(child2)

    def mutate(self, mutation_prob):
        pass
            
    def generate_phenotype(self):
        return self.genes


dna_1 = DNA_Variant_7()
dna_2 = DNA_Variant_7()

print(dna_1.genes)
print(dna_2.genes)

dna_f1, dna_f2 = DNA_Variant_7.crossover(dna_1, dna_2, 1)

print(dna_f1.genes)
print(dna_f2.genes)
