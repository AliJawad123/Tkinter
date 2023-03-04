# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:03:26 2023

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:15:35 2023

@author: HP
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import pygame
import tkinter as tk
import cv2




songs_list=["Kahani-Suno-2.0(PaglaSongs).mp3","bol-hu.mp3","Baarishein(PaglaSongs).mp3","Rim-Jhim-Yeh-Sawan(PaglaSongs).mp3"]
song_images_list=["6.png","4.png","3.png","5.png"]
current_song=0
########################################
#    Function for commands             #
########################################

def play(song):
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


    
def forward():
    global current_song
    
    current_song += 1
    if current_song >= len(songs_list):
        current_song = 0
    pygame.mixer.music.load(songs_list[current_song])
    pygame.mixer.music.play()
    new_image = tk.PhotoImage(file=song_images_list[current_song])
    Lf2.configure(image=new_image)
    Lf2.image = new_image
    
    #####################


root = ctk.CTk()
root.config(bg="black")
root.geometry("348x500")

########################################
#       Loading the images             #
########################################
image = Image.open("backward.jpg")
background_image = ImageTk.PhotoImage(image)


image2=Image.open("foward.jpg")
background_image2 = ImageTk.PhotoImage(image2)


image3=Image.open("pause.jpg")
background_image3 = ImageTk.PhotoImage(image3)

image4=Image.open("play.jpg")
background_image4 = ImageTk.PhotoImage(image4)

image5=Image.open("Quit.jpg")
background_image5 = ImageTk.PhotoImage(image5)



########################################
#       Loading the SONG images        #
########################################



########################################
#       Storing the SONG images        #
########################################


    



img1=Image.open("421.png")
img1 = img1.resize((200, 200), Image.ANTIALIAS)

img1=ImageTk.PhotoImage(img1)

l1=ctk.CTkLabel(text="    ",master=root,image=img1)
l1.grid(row=0, column=0)

frame = ctk.CTkFrame(master=root,width=0,height=0)
frame.configure(bg_color="black")
frame.grid(row=1, column=0,padx=4)


button1 = ctk.CTkButton(master=frame, text="",image=background_image, width=5, height=0,hover_color=("#2F2F4F"),bg_color="#464682")
button1.grid(row=0, column=1,padx=1,pady=2,)


button2 = ctk.CTkButton(master=frame, text="",image=background_image2,command=forward, width=0, height=0,hover_color=("#2F2F4F"))
button2.grid(row=0, column=3,padx=1,pady=2)

button3 = ctk.CTkButton(master=frame, text="",image=background_image3,command=lambda: play("Kahani-Suno-2.0(PaglaSongs).mp3"), width=0, height=0,hover_color=("red"))
button3.grid(row=0, column=2,padx=1,pady=2)

button4 = ctk.CTkButton(master=frame, text="",image=background_image4, width=0, height=0,hover_color=("#2F2F4F"))
button4.grid(row=0, column=0,padx=1,pady=2)

button5 = ctk.CTkButton(master=frame, text="",image=background_image5, width=0, height=0,hover_color=("#2F2F4F"))
button5.grid(row=0, column=4,padx=1,pady=2)

###################################

frame2 = ctk.CTkFrame(master=root,width=300,height=100)
frame2.grid(row=2, column=0,padx=0,pady=3)


initial_song_image = tk.PhotoImage(file="6.png")
Lf2=ctk.CTkLabel(frame2,image=initial_song_image,text="")
Lf2.grid(row=0,column=0,padx=1,pady=1)






frame3 = ctk.CTkFrame(master=root,width=0,height=0)
frame3.grid(row=3, column=0,padx=0,pady=0)


Lf3=ctk.CTkLabel(frame3,text="",width=10,height=10)
Lf3.grid(row=0,column=0,padx=1,pady=1)

cap = cv2.VideoCapture(0)

def update_video():
    ret, frame = cap.read()
    
    if ret:
        frame = cv2.resize(frame, (300, 200))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        Lf3.configure(image=photo)
        Lf3.image = photo
    root.after(10, update_video)

update_video()
###################################
root.mainloop()