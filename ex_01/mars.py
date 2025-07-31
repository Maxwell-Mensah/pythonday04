class Mars:
    
    __next_id = 0 #initialisation du premier id à zero
    
    def __init__(self):
        self.__id= Mars.__next_id
        Mars.__next_id += 1 #incrémentation de la variable d'id de la classe mars pour le prochain objet mars créé
               
    def get_id(self):
        return self.__id