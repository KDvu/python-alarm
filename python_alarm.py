import time
import winsound
import threading
import sys

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def countdown():
    time.sleep(2)
    print("WAKE UP")
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

def soundAlarm(duration):
    timer = threading.Thread(target=countdown)
    timer.start()

root = Tk()
root.title("Alarm Clock")
frame_top = Frame(root,width=100,height=100)
frame_top.pack(side="top")
frame_bot = Frame(root)
frame_bot.pack(side="bottom")

label = Label(frame_bot,text="Set Timer: ")
label.pack()

textbox = Entry(frame_bot)
textbox.pack(side="left")

submit = Button(frame_bot, text="Set Time", command = lambda: soundAlarm(int(textbox.get())))
submit.pack()

root.mainloop()

#duration = int(input("how long do you want to sleep for?"))



