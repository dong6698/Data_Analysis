from tkinter import *


def doNothing():
    print("Click tool bar but do nothing!!")


root = Tk()
toolBar = Frame(root, bg="red")
button_1 = Button(toolBar, text="Button_1", command=doNothing)
button_1.pack(side=LEFT, padx=2, pady=2)
button_2 = Button(toolBar, text="Button_2", command=doNothing)
button_2.pack(side=LEFT, padx=2, pady=2)

toolBar.pack(side=TOP, fill=X)

root.mainloop()