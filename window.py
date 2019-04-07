import tkinter
import sys
import os
from tkinter import *
from tkinter import messagebox
top = tkinter.Tk()
titleLabel=Label(top,text='GAME HUB',font=('Times New Roman',50))
def callPacman():
    os.system('python pacman.py')
def callFlappy():
    os.system('python flappy.py')
def callSnake():
    os.system('python snake.py')
def callMemory():
    os.system('python memory.py')
def callGuess():
    os.system('python guess.py')

A = tkinter.Button(top, text ="Pacman", command = callPacman)
B = tkinter.Button(top, text ="Flappy Bird", command = callFlappy)
C = tkinter.Button(top, text ="Snake Around", command = callSnake)
D = tkinter.Button(top, text ="Memory Game", command = callMemory)
E = tkinter.Button(top, text ="Guess the number", command = callGuess)
titleLabel.pack()
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
top.mainloop()