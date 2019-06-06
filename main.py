from tkinter import *
from pygame import mixer
from buttons import Buttons
import json

# Variables
root = Tk()

# Initializes Mixer and Starts Background Music
mixer.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play(loops=-1)

# Sets up Window

root.geometry('500x475')  # 210 is the center for some reason
root.title("Shopping List")
root.iconbitmap(r'listicon.ico')
root.resizable(False, False)


Welcome = Label(root, text='Welcome to my shopping list').pack()

Buttons(root)

# Loops everything in the window to keep it available
root.mainloop()
