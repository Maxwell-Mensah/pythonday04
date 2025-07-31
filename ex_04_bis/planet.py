class Mars:
    __next_id = 0
    def __init__(self, size=None):
        self.size = size
        self.id=Mars.__next_id
        Mars.__next_id += 1

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size