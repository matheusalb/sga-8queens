import textwrap
import numpy as np

from DNA_base import DNA_base


class DNA_List_Numeric(DNA_base):
    n_genes = 8

    def __init__(self, genes=None):

        if genes is None:
            permutation = np.random.permutation(self.n_genes)
            self.genes = permutation
        else:
            self.genes = genes

    @staticmethod
    def __insert_values(genes, insert):
        for v in insert:
            if v not in genes:
                genes = np.append(genes, v)

        return genes

    @classmethod
    def crossover(cls, dna_1, dna_2, crossover_prob):
        '''
            crossover_cut_crossfill
        '''
        if (np.random.rand() < crossover_prob):
            # Escolhe ponto de crossover
            cut_pos = np.random.randint(1, cls.n_genes)
            # Copia primeira parte nos filhos
            genes_1 = dna_1.genes[0:cut_pos]
            genes_2 = dna_2.genes[0:cut_pos]

            print(cut_pos)
            # Insere valores dos pais trocados, começando a partir do ponto de quebra
            aux_1 = np.concatenate((dna_2.genes[cut_pos:cls.n_genes], dna_2.genes[0:cut_pos]))
            aux_2 = np.concatenate((dna_1.genes[cut_pos:cls.n_genes], dna_1.genes[0:cut_pos]))

            genes_1 = DNA_List_Numeric.__insert_values(genes_1, aux_1)
            genes_2 = DNA_List_Numeric.__insert_values(genes_2, aux_2)
        else:
            genes_1 = dna_1.genes[:]
            genes_2 = dna_2.genes[:]

        return cls(genes_1), cls(genes_2)

    def mutate(self, mutation_prob):
        '''
            Mutate Swap
        '''
        if (np.random.rand() < mutation_prob):
            i = np.random.randint(0, self.n_genes)
            j = np.random.randint(0, self.n_genes)
            while (j == i):
                j = np.random.randint(0, self.n_genes)

            self.genes[i], self.genes[j] = self.genes[j], self.genes[i]

    def generate_phenotype(self):
        genes = textwrap.wrap(self.genes, 3)
        return list(map(lambda g: int(g, 2), genes))
