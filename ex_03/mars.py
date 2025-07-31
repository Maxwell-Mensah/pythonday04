class Mars:
       
    __next_id = 0
    
    def __init__(self):
        self.id= Mars.__next_id
        Mars.__next_id += 1
               
    def get_id(self):
        return self.id
    
    
class Planet:
    class Mars: ##crétion d'une inner class Mars dnas la class Mars
        def __init__(self, size=None):
            self.size = size

        def get_size(self):
            return self.size

        def set_size(self, size):
            self.size = size