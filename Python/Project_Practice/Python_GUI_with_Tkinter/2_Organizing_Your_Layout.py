from tkinter import *

# Basic window
root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button_1 = Button(topFrame, text="Button_1", fg="red")
button_2 = Button(topFrame, text="Button_2", fg="blue")
button_3 = Button(topFrame, text="Button_3", fg="green")
button_4 = Button(bottomFrame, text="Button_4", fg="purple")

button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack(side=BOTTOM)


# Mainloop
root.mainloop()
