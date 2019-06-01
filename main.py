from tkinter import *
from pygame import mixer

# Initializes Mixer and Starts Background Music
mixer.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play()

# Sets up Window
root = Tk()
root.geometry('500x500')  # 200 is the center for some reason
root.title("Shopping List")
root.iconbitmap(r'listicon.ico')


class ButtonAction():
    def AddItem():
        # Function that will eventually add items, doesn't yet
        print("Hello")

    def Pause():
        # Drops volue to zero "Pauses the music"
        # Changes icons
        mixer.music.set_volume(0)
        PauseSound.place_forget()
        ResumeSound.place(x=0, y=0)

    def Unpause():
        # Brings the music back fully
        # Changes icons
        mixer.music.set_volume(1)
        ResumeSound.place_forget()
        PauseSound.place(x=0, y=0)


# Puts text at the top of the screen as a welcome message
Welcome = Label(root, text='Welcome to my shopping list')
Welcome.pack()

# Inserts add image and makes it call the AddItem function when clicked
AddItemImg = PhotoImage(file='plus.png')
Addbtn = Button(root, image=AddItemImg, command=ButtonAction.AddItem)
Addbtn.place(x=200, y=125)

# Shows the without sound button, resumes sound when clicked
WithoutSound = PhotoImage(file='nosound.png')
ResumeSound = Button(root, image=WithoutSound, command=ButtonAction.Unpause)

# Shows the with sound button, mutes when clicked
WithSound = PhotoImage(file='sound.png')
PauseSound = Button(root, image=WithSound, command=ButtonAction.Pause)
PauseSound.place(x=0, y=0)

# Loops everything in the window to keep it available
root.mainloop()
