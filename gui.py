import os
import tkinter as tk


def hello():
    print("Hello World")


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=300,height=300)
    root.resizable(width=False,height=False)
    helloCommand= lambda : hello()
    panel = tk.Label(root)
    panel.pack(side="top", fill="both", expand="yes")

    play = tk.Button(root,command=helloCommand,text="hello")

    play.pack()

    root.mainloop()