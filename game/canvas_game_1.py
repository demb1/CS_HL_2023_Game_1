from tkinter import *
from PIL import ImageTk, Image
import os

app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.0.0')

mario_img = ImageTk.PhotoImage(Image.open("mario.png"))
hero = canvas.create_image(400, 250, image=mario_img)
chasser1 = canvas.create_oval(250, 100, 200, 50, tags="chasser", fill="red", outline="yellow")
chasser2 = canvas.create_oval(500, 100, 550, 150, tags="chasser", fill="red", outline="yellow")

xspeed1=-3
yspeed1=3

def move_chasser_1():
    global xspeed1, yspeed1
    canvas.move(chasser1, xspeed1, yspeed1)
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(chasser1)
    if leftpos <= 0 or rightpos >= 800:
        xspeed1 = -xspeed1

    if toppos <= 0 or bottompos >= 500:
        yspeed1 = -yspeed1
    canvas.after(20, move_chasser_1)

canvas.after(20, move_chasser_1)

xspeed2=4
yspeed2=4

def move_chasser_2():
    global xspeed2, yspeed2
    canvas.move(chasser2, xspeed2, yspeed2)
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(chasser2)
    if leftpos <= 0 or rightpos >= 800:
        xspeed2 = -xspeed2

    if toppos <= 0 or bottompos >= 500:
        yspeed2 = -yspeed2
    canvas.after(20, move_chasser_2)

canvas.after(20, move_chasser_2)

def coordsexit():
    if canvas.coords(hero)[0] > 755:
        exit(0)
    elif canvas.coords(hero)[0] < 0:
        exit(0)
    elif canvas.coords(hero)[1] > 455:
        exit(0)
    elif canvas.coords(hero)[1] < 0:
        exit(0)


def anymove(event):
    if event.char == "a":
        canvas.move(hero, -10, 0)
        coordsexit()
    elif event.char == "d":
        canvas.move(hero, 10, 0)
        coordsexit()
    elif event.char == "s":
        canvas.move(hero, 0, 10)
        coordsexit()
    elif event.char == "w":
        canvas.move(hero, 0, -10)
        coordsexit()
    elif event.char == "`":
        canvas.move(hero, -7, 7)
        coordsexit()
    elif event.char == "q":
        canvas.move(hero, -7, -7)
        coordsexit()
    elif event.char == "c":
        canvas.move(hero, 7, 7)
        coordsexit()
    elif event.char == "r":
        canvas.move(hero, 7, -7)
        coordsexit()


app.bind("<Key>", anymove)

# run the app
app.mainloop()
