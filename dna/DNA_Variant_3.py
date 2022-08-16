import textwrap
import numpy as np

from dna.DNA_base import DNA_base


class DNA_Variant_3(DNA_base):
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
    def __insert_values(genes, insert):
        genes_list = textwrap.wrap(genes, 3)
        insert_list = textwrap.wrap(insert, 3)

        for v in insert_list:
            if v not in genes_list:
                genes_list.append(v)

        return ''.join(genes_list)

    @classmethod
    def crossover(cls, dna_1, dna_2, crossover_prob):
        '''
            crossover_cut_crossfill
        '''
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

    def mutate(self, mutation_prob):
        '''
            Mutação por Perturbação
        '''
        if (np.random.rand() < mutation_prob):
            i = np.random.randint(0, self.n_genes)
            j = np.random.randint(0, self.n_genes)
            while (j == i):
                j = np.random.randint(0, self.n_genes)

            i, j = min(i, j), max(i, j)
            print(i, j)
            self.genes = np.concatenate(
                (self.genes[0: i],
                 np.random.shuffle(self.genes[i: j + 1]),
                 self.genes[j + 1:]))

    def generate_phenotype(self):
        return self.genes


# dna = DNA_Variant_3()

# print(dna.genes)
# dna.mutate(1)
# print(dna.genes)
