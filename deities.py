class Deity:
    
    def __init__(self):
        pass

    
    def get_deity(deity_name):
        
        if deity_name in _deities.keys():
            return _deities[deity_name]


class ExampleDeity(Deity):
    
    def __init__(self):
        super().__init__()
        self.name = "Example"


_deities = {
        #"Name": deityKonstruktor()
        "Example Deity" : ExampleDeity() 
        }

