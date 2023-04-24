from tkinter import *
from PIL import ImageTk, Image

app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.1.1')

def update_timer(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))

def start_timer(seconds):
    if seconds == 360:
        exit(0)
    else:
        update_timer(seconds)
        canvas.after(1000, start_timer, seconds+1)

timer_label = Label(app, text="00:00")
timer_label.place(x=750, y=10)

start_timer(0)

image = Image.open("mario.png")
resize_image = image.resize((50, 50))

mario_img = ImageTk.PhotoImage(resize_image)
hero = canvas.create_image(400, 250, image=mario_img)
chaser1 = canvas.create_oval(250, 100, 200, 50, tags="chasser", fill="red", outline="yellow")
chaser2 = canvas.create_oval(500, 100, 550, 150, tags="chasser", fill="red", outline="yellow")

chasers = [chaser1, chaser2]

xspeed1 = -3
yspeed1 = 3


def move_chaser_1():
    global xspeed1, yspeed1
    canvas.move(chaser1, xspeed1, yspeed1)
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(chaser1)
    if leftpos <= 0 or rightpos >= 800:
        xspeed1 = -xspeed1
    if toppos <= 0 or bottompos >= 500:
        yspeed1 = -yspeed1
    # check collision with hero
    if canvas.coords(hero)[0] - 25 <= rightpos <= canvas.coords(hero)[0] + 25 and \
        canvas.coords(hero)[1] - 25 <= bottompos <= canvas.coords(hero)[1] + 25:
        exit(0)

    canvas.after(20, move_chaser_1)


canvas.after(20, move_chaser_1)

xspeed2 = 4
yspeed2 = 4


def move_chaser_2():
    global xspeed2, yspeed2
    canvas.move(chaser2, xspeed2, yspeed2)
    (leftpos, toppos, rightpos, bottompos) = canvas.coords(chaser2)
    if leftpos <= 0 or rightpos >= 800:
        xspeed2 = -xspeed2
    if toppos <= 0 or bottompos >= 500:
        yspeed2 = -yspeed2
    # check collision with hero
    if canvas.coords(hero)[0] - 25 <= rightpos <= canvas.coords(hero)[0] + 25 and \
        canvas.coords(hero)[1] - 25 <= bottompos <= canvas.coords(hero)[1] + 25:
        exit(0)

    canvas.after(20, move_chaser_2)


canvas.after(20, move_chaser_2)

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


app.bind("<Key>", anymove)

# run the app
app.mainloop()
