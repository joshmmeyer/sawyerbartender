from tkinter import *
root = Tk()
recipe=0

def recipe1():
    global recipe
    recipe = 1

def recipe2():
    global recipe
    recipe = 2

def printVariable():
    print(variable)

button1 = Button(root, text="Screwdriver", command = recipe1)
button1.pack()
button2 = Button(root, text="Rum and Coke", command = recipe2)
button2.pack()

root.mainloop()
print(recipe)