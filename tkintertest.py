from Tkinter import *
root = Tk()
root.geometry("520x300")
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
root.title("Sawyer Bartender")
chooseDrink=Label(root, text="Choose a Drink", font=('Helvetica','15'))
#chooseDrink.co
chooseDrink.place(x=187, y=130)
screwdriverPic=PhotoImage(file="ClassicScrewdriver.png")
button1 = Button(root, image=screwdriverPic,height=142,width=140,command = recipe1)

#text="Screwdriver", font = ('Helvetica', '10'),
chooseDrink=Label(root, text="Screwdriver", font=('Helvetica','10'))
#chooseDrink.co
chooseDrink.place(x=35, y=50)
chooseDrink1=Label(root, text="Rum and Coke", font=('Helvetica','10'))
#chooseDrink.co
chooseDrink1.place(x=400, y=50)
chooseDrink2=Label(root, text="Welcome to the Sawyer Bartender!", font=('Helvetica 17 underline'))
#chooseDrink.co
chooseDrink2.place(x=75, y=1)

button1.pack(side=LEFT)
rumandcokePic=PhotoImage(file="CruzanWithCola.png")
button2 = Button(root, image=rumandcokePic, compound=LEFT, height=142,width=140,command = recipe2)
#text="Rum and Coke", font = ('Helvetica', '10')
button2.pack(side=RIGHT)

button3 = Button(root, text="Quit", font = ('Helvetica', '10'), command = root.quit)
button3.pack(side=BOTTOM)

root.mainloop()
print(recipe)
