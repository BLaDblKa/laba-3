class Sport:
    def __init__(self, name):
        self.name = name

class Football(Sport):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players

class Hobby:
    def __init__(self, name):
        self.name = name

class Music(Hobby):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

class Sound(Music):
    def __init__(self, name, instrument):
        super().__init__(name, 'Sound')
        self.instrument = instrument

class Hammer(Sport):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

class Instrument(Hammer):
    def __init__(self, name, material):
        super().__init__(name, 'Heavy')
        self.material = material

class Guitar(Instrument):
    def __init__(self, name, brand):
        super().__init__(name, 'Wood')
        self.brand = brand