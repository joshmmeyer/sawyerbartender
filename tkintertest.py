from tkinter import *
root = Tk()
recipe=0

def recipe1():
    global recipe
    recipe = 1
    root.quit()

def recipe2():
    global recipe
    recipe = 2
    root.quit()

def printVariable():
    print(variable)

button1 = Button(root, text="Screwdriver", font = ('Helvetica', '100'), command = recipe1)
button1.pack()
button2 = Button(root, text="Rum and Coke", font = ('Helvetica', '100'), command = recipe2)
button2.pack()

button3 = Button(root, text="Quit", font = ('Helvetica', '100'), command = root.quit)
button3.pack()

root.mainloop()
print(recipe)