from operator import mod
import textwrap
import numpy as np

from DNA_base import DNA_base

class DNA_Variant_5(DNA_base):
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
            PMX
        '''
        if (np.random.rand() < crossover_prob):
            genes_1, genes_2 = DNA_Variant_5.PMX_crossover(dna_1.genes, dna_2.genes, 0)
        else:
            genes_1 = dna_1.genes[:]
            genes_2 = dna_2.genes[:]

        return cls(genes_1), cls(genes_2)
    
    @staticmethod
    def PMX_crossover(parent1, parent2, seed):
        '''
        
        '''
        rng = np.random.default_rng(seed=seed)

        cutoff_1, cutoff_2 = np.sort(rng.choice(np.arange(len(parent1)+1), size=2, replace=False))
        print(cutoff_1, cutoff_2)
        
        def PMX_one_offspring(p1, p2):
            offspring = np.zeros(len(p1), dtype=p1.dtype)

            # Copy the mapping section (middle) from parent1
            offspring[cutoff_1:cutoff_2] = p1[cutoff_1:cutoff_2]

            # copy the rest from parent2 (provided it's not already there
            for i in np.concatenate([np.arange(0,cutoff_1), np.arange(cutoff_2,len(p1))]):
                candidate = p2[i]
                while candidate in p1[cutoff_1:cutoff_2]: # allows for several successive mappings
                    print(f"Candidate {candidate} not valid in position {i}") # DEBUGONLY
                    candidate = p2[np.where(p1 == candidate)[0][0]]
                offspring[i] = candidate
            return offspring

        offspring1 = PMX_one_offspring(parent1, parent2)
        offspring2 = PMX_one_offspring(parent2, parent1)

        return offspring1, offspring2


    def mutate(self, mutation_prob):
        pass
            
    def generate_phenotype(self):
        return self.genes


dna_1 = DNA_Variant_5()
dna_2 = DNA_Variant_5()

print(dna_1.genes)
print(dna_2.genes)

dna_f1, dna_f2 = DNA_Variant_5.crossover(dna_1, dna_2, 1)

print(dna_f1.genes)
print(dna_f2.genes)