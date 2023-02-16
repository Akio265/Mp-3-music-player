import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


musicplayer = tkr.Tk()
musicplayer.title("AKIO")
musicplayer.geometry("500x720")
p=False

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir(directory)
var = tkr.StringVar()

playlist = tkr.Listbox(musicplayer, font ="Roboto 15", bg= "black",fg="white",selectbackground="white",selectforeground="black",selectmode= tkr.SINGLE)
pos = 0
for item in songlist:
    playlist.insert(pos, item)
    pos = pos + 1

print(pos)

pygame.init()
pygame.mixer.init()

def play():
    song=playlist.get(tkr.ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def exitmusicplayer():
    pygame.mixer.music.stop()

def pause():
    global p
    if p==False:
        pygame.mixer.music.pause()
        p=True
    else:
        pygame.mixer.music.unpause()
        p=False

def next():
    next_song =playlist.curselection()
    next_song=next_song[0]+1
    song=playlist.get(next_song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    playlist.selection_clear(0,tkr.END)
    playlist.activate(next_song)
    playlist.selection_set(next_song, last=None)

def Previous():
    previous_song=playlist.curselection()
    previous_one=previous_song[0]-1
    song=playlist.get(previous_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    playlist.selection_clear(0,tkr.END)
    playlist.activate(previous_one)
    playlist.selection_set(previous_one)
 


Button1 = tkr.Button(musicplayer,width=5,height=3, font="Roboto 10",text="PLAY",command=play,bg="red",fg="white")
Button2 = tkr.Button(musicplayer,width=5,height=3, font="Roboto 10",text="PAUSE / UNPAUSE",command=pause,bg="blue",fg="white")
Button3 = tkr.Button(musicplayer,width=5,height=3, font="Roboto 10",text="NEXT",command=next,bg="green",fg="white")
Button4 = tkr.Button(musicplayer,width=5,height=3, font="Roberto 10",text="PREVIOUS",command=Previous,bg="brown",fg="white")
Button5 = tkr.Button(musicplayer,width=5,height=3, font="Roboto 10",text="STOP",command=exitmusicplayer,bg="black",fg="white")


playlist.pack(fill="both",expand="yes")
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")







musicplayer.mainloop()
