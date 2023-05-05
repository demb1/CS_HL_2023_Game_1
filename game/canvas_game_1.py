import random
from tkinter import *
from PIL import ImageTk, Image
from time import *

app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.2.0')

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
shoot1 = canvas.create_image(g1, 112, image=shoot_img)
shoot2 = canvas.create_image(g2, 162, image=shoot_img)
shoot3 = canvas.create_image(g3, 212, image=shoot_img)
shoot4 = canvas.create_image(g4, 262, image=shoot_img)
shoot5 = canvas.create_image(g5, 312, image=shoot_img)
shoot6 = canvas.create_image(g6, 362, image=shoot_img)
shoot7 = canvas.create_image(g7, 412, image=shoot_img)
shoot8 = canvas.create_image(g8, 462, image=shoot_img)
shoot9 = canvas.create_image(g9, 62, image=shoot_img)

# shoots vertical
shoot = Image.open("shoot_vertical.png")
resize_shoot_vertical = shoot.resize((24, 34))
shoot_vertical_img = ImageTk.PhotoImage(resize_shoot_vertical)
shootv1 = canvas.create_image(83, c1, image=shoot_vertical_img)
shootv2 = canvas.create_image(143, c2, image=shoot_vertical_img)
shootv3 = canvas.create_image(203, c3, image=shoot_vertical_img)
shootv4 = canvas.create_image(263, c4, image=shoot_vertical_img)
shootv5 = canvas.create_image(323, c5, image=shoot_vertical_img)
shootv6 = canvas.create_image(383, c6, image=shoot_vertical_img)
shootv7 = canvas.create_image(443, c7, image=shoot_vertical_img)
shootv8 = canvas.create_image(503, c8, image=shoot_vertical_img)
shootv9 = canvas.create_image(563, c9, image=shoot_vertical_img)
shootv10 = canvas.create_image(623, c10, image=shoot_vertical_img)
shootv11 = canvas.create_image(683, c11, image=shoot_vertical_img)
shootv12 = canvas.create_image(743, c12, image=shoot_vertical_img)

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

def check_collision():
    hearts_num = 5
    hearts_label = Label(app, text="0")
    hearts_label.config(text=hearts_num)
    hearts_label.place(x=55, y=10)
    if hearts_num == 0:
        canvas.create_text(400, 250, text="GAME OVER", fill="red", font=('Helvetica 50 bold'))
        sleep(20)
        print(timer_label)
        exit()
    if canvas.coords(hero)[0] == canvas.coords(shoot1)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot2)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot3)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot4)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot5)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot6)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot7)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot8)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot9)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[0] == canvas.coords(shoot1)[2]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv1)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv2)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv3)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv4)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv5)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv6)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv7)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv8)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv9)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv10)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv11)[3]:
        hearts_num -= 1
    if canvas.coords(hero)[1] == canvas.coords(shootv12)[3]:
        hearts_num -= 1
    canvas.after(1, check_collision())


# hero
image = Image.open("mario.png")
resize_hero = image.resize((50, 50))
mario_img = ImageTk.PhotoImage(resize_hero)
hero = canvas.create_image(400, 250, image=mario_img)

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

# hero moving
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
