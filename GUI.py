from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Alarm Clock")
        self.frame_top = Frame(self.root,width=100,height=100)
        self.frame_top.pack(side="top")
        self.frame_bot = Frame(self.root)
        self.frame_bot.pack(side="bottom")

        self.label = Label(self.frame_bot,text="Set Timer: ")
        self.label.pack(side="left")

        self.text_box = Entry(self.frame_bot)
        self.text_box.pack(side="right")

        self.root.mainloop()