from tkinter import *


def doNothing():
    print("Click tool bar but do nothing!!")


root = Tk()
# ********** Tool Bar ************* #
toolBar = Frame(root, bg="red")
button_1 = Button(toolBar, text="Button_1", command=doNothing)
button_1.pack(side=LEFT, padx=2, pady=2)
button_2 = Button(toolBar, text="Button_2", command=doNothing)
button_2.pack(side=LEFT, padx=2, pady=2)
toolBar.pack(side=TOP, fill=X)

# ********** Status Bar ************* #
statusbar = Label(root, text="Prepare to do nothing....", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()