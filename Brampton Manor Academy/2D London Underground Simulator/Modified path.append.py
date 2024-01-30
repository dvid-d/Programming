# main.py

# import sys
# from os.path import abspath
# from inspect import getsourcefile

# path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
# sys.path.append(f"{path}\\Game Properties")
# sys.path.append(f"{path}\\Fonts")
# sys.path.append(f"{path}\\Maps")
# sys.path.append(f"{path}\\RunTime")
# sys.path.append(f"{path}\\Saves")
# sys.path.append(f"{path}\\Trains")

import pygame
import time
from pytmx.util_pygame import load_pygame
from button import *
from controls import *
from settings import *
from play import *
from game import *
from saves import *

#play.py

#import sys
# import sys
# from os.path import abspath
# from inspect import getsourcefile
# path = abspath(getsourcefile(lambda:0))[:-16]
# sys.path.append(f"{path}\\Game Properties")
# sys.path.append(f"{path}\\Fonts")
# sys.path.append(f"{path}\\Maps")
# sys.path.append(f"{path}\\RunTime")
# sys.path.append(f"{path}\\Saves")
# sys.path.append(f"{path}\\Trains")

#shop.py

#import pygame, sys, button
# from os.path import abspath
# from inspect import getsourcefile
# path = abspath(getsourcefile(lambda:0))[:-16]

# sys.path.append(f"{path}\\Game Properties")
# sys.path.append(f"{path}\\Fonts")
# sys.path.append(f"{path}z\Maps")
# sys.path.append(f"{path}\\RunTime")
# sys.path.append(f"{path}\\Saves")
# sys.path.append(f"{path}\\Trains")

#settings.py

#import sys
# from os.path import abspath
# from inspect import getsourcefile
# path = abspath(getsourcefile(lambda:0))[:-16]

# sys.path.append(f"{path}\\Game Properties")
# sys.path.append(f"{path}\\Fonts")
# sys.path.append(f"{path}\\Maps")
# sys.path.append(f"{path}\\RunTime")
# sys.path.append(f"{path}\\Saves")
# sys.path.append(f"{path}\\Trains")

#train.py
from os.path import abspath
from inspect import getsourcefile

path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
sys.path.append(f"{path}\\Icons")
