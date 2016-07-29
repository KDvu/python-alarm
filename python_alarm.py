import time
import winsound
import threading
import sys

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar

class Alarm(Frame):
    def __init__(self,parent=None):
        #Frame.__init__(self,parent)
        super(Alarm, self).__init__()
        self.start = "1"
        self.running = False
        self.elapsed_time = 0
        self.time = StringVar()
        self.time.set("0:00")
        self.createTimer()
        self.duration = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def createTimer(self):
        label = Label(self,textvariable=self.time)
        label.pack()

    def update(self):
        self.elapsed_time -=1
        self.seconds -= 1
        self.setTime()
        print(self.time.get())
        self.timer = self.after(1000,self.update)
        time.sleep(0.1)
        if self.elapsed_time == 0:
            #self.time.set("0:0:0")
            self.stop()
            self.alarm = threading.Thread(target=self.soundAlarm)
            self.alarm.start()

    def soundAlarm(self):
        print("WAKE UP")
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

    def setTime(self):
        if self.seconds <= 0:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes <=0:
                self.minutes = 59
                self.hours -= 1
                if self.hours <= 0:
                    self.hours = 24

        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))

    def setDuration(self):
        self.hours = self.duration / 3600
        self.minutes = self.duration / 60
        self.seconds = self.duration % 60
        print(self.seconds)
        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))

    def startTimer(self, duration):
        if not self.running:
            self.duration = duration
            self.elapsed_time = duration
            self.setDuration()
            self.update()
            self.running = True

    def stop(self):
        if self.running:
            self.running = False
            print("Stop")
            self.after_cancel(self.timer)

    def reset(self):
        self.after_cancel(self.timer)
        self.duration = 0
        self.elapsed_time = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))

def main():
    root = Tk()

    a = Alarm(root)
    a.pack(side="bottom")

    textbox = Entry(root)
    textbox.pack(side="left")

    start = Button(root, text="Start",command= lambda: a.startTimer(int(textbox.get())))
    start.pack(side="left")
    stop = Button(root, text="Stop",command=a.stop)
    stop.pack(side="left")
    reset = Button(root, text="Reset", command=a.reset)
    reset.pack(side="left")

    root.mainloop()

if __name__ == '__main__':
    main()

'''
def soundAlarm(duration):
    #self.t
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

def countdown(duration):
    timer = threading.Thread(target=soundAlarm, args=(duration))
    timer.start()

def stop():
    print("stop")
def resume():
    print("resume")

root = Tk()
root.title("Alarm Clock")
frame_top = Frame(root,width=100,height=100)
frame_top.pack(side="top")
frame_bot = Frame(root)
frame_bot.pack(side="bottom")

label = Label(frame_bot,text="Set Timer: ")

label_time = Label(frame_top,text="0:00")
label_time.pack()

textbox = Entry(frame_bot)
textbox.pack(side="left")

submit = Button(frame_bot, text="Set Time", command = lambda: soundAlarm(int(textbox.get())))
#submit = Button(frame_bot, text="Set Time", command = lambda x = textbox.get(): countdown(x))

#submit = Button(frame_bot, text="Set Time", command = countdown)
submit.pack()

stop = Button(frame_bot, text="Stop", command = stop)
stop.pack(side="left")
resume = Button(frame_bot, text="Resume", command = resume)
resume.pack(side="right")

root.mainloop()

#duration = int(input("how long do you want to sleep for?"))
'''