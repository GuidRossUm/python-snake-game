import turtle
import  random
w = 500
h = 500
fs = 10
d = 100

sozluk = { #(yukarı(0,20), aşagı(0,20), sol(-20,0), sağ(20,0))
    "up":(0,15),
    "down":(0, -15),
    "left":(-20,0),
    "right":(20,0)
}
#yılan işlevi
def run():
    global  saap, kata, khanat, pen
    saap = [[0,0], [0,20], [0,40], [0,60], [0,80]]#liste
    kata = "up"
    khanat = nun()
    food.goto(khanat)
    hall()

def hall():
    global kata

    new_head = saap[-1].copy()
    new_head[0] = saap[-1][0] + sozluk[kata][0]
    new_head[1] = saap[-1][1] + sozluk[kata][1]
    if new_head in saap[:-1]:

        run()
    else:
        saap.append(new_head)
        if not khana():
            saap.pop(0)

        if saap[-1][0] > w / 2:
            saap[-1][0] -= w
        elif saap[1][0] < - w / 2:
            saap[-1][0] += w
        elif saap[-1][1] > h / 2:
            saap[-1][1] -= h
        elif saap[-1][1] < -h / 2:
            saap[-1][1] += h

        pen.clearstamps()
        for segment in saap:
            pen.goto(segment[0] , segment[1])
            pen.stamp()
        screen.update()
        turtle.ontimer(hall , d)

# yemek kodlama bölümü
def khana():
    global khanat
    if dist(saap[-1], khanat) < 20:
        khanat = nun()
        food.goto(khanat)
        return True
    return  True
def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)# yemek konumu
    y = random.randint(- h / 2 + fs, h / 2 - fs)# yemek konumu
    return  (x, y)
#mesafe zaman ayarı
def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2- y1) ** 2 + (x2 -x1) **2) ** 0.5
    return  distance
#yılan haraketleri
def mathi():
    global  kata
    if kata != "down":
        kata = "up"
def go_right():
    global  kata
    if kata != "left":
        kata = "right"
def go_down():
    global  kata
    if kata != "up":
        kata = "down"

def go_left():
    global  kata
    if kata != "right":
        kata = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("saap")
screen.bgcolor("red")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(fs / 20)
food.penup()

screen.listen()
screen.onkey(mathi, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

run()
turtle.done()














