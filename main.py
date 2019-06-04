from tkinter import *
from pygame import mixer
import json

# Variables
root = Tk()
Addbtnx = 210
Addbtny = 30
Entryx = 170
Entryy = 25
NumItems = []
Cart = []

# Initializes Mixer and Starts Background Music
mixer.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play(loops=-1)

# Sets up Window

root.geometry('500x475')  # 210 is the center for some reason
root.title("Shopping List")
root.iconbitmap(r'listicon.ico')
root.resizable(False, False)


class ButtonAction():
    def AddItem():
        # Function that adds items
        global Addbtny, Entryy, NumItems
        if len(NumItems) < 20:
            Addbtny += 20
            Addbtn.place_forget()
            saveButton.place_forget()
            saveButton.place(x=Addbtnx+65, y=Addbtny+5)
            Addbtn.place(x=Addbtnx, y=Addbtny)
            NumItems.append(Entry(root, width=25).place(x=Entryx, y=Entryy))
            Entryy += 20
        if len(NumItems) >= 20:
            Addbtn.place_forget()
            stopimgb.place(x=Addbtnx, y=Addbtny)
            print("I'm sorry, you are at the maximum number of items\n")

    def Pause():
        # Drops volue to zero "Pauses the music"
        # Changes icons
        mixer.music.set_volume(0)
        PauseSound.place_forget()
        ResumeSound.place(x=10, y=10)

    def Unpause():
        # Brings the music back fully
        # Changes icons
        mixer.music.set_volume(1)
        ResumeSound.place_forget()
        PauseSound.place(x=10, y=10)

    def Save():
        global cart
        for item in NumItems:
            item = item.get()
            Cart.append(item)


# Puts text at the top of the screen as a welcome message
Welcome = Label(root, text='Welcome to my shopping list')
Welcome.pack()

# Inserts add image and makes it call the AddItem function when clicked
AddItemImg = PhotoImage(file='NewItem.png')
Addbtn = Button(root, image=AddItemImg, command=ButtonAction.AddItem, borderwidth=0)
Addbtn.place(x=Addbtnx, y=Addbtny)

# Shows the without sound button, resumes sound when clicked
WithoutSound = PhotoImage(file='nosound.png')
ResumeSound = Button(root, image=WithoutSound, command=ButtonAction.Unpause, borderwidth=0)

# Shows the with sound button, mutes when clicked
WithSound = PhotoImage(file='sound.png')
PauseSound = Button(root, image=WithSound, command=ButtonAction.Pause, borderwidth=0)
PauseSound.place(x=10, y=10)

# Shows when the max items (20) has been reached, in place of the shopping cart
stopimg = PhotoImage(file='stop.png')
stopimgb = Button(root, image=stopimg, command=ButtonAction.AddItem, borderwidth=0)

# Saves the items
saveimg = PhotoImage(file='save.png')
saveButton = Button(root, image=saveimg, command=ButtonAction.Save, borderwidth=0)
saveButton.place(x=Addbtnx+65, y=Addbtny+5)

# Loops everything in the window to keep it available
root.mainloop()
