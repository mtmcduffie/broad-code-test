class Route:
    def __init__(self, id, long_name):
        self.id = id
        self.long_name = long_name
    def __str__(self):
        return self.long_name

class Stop:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name