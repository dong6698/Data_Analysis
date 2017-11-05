from tkinter import *


root = Tk()


def leftClick(event):
    print("Left click")

def middleClick(event):
    print("Middle click")

def rightClick(event):
    print("Right click")

'''
<Button-1> = Left Click
<Button-2> = Middle Click
<Button-3> = Right Click
'''
frame = Frame(root, width=300, height=200)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()