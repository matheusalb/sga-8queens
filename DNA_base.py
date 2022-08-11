from abc import ABC, abstractclassmethod, abstractmethod

class DNA_base(ABC):

    @abstractmethod
    def crossover(cls, dna_1, dna_2, crossover_prob):
        pass
    
    @abstractmethod
    def mutate(self, mutation_prob):
        pass
    
    @abstractmethod
    def generate_phenotype(self):
        pass

