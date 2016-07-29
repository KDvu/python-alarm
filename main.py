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

    start = Button(root, text="Start",command= lambda: a.startTimer(int(textbox.get())))
    start.pack(side="left")
    stop = Button(root, text="Stop",command=a.stop)
    stop.pack(side="left")
    reset = Button(root, text="Reset", command=a.reset)
    reset.pack(side="left")

    root.mainloop()

if __name__ == '__main__':
    main()