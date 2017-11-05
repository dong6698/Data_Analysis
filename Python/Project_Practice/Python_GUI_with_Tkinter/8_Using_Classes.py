from tkinter import *


class DongsButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printMessageButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printMessageButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, It works!!")


root = Tk()
b = DongsButtons(root)
root.mainloop()
