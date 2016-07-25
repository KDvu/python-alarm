from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry

root = Tk()
root.title("Alarm Clock")
frame_top = Frame(root,width=100,height=100)
frame_top.pack(side="top")
frame_bot = Frame(root)
frame_bot.pack(side="bottom")

label = Label(frame_bot,text="Set Timer: ")
label.pack(side="left")

text_box = Entry(frame_bot)
text_box.pack(side="right")

root.mainloop()