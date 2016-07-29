import time
import winsound
import threading

from tkinter import Frame
from tkinter import Label
from tkinter import StringVar

class Alarm(Frame):
    def __init__(self,parent=None):
        #Frame.__init__(self,parent)
        super(Alarm, self).__init__()
        self.start = "1"
        self.running = False
        self.started = False
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
        if self.seconds <= 0 and self.elapsed_time != 0:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes <=0 and self.elapsed_time !=0:
                self.minutes = 59
                self.hours -= 1
                if self.hours <= 0 and self.elapsed_time !=0:
                    self.hours = 24

        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))

    def setDuration(self):
        '''
        self.hours = self.duration / 3600
        self.minutes = self.duration / 60
        self.seconds = self.duration % 60
        '''
        self.hours = self.duration // (60 * 60)
        self.seconds = self.duration % (60 * 60)
        self.minutes = self.seconds // 60
        self.seconds %= 60
        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))

    def startTimer(self, duration, startbtn, stopbtn, textbox):
        if not self.running:
            self.duration = duration
            self.elapsed_time = duration
            self.setDuration()
            self.update()
            self.running = True
            startbtn.config(text="Resume",state="disabled",command= lambda: self.resume(startbtn,stopbtn))
            stopbtn.config(state="normal")
            textbox.config(state="disabled")

    def resume(self,startbtn,stopbtn):
        if not self.running:
            self.update()
            self.running = True
            startbtn.config(text="Resume",state="disabled")
            stopbtn.config(state="normal")

    def stop(self, startbtn, stopbtn):
        if self.running:
            self.after_cancel(self.timer)
            self.running = False
            startbtn.config(state="normal")
            stopbtn.config(state="disabled")

    def reset(self, startbtn, stopbtn, textbox):
        self.after_cancel(self.timer)
        self.duration = 0
        self.elapsed_time = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.time.set("%d:%d:%d" % (self.hours,self.minutes,self.seconds))
        startbtn.config(text="Start",state="normal", command= lambda: self.startTimer(int(textbox.get()), startbtn, stopbtn, textbox))
        stopbtn.config(state="disabled")
        textbox.config(state="normal")
