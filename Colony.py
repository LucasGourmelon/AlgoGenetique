class Colony(): 
    def __init__(self):
        self.ants = []

    def add_ant(self, ant):
        self.ants.append(ant)
        return self

    def remove_ant(self, ant):
        self.ants.remove(ant)
        return self
    
    def get_ant(self, index):
        return self.ants[index]
    
    def get_ants(self):
        return self.ants

    def __str__(self):
        return "Colony with " + str(len(self.ants)) + " ants"
    
