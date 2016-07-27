import time
import winsound
import threading
import sys

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def soundAlarm():
    #time.sleep(int(textbox.get()))

    duration = int(textbox.get())

    for t in range(duration,-1,-1):
        m, s = divmod(t, 60)

        label_time.config(text="%d:%d" % (m,s))

        #label_time.config(text= t)
        root.update()
        time.sleep(1)

    print(textbox.get())
    print("WAKE UP")
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

def countdown():
    timer = threading.Thread(target=soundAlarm)
    timer.start()

root = Tk()
root.title("Alarm Clock")
frame_top = Frame(root,width=100,height=100)
frame_top.pack(side="top")
frame_bot = Frame(root)
frame_bot.pack(side="bottom")

label = Label(frame_bot,text="Set Timer: ")
label.pack()

label_time = Label(frame_top,text="0:00")
label_time.pack()

textbox = Entry(frame_bot)
textbox.pack(side="left")

#submit = Button(frame_bot, text="Set Time", command = lambda: soundAlarm(int(textbox.get())))
submit = Button(frame_bot, text="Set Time", command = countdown)
submit.pack()

root.mainloop()

#duration = int(input("how long do you want to sleep for?"))



