import pygame, sys, button
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")

class Shop():
    def __init__(self):
        self.storage = [{"Train_ID":100},{"Track_ID":20},{"Signal_ID":50}] #stores each train/track/signal as Track_ID:Price where ID is replaced by the ID of the item
        self.loans = [["Loan_ID",1000000, 0.01], ["Loan_ID", 50000, 0.03]] #LoanID, Loan Amount, Annual Interest

        
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