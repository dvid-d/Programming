states_dict = {"startUp":1,"returnToMain":2,"savesMenu":3,"returnToSaves":4,"playGame":5,"inSettings":6}

class Game():
    def __init__(self, state):
        for possible_state in states_dict:
            if states_dict[possible_state] == state:
                self.state = state
                break
        levels = {"level 1":0, "level 2":1} #continue adding level

    def getState(self):
        return self.state
    
    def changeState(self, state):
        for possible_state in states_dict:
            if states_dict[possible_state]== state:
                self.state = state
                break