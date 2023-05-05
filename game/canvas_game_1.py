from tkinter import *
from PIL import ImageTk, Image


app = Tk()
canvas = Canvas(app, width=800, height=500)
canvas.pack()
app.bind()
app.title('Run away game version 1.2.0')

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
