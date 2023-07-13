# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# command= lambda: {command} lets you pass on arguments

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def InitialiseGame():
    source = Tk()
    source.title("London Underground Simulator")
    screen_width = source.winfo_screenwidth()
    screen_height = source.winfo_screenheight()
    source.geometry(f"{screen_width}x{screen_height}")
    return source, screen_width, screen_height


def LoadImage(source):
    map = ImageTk.PhotoImage(Image.open("London Underground (Victoria line only).png"))
    map_label = Label(image=map)
    map_label.place(x=20, y=50)


def ClearFrame(source):
    for widget in source.winfo_children():
        widget.destroy()


def GenerateMap(source):
    ClearFrame(source)
    LoadImage(source)


def Play(playButton):
    GenerateMap(playButton)


def QuitGame():
    source.destroy()


def main_screen(source, screen_width, screen_height):
    playButton = Button(source, padx=250, pady=50, text="Play", command=lambda: Play(source), background="grey")
    playButton.place(x=screen_width/3, y=screen_height/3)

    quitButton = Button(source, padx=15, pady=15, text="Quit", background="gray", command=QuitGame)
    quitButton.place(x=screen_width/2.5 + 65, y=screen_height/1.15)

    welcome = Label(source, text="2D London Underground Simulator", font=("Times", 40))
    welcome.place(x=screen_width/3.5 - 30, y=screen_height/5)


if __name__ == "__main__":
    source, screen_width, screen_height = InitialiseGame()
    main_screen(source, screen_width, screen_height)
    source.mainloop()
