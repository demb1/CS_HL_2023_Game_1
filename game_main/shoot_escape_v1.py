import random
from tkinter import *
from PIL import ImageTk, Image
from time import *
from math import *

app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game_main version 1.4.0')

# difficulty settings input
print("hard - 1")
print("medium - 2")
print("easy - 3")

# speed and health number
yspeed = int
xspeed = int
hearts_num = 10

# difficulty setting in game_main
x = int(input("Enter your difficulty number: "))
if x == 1:
    yspeed = 2
    xspeed = 2
    hearts_num = 40

if x == 2:
    yspeed = 1.5
    xspeed = 1.5
    hearts_num = 60

if x == 3:
    yspeed = 1.1
    xspeed = 1.1
    hearts_num = 80

# hero
hero = canvas.create_oval(400, 250, 400 + 40, 250 + 40, fill="blue", outline="red")


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


end_time = -1


def start_timer(seconds):
    global end_time
    if seconds == 360:
        exit(0)
    else:
        update_timer(seconds)
        canvas.after(1000, start_timer, seconds+1)
        end_time += 1


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
shoot1 = canvas.create_oval(g1, 100, g1 + 25, 100 + 25, fill="red")
shoot2 = canvas.create_oval(g2, 150, g2 + 25, 150 + 25, fill="red")
shoot3 = canvas.create_oval(g3, 200, g3 + 25, 200 + 25, fill="red")
shoot4 = canvas.create_oval(g4, 250, g4 + 25, 250 + 25, fill="red")
shoot5 = canvas.create_oval(g5, 300, g5 + 25, 300 + 25, fill="red")
shoot6 = canvas.create_oval(g6, 350, g6 + 25, 350 + 25, fill="red")
shoot7 = canvas.create_oval(g7, 400, g7 + 25, 400 + 25, fill="red")
shoot8 = canvas.create_oval(g8, 450, g8 + 25, 450 + 25, fill="red")
shoot9 = canvas.create_oval(g9, 50, g9 + 25, 50 + 25, fill="red")


# shoots vertical
shoot = Image.open("shoot_vertical.png")
resize_shoot_vertical = shoot.resize((24, 34))
shoot_vertical_img = ImageTk.PhotoImage(resize_shoot_vertical)
shootv1 = canvas.create_oval(70, c1, 70 + 25, c1 + 25, fill="red")
shootv2 = canvas.create_oval(130, c2, 130 + 25, c2 + 25, fill="red")
shootv3 = canvas.create_oval(190, c3, 190 + 25, c3 + 25, fill="red")
shootv4 = canvas.create_oval(250, c4, 250 + 25, c4 + 25, fill="red")
shootv5 = canvas.create_oval(310, c5, 310 + 25, c5 + 25, fill="red")
shootv6 = canvas.create_oval(370, c6, 370 + 25, c6 + 25, fill="red")
shootv7 = canvas.create_oval(430, c7, 430 + 25, c7 + 25, fill="red")
shootv8 = canvas.create_oval(490, c8, 490 + 25, c8 + 25, fill="red")
shootv9 = canvas.create_oval(550, c9, 550 + 25, c9 + 25, fill="red")
shootv10 = canvas.create_oval(610, c10, 610 + 25, c10 + 25, fill="red")
shootv11 = canvas.create_oval(670, c11, 670 + 25, c11 + 25, fill="red")
shootv12 = canvas.create_oval(730, c12, 730 + 25, c12 + 25, fill="red")


def move_shoots():
    global pos, yspeed, xspeed, hearts_num
    if canvas.coords(shoot1)[0] > 800:
        canvas.move(shoot1, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot1, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot1)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot1, random.randint(-1800, -900), 0)
    if canvas.coords(shoot2)[0] > 800:
        canvas.move(shoot2, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot2, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot2)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot2, random.randint(-1800, -900), 0)
    if canvas.coords(shoot3)[0] > 800:
        canvas.move(shoot3, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot3, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot1)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot3, random.randint(-1800, -900), 0)
    if canvas.coords(shoot4)[0] > 800:
        canvas.move(shoot4, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot4, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot4)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot4, random.randint(-1800, -900), 0)
    if canvas.coords(shoot5)[0] > 800:
        canvas.move(shoot5, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot5, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot5)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot5, random.randint(-1800, -900), 0)
    if canvas.coords(shoot6)[0] > 800:
        canvas.move(shoot6, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot6, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot6)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot6, 0, random.randint(-1800, -900))
    if canvas.coords(shoot7)[0] > 800:
        canvas.move(shoot7, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot7, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot7)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot7, 0, random.randint(-1800, -900))
    if canvas.coords(shoot8)[0] > 800:
        canvas.move(shoot8, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot8, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot8)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot8, 0, random.randint(-1800, -900))
    if canvas.coords(shoot9)[0] > 800:
        canvas.move(shoot9, random.randint(-1800, -900), 0)
    else:
        canvas.move(shoot9, xspeed, 0)
        x1, y1, x2, y2 = canvas.coords(shoot9)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shoot9, 0, random.randint(-1800, -900))
    if canvas.coords(shootv1)[1] > 500:
        canvas.move(shootv1, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv1, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv1)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv1, 0, random.randint(-1800, -900))
    if canvas.coords(shootv2)[1] > 500:
        canvas.move(shootv2, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv2, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv2)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv2, 0, random.randint(-1800, -900))
    if canvas.coords(shootv3)[1] > 500:
        canvas.move(shootv3, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv3, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv3)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv3, 0, random.randint(-1800, -900))
    if canvas.coords(shootv4)[1] > 500:
        canvas.move(shootv4, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv4, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv4)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv4, 0, random.randint(-1800, -900))
    if canvas.coords(shootv5)[1] > 500:
        canvas.move(shootv5, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv5, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv1)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv5, 0, random.randint(-1800, -900))
    if canvas.coords(shootv6)[1] > 500:
        canvas.move(shootv6, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv6, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv6)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv6, 0, random.randint(-1800, -900))
    if canvas.coords(shootv7)[1] > 500:
        canvas.move(shootv7, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv7, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv7)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv7, 0, random.randint(-1800, -900))
    if canvas.coords(shootv8)[1] > 500:
        canvas.move(shootv8, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv8, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv8)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv8, 0, random.randint(-1800, -900))
    if canvas.coords(shootv9)[1] > 500:
        canvas.move(shootv9, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv9, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv9)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv9, 0, random.randint(-1800, -900))
    if canvas.coords(shootv10)[1] > 500:
        canvas.move(shootv10, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv10, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv10)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv10, 0, random.randint(-1800, -900))
    if canvas.coords(shootv11)[1] > 500:
        canvas.move(shootv11, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv11, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv11)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv11, 0, random.randint(-1800, -900))
    if canvas.coords(shootv12)[1] > 500:
        canvas.move(shootv12, 0, random.randint(-1800, -900))
    else:
        canvas.move(shootv12, 0, yspeed)
        x1, y1, x2, y2 = canvas.coords(shootv12)
        x3 = pos[0]
        y3 = pos[1]
        dx = x1 - x3
        dy = y1 - y3
        if sqrt(dx * dx + dy * dy) < 33:
            hearts_num -= random.randint(1, 10)
            hearts_label.config(text=hearts_num)
            update_hearts()
            canvas.move(shootv12, 0, random.randint(-1800, -900))
    canvas.after(2, move_shoots)


canvas.after(2, move_shoots)


# hearts
def update_hearts():
    global hearts_num, end_time
    if hearts_num <= 0:
        print()
        print("Game over")
        print()
        print("Time played:", end_time, "s")
        sleep(3)
        exit()
    print("The heart number remaining: ", hearts_num)


health = "HP"
health_label = Label(app)
health_label.place(x=43, y=24)
health_label.config(text=health)
hearts_label = Label(app)
hearts_label.place(x=65, y=24)
hearts_label.config(text=hearts_num)


# cords exit rule
def coordsexit():
    if canvas.coords(hero)[0] > 760:
        print(end_time)
        exit(0)
    elif canvas.coords(hero)[0] < 0:
        print(end_time)
        exit(0)
    elif canvas.coords(hero)[1] > 480:
        print(end_time)
        exit(0)
    elif canvas.coords(hero)[1] < 0:
        print(end_time)
        exit(0)


pos = canvas.coords(hero)


# hero movement
def anymove(event):
    global pos
    if event.char == "a":
        canvas.move(hero, -20, 0)
        pos = canvas.coords(hero)
        coordsexit()
    elif event.char == "d":
        canvas.move(hero, 20, 0)
        pos = canvas.coords(hero)
        coordsexit()
    elif event.char == "s":
        canvas.move(hero, 0, 20)
        pos = canvas.coords(hero)
        coordsexit()
    elif event.char == "w":
        canvas.move(hero, 0, -20)
        pos = canvas.coords(hero)
        coordsexit()


app.bind("<Key>", anymove)

# run the app
app.mainloop()
