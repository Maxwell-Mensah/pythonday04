class Astronaut:
    
    __next_id = 0 #initialisation du premier id à zero
    
    def __init__(self, name, snacks=0, destination=None):
        self.__id= Astronaut.__next_id
        Astronaut.__next_id += 1 #incrémentation de la variable d'id de la class Astronaut pour le prochain astronaut créé
        self.name=name
        self.snacks=snacks
        self.destination=destination
        
        print(self.name, "ready for lunch !")
        
    def get_id(self):
        return self.__id
    
    def get_destination(self):
        return self.destination