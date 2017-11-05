from tkinter import *


root = Tk()

photo = PhotoImage(file="cats.png")
label = Label(root, Image=photo)
label.pack()


root.mainloop()