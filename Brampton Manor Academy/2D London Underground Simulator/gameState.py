class GameState():
    states = {"startUp":1,"savesMenu":2,"playGame":3,"inSettings":4,"returnToMenu":5,"returnToSaves":6}
    def __init__(self, state):
        self.state = states[state]
    
    def getState(self):
        return self.state
    
    def changeState(self, state):
        self.state = state