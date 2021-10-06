class Scence (object):
    def enter (self):
        pass

class Engine(object):
    def __init__(self,scence_map):
        pass
    def play(self):
        pass
class death(Scence):
    def enter(self):
        pass

class centralcorridor(Scence):
    def enter(self):
        pass

class laserWeaponArmy(Scence):
    def enter(self):
        pass

class Thebridge(Scence):
    def enter(self):
        pass

class Escapepod(Scence):
    def enter(self):
        pass

class map(object):
    def __init__(self,start_scence):
        pass
    def next_scence(self,scence_next):
        pass
    def opening_scence(self):
        pass

a_map=map('central_corridor')
a_game=Engine(a_map)
a_game.play()