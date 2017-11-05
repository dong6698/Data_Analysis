from tkinter import *
import tkinter.messagebox


def showMessage_1():
    tkinter.messagebox.showinfo('ShowInfo', 'This Message Box Just Show Information!')

def showMessage_2():
    answer = tkinter.messagebox.askquestion('askQuestion', 'Do You Like Me?')
    if answer == 'yes':
        print('Thanks i like you too.')
    else:
        print('Fuck off man !')

def showMessage_3():
    option = tkinter.messagebox.askyesnocancel('askYesNoCancel', 'Choose Yes Or No Or Cancel.')
    # print(option)
    if option is True:
        print('You choose yes!')
    elif option is False:
        print('You choose no!')
    elif option is None:
        print('You choose cancel!')

def showMessage_4():
    option = tkinter.messagebox.askokcancel('asOkCancel', 'Do you wanna quit?')
    print(option)
    if option is True:
        root.quit()

root = Tk()

button_1 = Button(root, text="ShowInfo", command=showMessage_1)
button_1.pack(fill=X)
button_2 = Button(root, text="askQuestion", command=showMessage_2)
button_2.pack(fill=X)
button_3 = Button(root, text="askYesNoCancel", command=showMessage_3)
button_3.pack(fill=X)
button_4 = Button(root, text="askOkCancel", command=showMessage_4)
button_4.pack(fill=X)

root.mainloop()