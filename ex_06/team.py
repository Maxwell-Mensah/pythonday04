class Team:
    def __init__(self, name):
        self.team_name=name
        self.astr=[] #création de la liste interne de Team
        
    def get_name(self):
        return self.team_name
    
    def get_astronauts(self):
        return self.astr
    
    def add(self, astronaut):
        if type(astronaut).__qualname__=="Astronaut": #si l'argument est un objet Astronaut
            self.astr.append(astronaut)
        else : #argument!= Astroanut
            print(f"{self.team_name}: Sorry, you are not part of the team")

    def remove(self, astronaut):
        self.astr.remove(astronaut) #suppression de astronaut de la liste interne de Team avec la méthode remove sur les listes
    
    def count_members(self):
        return len(self.astr)
    
    def show_members(self):
        if len(self.astr)>0:
            print(self.team_name, ":", end=" ")
            for astronaut in self.astr:
                if astronaut.destination==None:
                    print(f"{astronaut.name} on standby", end=", ")
                else:
                    print(f"{astronaut.name} on mission", end=", ")
        print()

