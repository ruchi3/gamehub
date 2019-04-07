import tkinter
import sys
import os
from tkinter import *
from tkinter import messagebox
top = tkinter.Tk()
titleLabel=Label(top,text='GAME HUB',font=('Times New Roman',50))
def callPacman():
    os.system('python pacman.py')
def callSnake():
    os.system('python snake.py')
def callGuess():
    os.system('python guess.py')

A = tkinter.Button(top, text ="Pacman", command = callPacman)
C = tkinter.Button(top, text ="Snake Around", command = callSnake)
E = tkinter.Button(top, text ="Guess the number", command = callGuess)
titleLabel.pack()
A.pack()
C.pack()
E.pack()
top.mainloop()
