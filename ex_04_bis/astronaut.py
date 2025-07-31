import mars
import planet
import chocolate

class Astronaut:
    
    __next_id = 0
    
    def __init__(self, name, snacks=0, destination=None):
        self.__id= Astronaut.__next_id
        Astronaut.__next_id += 1
        self.name=name
        self.snacks=snacks
        self.destination=destination
        
        print(self.name, "ready for lunch !")
        
    def get_id(self):
        return self.__id
    
    def get_destination(self):
        return self.destination
    
    def get_snacks(self):
        return self.snacks
    
    def do_actions(self, param=None):
        match type(param).__module__ :
            case "planet":
                print(self.name, ": started a mission !")
                self.destination=param
                
            case "chocolate":
                print(self.name, "is eating mars number", param.id )
                self.snacks+=1
            case None :
                print(f"{self.name}: Nothing to do")
                
    def __del__(self):
        if self.destination:
            print(f"{self.name}: Mission aborted !")
        else:
            print(f"{self.name}: I may have done nothing, but I have {self.snacks} Mars to eat at least !")