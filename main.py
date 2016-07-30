from alarm import Alarm

from tkinter import Tk
from tkinter import Entry
from tkinter import Button

def main():
    root = Tk()

    a = Alarm(root)
    a.pack(side="bottom")

    textbox = Entry(root)
    textbox.pack(side="left")

    start = Button(root, text="Start",command= lambda: a.startTimer(int(textbox.get()), start, stop, textbox))
    start.pack(side="left")
    stop = Button(root, text="Stop",command= lambda: a.stop(start,stop))
    stop.config(state="disabled")
    stop.pack(side="left")
    reset = Button(root, text="Reset", command= lambda: a.reset(start,stop,textbox))
    reset.pack(side="left")

    root.mainloop()

if __name__ == '__main__':
    main()