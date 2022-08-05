from DNA import DNA
import textwrap

class Table:
    
    def __init__(self):
        self.DNA = DNA()

    def getPhenotype(self):
        genes = textwrap.wrap(self.DNA.getGenes(), 3)
        return map(lambda g: int(g, 2), genes)
    
    def fitness():
        pass
    
    