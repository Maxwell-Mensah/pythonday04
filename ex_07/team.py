from astronaut import Astronaut
from phobos import Phobos
class Team:
    def __init__(self, name):
        self.team_name=name
        self.astr=[]
        
    def get_name(self):
        return self.team_name
    
    def get_astronauts(self):
        return self.astr
    
    def add(self, astronaut):
        if type(astronaut).__qualname__=="Astronaut":
            self.astr.append(astronaut)
        else :
            print(f"{self.team_name}: Sorry, you are not part of the team")

    def remove(self, astronaut):
        self.astr.remove(astronaut)
    
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
        
    def do_actions(self, param=None):
        if param:
            for astronaut in self.astr:
                astronaut.do_actions(param)
        else:
            print(f"{self.team_name}: Nothing to do")
        
        Phobos(param)
            
            

