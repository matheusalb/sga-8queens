from cgitb import text
from itertools import permutations
import textwrap
import numpy as np

class DNA:
    n_genes = 24
    def __init__(self, genes=None):
        
        if genes is None:
            permutation = np.random.permutation(int(self.n_genes/3))
            # String de bits
            self.genes = ''
            for decimal in permutation:
                str_bin = format(decimal, '03b')
                self.genes += str_bin
        else:
            self.genes = genes
    
    def copy(self):
        return DNA(self.genes[:])
    
    @staticmethod
    def __insert_values(genes, insert):        
        genes_list = textwrap.wrap(genes, 3) 
        insert_list = textwrap.wrap(insert, 3)
        
        for v in insert_list:
            if v not in genes_list:
                genes_list.append(v)
        
        return ''.join(genes_list)

    @classmethod
    def crossover_cut_crossfill(cls, dna_1, dna_2, crossover_prob):
        
        if (np.random.rand() < crossover_prob):
            # Escolhe ponto de crossover
            cut_pos = np.random.randint(1, cls.n_genes/3) * 3
            # Copia primeira parte nos filhos        
            genes_1 = dna_1.genes[0:cut_pos]
            genes_2 = dna_2.genes[0:cut_pos]
                    
            # Insere valores dos pais trocados, começando a partir do ponto de quebra
            aux_1 = dna_2.genes[cut_pos:cls.n_genes] + dna_2.genes[0:cut_pos]
            aux_2 = dna_1.genes[cut_pos:cls.n_genes] + dna_1.genes[0:cut_pos]

            genes_1 = DNA.__insert_values(genes_1, aux_1)
            genes_2 = DNA.__insert_values(genes_2, aux_2)
        else:
            genes_1 = dna_1.genes[:]
            genes_2 = dna_2.genes[:]
    
        return cls(genes_1), cls(genes_2)
        
    def mutate_swap(self, mutation_prob):
        if (np.random.rand() < mutation_prob):
            i = np.random.randint(0, self.n_genes/3) 
            j = np.random.randint(0, self.n_genes/3)
            while (j == i):
                j = np.random.randint(0, self.n_genes/3)
            
            gen_list = textwrap.wrap(self.genes, 3)
            
            gen_list[i], gen_list[j] = gen_list[j], gen_list[i]
            self.genes = ''.join(gen_list)
