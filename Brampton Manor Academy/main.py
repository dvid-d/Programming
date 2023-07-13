# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# command= lambda: {command} lets you pass on arguments

from tkinter import *
from tkinter import ttk


def InitialiseGame():
    source = Tk()
    source.title("London Underground Simulator")
    screen_width = source.winfo_screenwidth()
    screen_height = source.winfo_screenheight()
    source.geometry(f"{screen_width}x{screen_height}")
    return source, screen_width, screen_height


def LoadImage():
    pass


def GenerateMap(playButton):
    playButton.destroy()


def Play(playButton):
    GenerateMap(playButton)


def QuitGame():
    source.destroy()


def main_screen(source, screen_width, screen_height):
    playButton = Button(source, padx=250, pady=50, text="Play", command=lambda: Play(playButton), background="grey")
    playButton.place(x=screen_width/3, y=screen_height/3)

    quitButton = Button(source, padx=15, pady=15, text="Quit", background="gray", command=QuitGame)
    quitButton.place(x=screen_width/2.5 + 65, y=screen_height/1.15)

    welcome = Label(source, text="2D London Underground Simulator", font=("Times", 40))
    welcome.place(x=screen_width/3.5 - 30, y=screen_height/5)


if __name__ == "__main__":
    source, screen_width, screen_height = InitialiseGame()
    main_screen(source, screen_width, screen_height)
    source.mainloop()
