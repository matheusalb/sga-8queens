from itertools import permutations
import numpy as np

class DNA:
    def __init__(self):

        permutation = np.random.permutation(8)
        
        # String de bits
        self.__genes=''
        for decimal in permutations:
            str_bin = format(decimal, '03b')
            self.__genes += str_bin
        
    
    def getGenes(self):
        return self.__genes
    
    def mutate(self, prob):
        pass
