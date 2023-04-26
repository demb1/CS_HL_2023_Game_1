from tkinter import *
from PIL import ImageTk, Image


app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.1.1')

#guns
frameCnt = 3
frames = [PhotoImage(file='gun_gif_1.gif', format='gif -index %i' % i) for i in range(frameCnt)]
frames2 = [PhotoImage(file='gun_gif_2.gif', format='gif -index %i' % i) for i in range(frameCnt)]

def update1(ind):

    frame = frames[ind]
    frame2 = frames2[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    gun_label.configure(image=frame)
    gun2_label.configure(image=frame)
    gun3_label.configure(image=frame)
    gun4_label.configure(image=frame)
    gunHorizontal_label.configure(image=frame2)
    gunHorizontal2_label.configure(image=frame2)
    gunHorizontal3_label.configure(image=frame2)
    gunHorizontal4_label.configure(image=frame2)
    gunHorizontal5_label.configure(image=frame2)
    gunHorizontal6_label.configure(image=frame2)
    app.after(1000, update1, ind)

b = 100
aa = 75

def move_gun():
    global b, aa
    while b < 175:
        b += 5
    while aa < 150:
        aa += 5
    canvas.after(20, move_gun)


canvas.after(20, move_gun)

gun_label = Label(app)
gun_label.pack()
gun_label.place(x=0, y=b)
app.after(0, update1, 0)
gun2_label = Label(app)
gun2_label.pack()
gun2_label.place(x=0, y=b + 100)
app.after(0, update1, 0)
gun3_label = Label(app)
gun3_label.pack()
gun3_label.place(x=0, y=b + 200)
app.after(0, update1, 0)
gun4_label = Label(app)
gun4_label.pack()
gun4_label.place(x=0, y=b + 300)
app.after(0, update1, 0)
gunHorizontal_label = Label(app)
gunHorizontal_label.pack()
gunHorizontal_label.place(x=aa, y=0)
app.after(0, update1, 0)
gunHorizontal2_label = Label(app)
gunHorizontal2_label.pack()
gunHorizontal2_label.place(x=aa + 125, y=0)
app.after(0, update1, 0)
gunHorizontal3_label = Label(app)
gunHorizontal3_label.pack()
gunHorizontal3_label.place(x=aa + 250, y=0)
app.after(0, update1, 0)
gunHorizontal4_label = Label(app)
gunHorizontal4_label.pack()
gunHorizontal4_label.place(x=aa + 375, y=0)
app.after(0, update1, 0)
gunHorizontal5_label = Label(app)
gunHorizontal5_label.pack()
gunHorizontal5_label.place(x=aa + 500, y=0)
app.after(0, update1, 0)
gunHorizontal6_label = Label(app)
gunHorizontal6_label.pack()
gunHorizontal6_label.place(x=aa + 625, y=0)
app.after(0, update1, 0)

#timer
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

#display hearts
heart = Image.open("heart.png")
resize_heart = heart.resize((40, 40))
heart_img = ImageTk.PhotoImage(resize_heart)
heartDisplay = canvas.create_image(25, 25, image=heart_img)

def updateHearts():
    hearts_num = 5
    hearts_label.config(text=hearts_num)
hearts_label = Label(app, text="0")
hearts_label.place(x=55, y=10)

updateHearts()

#hero
image = Image.open("mario.png")
resize_hero = image.resize((50, 50))
mario_img = ImageTk.PhotoImage(resize_hero)
hero = canvas.create_image(400, 250, image=mario_img)
chaser1 = canvas.create_oval(250, 100, 200, 50, tags="chasser", fill="red", outline="yellow")
chaser2 = canvas.create_oval(500, 100, 550, 150, tags="chasser", fill="red", outline="yellow")
chasers = [chaser1, chaser2]

#chasers moving
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
    #check collision with hero
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
    #check collision with hero
    if canvas.coords(hero)[0] - 25 <= rightpos <= canvas.coords(hero)[0] + 25 and \
        canvas.coords(hero)[1] - 25 <= bottompos <= canvas.coords(hero)[1] + 25:
        exit(0)

    canvas.after(20, move_chaser_2)


canvas.after(20, move_chaser_2)

#cords exit rule
def coordsexit():
    if canvas.coords(hero)[0] > 785:
        exit(0)
    elif canvas.coords(hero)[0] < 20:
        exit(0)
    elif canvas.coords(hero)[1] > 480:
        exit(0)
    elif canvas.coords(hero)[1] < 20:
        exit(0)

#hero moving
def anymove(event):
    if event.char == "a":
        canvas.move(hero, -20, 0)
        coordsexit()
    elif event.char == "d":
        canvas.move(hero, 20, 0)
        coordsexit()
    elif event.char == "s":
        canvas.move(hero, 0, 20)
        coordsexit()
    elif event.char == "w":
        canvas.move(hero, 0, -20)
        coordsexit()


app.bind("<Key>", anymove)

# run the app
app.mainloop()
