from tkinter import *
from PIL import ImageTk, Image


def setUp(font_size, font):
    global root, frame
    root = Tk()
    root.title("KS4 & KS5 Revision Tool")
    root.geometry("1920x1080")
    frame = LabelFrame(root, width=1920, height=1100)
    frame.place(x=0, y=0)

    app_name = Label(frame, text="KS4 & KS5 Revision Tool", font=(font, font_size))
    app_name.place(x=610, y=170)

    # app_logo = Label()

    # Button for exiting program
    close = Button(frame, text="Close", command=root.quit, bg="red", fg="white")
    close.place(x=900, y=980)

    # Application info
    version = Label(frame, text="ALPHA 0.0.1")
    version.place(x=1840, y=985)


    return root, frame


def cleanScreen():
    frame.quit()
    new_frame = LabelFrame(root, width=1920, height=1100)
    return new_frame


def addButtons():
    settings()
    pass  # may not keep this


def pickLevel(font, font_size):
    gcse = Button(frame,text="GCSE", font=(font, font_size), command=pickBoard(level="gcse"))
    gcse.place(x=100, y=300)
    AS = Button(frame,text="AS", font=(font, font_size), command=pickBoard(level="AS"))
    AS.place(x=800, y=300)
    a_level = Button(frame,text="A-level", font=(font, font_size), command=pickBoard(level="A-level"))
    a_level.place(x=1600, y=300)


def pickBoard(level):
    frame = cleanScreen()
    # aqa
    aqa_logo = ImageTk.PhotoImage(Image.open('aqa_logo.jpg'))
    aqa_logo_image = Button(frame, image=aqa_logo)
    aqa_logo_image.place(x=710, y=0)

    # edexcel
    edexcel_logo = ImageTk.PhotoImage(Image.open('edexcel_logo.jpg'))
    edexcel_logo_image = Button(frame, image=edexcel_logo)
    edexcel_logo_image.place(x=710, y=300)

    # ocr
    ocr_logo = ImageTk.PhotoImage(Image.open('ocr_logo.jpg'))
    ocr_logo_image = Button(frame, image=ocr_logo)
    ocr_logo_image.place(x=710, y=500)
    pass


def pickSubject(level, board):
    cleanScreen()
    if board == "aqa":
        if level == "gcse":
            pass
        elif level == "AS":
            pass
        elif level == "A-level":
            pass
    elif board == "edexcel":
        if level == "gcse":
            pass
        elif level == "AS":
            pass
        elif level == "A-level":
            pass
    elif board == "ocr":
        if level == "gcse":
            pass
        elif level == "AS":
            pass
        elif level == "A-level":
            pass


def settings():
    pass


if __name__ == "__main__":
    font_size = 40
    font = "Arial"
    root, frame = setUp(font_size, font)
    pickLevel(font, font_size)
    root.mainloop()

# Buttons: Subject, Exam Board (after clicking Level button), Level (if AS/A level is to be added, button for each),
# Settings Links to exam board-specific text books in every subject, Revision summary for every subject,
# Exam Questions, Spec Subjects: English Lit, Maths, Bio, Chem, Physics, Comp Sci
