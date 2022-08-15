from operator import mod
import textwrap
import numpy as np

from DNA_base import DNA_base

class DNA_Variant_4(DNA_base):
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
            Cruzamento de Ordem 1
        '''
        if (np.random.rand() < crossover_prob):
            # Escolhe ponto de crossover
            i = np.random.randint(0, cls.n_genes)
            j = np.random.randint(0, cls.n_genes)
            
            while (j == i):
                j = np.random.randint(0, cls.n_genes)
            
            i, j = min(i,j), max(i,j)
            
            genes_1 = np.array([-1]*cls.n_genes)
            genes_2 = np.array([-1]*cls.n_genes)
            # Copia primeira parte nos filhos
            genes_1[i:j+1] = dna_1.genes[i:j+1]
            genes_2[i:j+1] = dna_2.genes[i:j+1]

            # Insere valores dos pais trocados, começando a partir do ponto de quebra
            aux_1 = np.concatenate((dna_2.genes[j+1:cls.n_genes], dna_2.genes[0:j+1]))
            aux_2 = np.concatenate((dna_1.genes[j+1:cls.n_genes], dna_1.genes[0:j+1]))
            print(i, j)
            genes_1 = DNA_Variant_4.__insert_values(genes_1, aux_1, i, j)
            genes_2 = DNA_Variant_4.__insert_values(genes_2, aux_2, i, j)
        else:
            genes_1 = dna_1.genes[:]
            genes_2 = dna_2.genes[:]

        return cls(genes_1), cls(genes_2)

    def mutate(self, mutation_prob):
        pass
            
    def generate_phenotype(self):
        return self.genes


dna_1 = DNA_Variant_4()
dna_2 = DNA_Variant_4()

print(dna_1.genes)
print(dna_2.genes)

dna_f1, dna_f2 = DNA_Variant_4.crossover(dna_1, dna_2, 1)

print(dna_f1.genes)
print(dna_f2.genes)
