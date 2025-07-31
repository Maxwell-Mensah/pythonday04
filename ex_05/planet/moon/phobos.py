class Phobos:
    def __init__(self, mars=None):
        self.mars=mars
        if type(self.mars).__module__=="planet.mars":
            print("Phobos placed in orbit")
        else:
            print("No planet given")
        
    def get_mars(self):
        return self.mars