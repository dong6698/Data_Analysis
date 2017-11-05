from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenRec = canvas.create_rectangle(25, 25, 130, 50, fill="green")

canvas.delete(redLine)
canvas.delete(blackLine)
#canvas.delete(ALL)

root.mainloop()