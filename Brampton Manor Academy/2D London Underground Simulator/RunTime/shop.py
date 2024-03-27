import pygame, sys
from os.path import abspath
from inspect import getsourcefile
path = abspath(getsourcefile(lambda:0))[:-16]

sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}z\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")
sys.path.append(f"{path}\\Events")

# from button import Button

class Shop():
    def __init__(self):
        self.storage = [{"Train_ID":100},{"Track_ID":20},{"Signal_ID":50}] #stores each train/track/signal as Track_ID:Price where ID is replaced by the ID of the item
        self.loans = [["Loan_ID",1000000, 0.01], ["Loan_ID", 50000, 0.03]] #LoanID, Loan Amount, Annual Interest

        
    def loadButton(path):
        shop_button_icon = pygame.image.load(f"{path}\\icons\\shop_button.png")
        pass
    
    def GetTrains(self):
        pass

    def GetTracks(self):
        pass

    def GetSignals(self):
        pass

    def UseShop(self, inShop):
        self.Shop.Load()
        while inShop:
            pass

    def Load(self):
        pass

    def Display(self):
        pass

    def BuyTrain(self, TrainID):
        pass

    def BuyTrack(self, TrackID):
        pass

    def BuySignal(self, SignalID):
        pass

    def BuyLoan(self, LoanID):
        pass

    def PayLoan(self, LoanID):
        pass