from marmee.abstract_marmee import AbstractMarmee

class Marmee(AbstractMarmee):
    
    def __init__(self, name, inputs, filters, results):
        super(Marmee, self).__init__(
            name,
            inputs,
            filters,
            results
        )

        self.name = name
        self.inputs = inputs
        self.filters = filters
        self.results = results
