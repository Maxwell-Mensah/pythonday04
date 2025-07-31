class Mars:
       
    __next_id = 0
    
    def __init__(self):
        self.id= Mars.__next_id
        Mars.__next_id += 1
               
    def get_id(self):
        return self.id
    