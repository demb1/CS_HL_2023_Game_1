import random
from tkinter import *
from PIL import ImageTk, Image
from time import *


app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.2.1')

# hero
image = Image.open("mario.png")
resize_hero = image.resize((50, 50))
mario_img = ImageTk.PhotoImage(resize_hero)
hero = canvas.create_image(400, 250, image=mario_img)


# guns
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
    gun5_label.configure(image=frame)
    gun6_label.configure(image=frame)
    gun7_label.configure(image=frame)
    gun8_label.configure(image=frame)
    gun9_label.configure(image=frame)
    gunHorizontal_label.configure(image=frame2)
    gunHorizontal2_label.configure(image=frame2)
    gunHorizontal3_label.configure(image=frame2)
    gunHorizontal4_label.configure(image=frame2)
    gunHorizontal5_label.configure(image=frame2)
    gunHorizontal6_label.configure(image=frame2)
    gunHorizontal7_label.configure(image=frame2)
    gunHorizontal8_label.configure(image=frame2)
    gunHorizontal9_label.configure(image=frame2)
    gunHorizontal10_label.configure(image=frame2)
    gunHorizontal11_label.configure(image=frame2)
    gunHorizontal12_label.configure(image=frame2)
    app.after(400, update1, ind)


gun_label = Label(app)
gun_label.pack()
gun_label.place(x=0, y=100)
app.after(0, update1, 0)
gun2_label = Label(app)
gun2_label.pack()
gun2_label.place(x=0, y=150)
app.after(0, update1, 0)
gun3_label = Label(app)
gun3_label.pack()
gun3_label.place(x=0, y=200)
app.after(0, update1, 0)
gun4_label = Label(app)
gun4_label.pack()
gun4_label.place(x=0, y=250)
app.after(0, update1, 0)
gun5_label = Label(app)
gun5_label.pack()
gun5_label.place(x=0, y=300)
app.after(0, update1, 0)
gun6_label = Label(app)
gun6_label.pack()
gun6_label.place(x=0, y=350)
app.after(0, update1, 0)
gun7_label = Label(app)
gun7_label.pack()
gun7_label.place(x=0, y=400)
app.after(0, update1, 0)
gun8_label = Label(app)
gun8_label.pack()
gun8_label.place(x=0, y=450)
app.after(0, update1, 0)
gun9_label = Label(app)
gun9_label.pack()
gun9_label.place(x=0, y=50)
gunHorizontal_label = Label(app)
gunHorizontal_label.pack()
gunHorizontal_label.place(x=70, y=0)
app.after(0, update1, 0)
gunHorizontal2_label = Label(app)
gunHorizontal2_label.pack()
gunHorizontal2_label.place(x=130, y=0)
app.after(0, update1, 0)
gunHorizontal3_label = Label(app)
gunHorizontal3_label.pack()
gunHorizontal3_label.place(x=190, y=0)
app.after(0, update1, 0)
gunHorizontal4_label = Label(app)
gunHorizontal4_label.pack()
gunHorizontal4_label.place(x=250, y=0)
app.after(0, update1, 0)
gunHorizontal5_label = Label(app)
gunHorizontal5_label.pack()
gunHorizontal5_label.place(x=310, y=0)
app.after(0, update1, 0)
gunHorizontal6_label = Label(app)
gunHorizontal6_label.pack()
gunHorizontal6_label.place(x=370, y=0)
app.after(0, update1, 0)
gunHorizontal7_label = Label(app)
gunHorizontal7_label.pack()
gunHorizontal7_label.place(x=430, y=0)
app.after(0, update1, 0)
gunHorizontal8_label = Label(app)
gunHorizontal8_label.pack()
gunHorizontal8_label.place(x=490, y=0)
app.after(0, update1, 0)
gunHorizontal9_label = Label(app)
gunHorizontal9_label.pack()
gunHorizontal9_label.place(x=550, y=0)
app.after(0, update1, 0)
gunHorizontal10_label = Label(app)
gunHorizontal10_label.pack()
gunHorizontal10_label.place(x=610, y=0)
app.after(0, update1, 0)
gunHorizontal11_label = Label(app)
gunHorizontal11_label.pack()
gunHorizontal11_label.place(x=670, y=0)
app.after(0, update1, 0)
gunHorizontal12_label = Label(app)
gunHorizontal12_label.pack()
gunHorizontal12_label.place(x=730, y=0)
app.after(0, update1, 0)


# timer
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

# display heart
heart = Image.open("heart.png")
resize_heart = heart.resize((40, 40))
heart_img = ImageTk.PhotoImage(resize_heart)
heartDisplay = canvas.create_image(25, 25, image=heart_img)

# random numbers for horizontal shoot generation
g1 = random.randint(-1000, 0)
g2 = random.randint(-1000, 0)
g3 = random.randint(-1000, 0)
g4 = random.randint(-1000, 0)
g5 = random.randint(-1000, 0)
g6 = random.randint(-1000, 0)
g7 = random.randint(-1000, 0)
g8 = random.randint(-1000, 0)
g9 = random.randint(-1000, 0)

# random number for vertical shoot generation
c1 = random.randint(-800, 0)
c2 = random.randint(-800, 0)
c3 = random.randint(-800, 0)
c4 = random.randint(-800, 0)
c5 = random.randint(-800, 0)
c6 = random.randint(-800, 0)
c7 = random.randint(-800, 0)
c8 = random.randint(-800, 0)
c9 = random.randint(-800, 0)
c10 = random.randint(-800, 0)
c11 = random.randint(-800, 0)
c12 = random.randint(-800, 0)

# shoots horizontal
shoot = Image.open("shoot.png")
resize_shoot = shoot.resize((34, 24))
shoot_img = ImageTk.PhotoImage(resize_shoot)
shoot1 = canvas.create_oval(g1, 112, g1 + 40, 112 + 40, fill="red")
shoot2 = canvas.create_oval(g2, 162, g2 + 40, 162 + 40, fill="red")
shoot3 = canvas.create_oval(g3, 212, g3 + 40, 212 + 40, fill="red")
shoot4 = canvas.create_oval(g4, 262, g4 + 40, 262 + 40, fill="red")
shoot5 = canvas.create_oval(g5, 312, g5 + 40, 312 + 40, fill="red")
shoot6 = canvas.create_oval(g6, 362, g6 + 40, 362 + 40, fill="red")
shoot7 = canvas.create_oval(g7, 412, g7 + 40, 412 + 40, fill="red")
shoot8 = canvas.create_oval(g8, 462, g8 + 40, 462 + 40, fill="red")
shoot9 = canvas.create_oval(g9, 62, g9 + 40, 62 + 40, fill="red")


# shoots vertical
shoot = Image.open("shoot_vertical.png")
resize_shoot_vertical = shoot.resize((24, 34))
shoot_vertical_img = ImageTk.PhotoImage(resize_shoot_vertical)
shootv1 = canvas.create_oval(83, c1, 83 + 40, c1 + 40, fill="red")
shootv2 = canvas.create_oval(143, c2, 143 + 40, c2 + 40, fill="red")
shootv3 = canvas.create_oval(203, c3, 203 + 40, c3 + 40, fill="red")
shootv4 = canvas.create_oval(263, c4, 263 + 40, c4 + 40, fill="red")
shootv5 = canvas.create_oval(323, c5, 323 + 40, c5 + 40, fill="red")
shootv6 = canvas.create_oval(383, c6, 383 + 40, c6 + 40, fill="red")
shootv7 = canvas.create_oval(443, c7, 443 + 40, c7 + 40, fill="red")
shootv8 = canvas.create_oval(503, c8, 503 + 40, c8 + 40, fill="red")
shootv9 = canvas.create_oval(563, c9, 563 + 40, c9 + 40, fill="red")
shootv10 = canvas.create_oval(623, c10, 623 + 40, c10 + 40, fill="red")
shootv11 = canvas.create_oval(683, c11, 683 + 40, c11 + 40, fill="red")
shootv12 = canvas.create_oval(743, c12, 743 + 40, c12 + 40, fill="red")


yspeed = 1
xspeed = 1


def move_shoots():
    global xspeed
    global yspeed
    if canvas.coords(shoot1)[0] > 800:
        canvas.move(shoot1, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot1, xspeed, 0)
    if canvas.coords(shoot2)[0] > 800:
        canvas.move(shoot2, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot2, xspeed, 0)
    if canvas.coords(shoot3)[0] > 800:
        canvas.move(shoot3, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot3, xspeed, 0)
    if canvas.coords(shoot4)[0] > 800:
        canvas.move(shoot4, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot4, xspeed, 0)
    if canvas.coords(shoot5)[0] > 800:
        canvas.move(shoot5, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot5, xspeed, 0)
    if canvas.coords(shoot6)[0] > 800:
        canvas.move(shoot6, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot6, xspeed, 0)
    if canvas.coords(shoot7)[0] > 800:
        canvas.move(shoot7, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot7, xspeed, 0)
    if canvas.coords(shoot8)[0] > 800:
        canvas.move(shoot8, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot8, xspeed, 0)
    if canvas.coords(shoot9)[0] > 800:
        canvas.move(shoot9, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot9, xspeed, 0)
    if canvas.coords(shootv1)[1] > 500:
        canvas.move(shootv1, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv1, 0, yspeed)
    if canvas.coords(shootv2)[1] > 500:
        canvas.move(shootv2, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv2, 0, yspeed)
    if canvas.coords(shootv3)[1] > 500:
        canvas.move(shootv3, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv3, 0, yspeed)
    if canvas.coords(shootv4)[1] > 500:
        canvas.move(shootv4, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv4, 0, yspeed)
    if canvas.coords(shootv5)[1] > 500:
        canvas.move(shootv5, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv5, 0, yspeed)
    if canvas.coords(shootv6)[1] > 500:
        canvas.move(shootv6, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv6, 0, yspeed)
    if canvas.coords(shootv7)[1] > 500:
        canvas.move(shootv7, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv7, 0, yspeed)
    if canvas.coords(shootv8)[1] > 500:
        canvas.move(shootv8, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv8, 0, yspeed)
    if canvas.coords(shootv9)[1] > 500:
        canvas.move(shootv9, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv9, 0, yspeed)
    if canvas.coords(shootv10)[1] > 500:
        canvas.move(shootv10, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv10, 0, yspeed)
    if canvas.coords(shootv11)[1] > 500:
        canvas.move(shootv11, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv11, 0, yspeed)
    if canvas.coords(shootv12)[1] > 500:
        canvas.move(shootv12, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv12, 0, yspeed)
    canvas.after(3, move_shoots)


canvas.after(3, move_shoots)


# hearts
def update_hearts(check):
    global hearts_num
    if hearts_num == 0:
        canvas.create_text(400, 250, text="GAME OVER", fill="red", font=('Helvetica 50 bold'))
        sleep(20)
        print(timer_label)
        exit()
    hearts_num -= 1
    hearts_label.config(text=hearts_num)
    print(hearts_num)


hearts_num = 5
hearts_label = Label(app)
hearts_label.place(x=55, y=10)
hearts_label.config(text=hearts_num)

# collision checker
def collision_checker(check):
    pos = canvas.coords(hero)
    pos_shoot1 = canvas.coords(shoot1)
    if pos_shoot1 in canvas.find_overlapping(pos[0], pos[1], pos[2], pos[3]):
        update_hearts(check)


# cords exit rule
def coordsexit():
    if canvas.coords(hero)[0] > 785:
        exit(0)
    elif canvas.coords(hero)[0] < 20:
        exit(0)
    elif canvas.coords(hero)[1] > 480:
        exit(0)
    elif canvas.coords(hero)[1] < 20:
        exit(0)


# hero movement
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
    collision_checker()


app.bind("<Key>", anymove)

# run the app
app.mainloop()