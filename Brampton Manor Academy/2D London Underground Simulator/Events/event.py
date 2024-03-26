class Event():
  
  def __init__(self, id, line, train):
    self.__ID = id
    self.__line = line
    self.__isCompleted = False
    self__train = pygame.sprite.GroupSingle(train)
  
  def setAsCompleted(self):
    self.__isCompleted = True

  def get_isCompleted(self):
    return self.__isCompleted

  def closeStation(self):
    #choose randomly between 8 and 9
    #8:"Fire alert", 9:"Flooding"
    #Fire alert affects service less
    #Flooding more severe

  def Breakdown(self):
    pass

#Trains breaking down
# Track faults
# Closed stations
# Signal issues (e.g. “signalling upgrades are needed but there is not enough funding. What do you do? {ignore} / {borrow money} / {Repair signal infrastructure}”)
# Flooding
# Crime
# Lack of available trains/drivers
# Driver Strikes
# Train getting too hot
# Fire alert
