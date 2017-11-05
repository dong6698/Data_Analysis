from tkinter import *


def doNothing():
    print("wow,wow, nothing happened!!....")

# Create a blank window
root = Tk()

# Create a main blank menu bar on the top of window
main_menu_bar = Menu(root)
# Use root.config to put the menu bar on the window, like pack()
root.config(menu=main_menu_bar)
# Create a file submenu on the main_menu
fileMenu = Menu(main_menu_bar)
# Use main_menu.add_cascade to config the submenu name and filemenu
main_menu_bar.add_cascade(label="File", menu=fileMenu)
# add submenu content of fileMenu
fileMenu.add_command(label="File_1", command=doNothing)
fileMenu.add_command(label="File_2", command=doNothing)
# This is a separator line of the submenu.
fileMenu.add_separator()
fileMenu_File_3 = Menu(fileMenu)
fileMenu.add_cascade(label="File_3", menu=fileMenu_File_3)
fileMenu_File_3.add_command(label="File_3_1")
fileMenu_File_3.add_command(label="File_3_2")
fileMenu_File_3.add_command(label="File_3_3")
fileMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(main_menu_bar)
main_menu_bar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Edit_1")

root.mainloop()
