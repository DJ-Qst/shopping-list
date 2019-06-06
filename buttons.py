from tkinter import *
from pygame import mixer


class Buttons():
    def __init__(self, frame):
        self.frame = frame
        self.Addbtnx = 210
        self.Addbtny = 30
        self.Entryx = 170
        self.Entryy = 25
        self.Savex = self.Addbtnx + 65
        self.Savey = self.Addbtny + 5
        self.Cart = []
        self.NumItems = []

        # Creating the Shopping cart button
        self.AddItemImg = PhotoImage(file='NewItem.png')
        self.Addbtn = Button(self.frame, image=self.AddItemImg,
                             command=self.AddItem, borderwidth=0)
        self.Addbtn.place(x=self.Addbtnx, y=self.Addbtny)

        # Shows when the max items (20) has been reached, in place of the shopping cart
        self.stopimg = PhotoImage(file='stop.png')
        self.stopimgb = Button(self.frame, image=self.stopimg, command=self.AddItem, borderwidth=0)

        # Shows the without sound button, resumes sound when clicked
        self.WithoutSound = PhotoImage(file='nosound.png')
        self.ResumeSound = Button(self.frame, image=self.WithoutSound,
                                  command=self.Unpause, borderwidth=0)

        # Shows the with sound button, mutes when clicked
        self.WithSound = PhotoImage(file='sound.png')
        self.PauseSound = Button(self.frame, image=self.WithSound,
                                 command=self.Pause, borderwidth=0)
        self.PauseSound.place(x=10, y=10)

        # Saves the items
        self.saveimg = PhotoImage(file='save.png')
        self.saveButton = Button(self.frame, image=self.saveimg, command=self.Save, borderwidth=0)
        self.saveButton.place(x=self.Savex, y=self.Savey)

    def AddItem(self):
        # Function that adds items
        if len(self.NumItems) < 20:
            self.Addbtny += 20
            self.Addbtn.place_forget()
            self.saveButton.place_forget()
            self.Addbtn.place(x=self.Addbtnx, y=self.Addbtny)
            self.saveButton.place(x=self.Addbtnx + 65, y=self.Addbtny + 5)
            self.NumItems.append(Entry(self.frame, width=25).place(x=self.Entryx, y=self.Entryy))
            self.Entryy += 20
        if len(self.NumItems) >= 20:
            self.Addbtn.place_forget()
            self.stopimgb.place(x=self.Addbtnx, y=self.Addbtny)
            print("\nI'm sorry, you are at the maximum number of items")

    def Pause(self):
        # Drops volue to zero "Pauses the music"
        # Changes icons
        mixer.music.set_volume(0)
        self.PauseSound.place_forget()
        self.ResumeSound.place(x=10, y=10)

    def Unpause(self):
        # Brings the music back fully
        # Changes icons
        mixer.music.set_volume(1)
        self.ResumeSound.place_forget()
        self.PauseSound.place(x=10, y=10)

    def Save(self):
        try:
            for item in NumItems:
                item = item.get()
                Cart.append(item)
        except NameError:
            print("Sorry, this feature isn't ready yet")
