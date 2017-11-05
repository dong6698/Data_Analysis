from tkinter import *


root = Tk()


# This function for way 1
def printName_1():
    print("Hello my name is Dong")


# This function for way 2
def printName_2(event):
    print("Hello my name is Dong")

# Way 1 to bind function
button_1 = Button(root, text="Print My Name", command=printName_1)
button_1.pack()

# Way 2 to bind function
button_2 = Button(root, text="Left Click Me")
button_2.bind("<Button-1>", printName_2)
button_2.pack()


root.mainloop()