import pygame

import json
from inspect import getsourcefile
from os.path import abspath
path = abspath(getsourcefile(lambda:0))[:-16]

class Event():

  events = []
  with open(f"{path}\\Saves\\event_descriptions.json", 'r') as save_file:
            events = json.load(save_file)

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
    pass
  
  def Display_Options(screen, option_A, option_B):
     pass
  
  def Breakdown(self, events, save_data):
    train = self.__train
    train.set_isBrokenDown = True

    repair_cost_A = events["Breakdown"]["A"]["Cost"]
    time_to_solve_A = events["Breakdown"]["A"]["Duration"]

    repair_cost_B = events["Breakdown"]["B"]["Cost"]
    time_to_solve_B = events["Breakdown"]["B"]["Duration"]

    print(f"Train ({train.getID()}) on {train.getLine().capitalize()} line has broken down.")
    print("Choose one of the options below to resolve this.")
    print()
    print(f"A: Repair train (£{repair_cost_A}, {time_to_solve_A}s)")
    print(f"B: Wait for engineers (£{repair_cost_B}, {time_to_solve_B}s)")

    decision = input().upper()

    if decision == 'A':
       new_money = save_data["money"] - repair_cost_A
       save_data["money"] = new_money


    elif decision == 'B':
       ew_money = save_data["money"] - repair_cost_B
       save_data["money"] = new_money