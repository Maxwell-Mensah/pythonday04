class Mars:
       
    __next_id = 0
    
    def __init__(self):
        self.id= Mars.__next_id
        Mars.__next_id += 1
               
    def get_id(self):
        return self.id
    
    
class planet:
    class Mars:
        __next_id = 0
        def __init__(self, size=None):
            self.size = size
            self.id= planet.Mars.__next_id
            planet.Mars.__next_id += 1

        def get_size(self):
            return self.size

        def set_size(self, size):
            self.size = size
            
class chocolate:
    class Mars:
        __next_id = 0
        def __init__(self):
            self.id = chocolate.Mars.__next_id
            chocolate.Mars.__next_id += 1
            
