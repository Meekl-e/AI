from tkinter import *
from PIL import ImageGrab
import time
import random

def get_color(coordX, coordY):
    x=canvas.winfo_rootx()+coordX
    y = canvas.winfo_rooty()+coordY
    # x, y = cnvs.winfo_pointerx(), cnvs.winfo_pointery()
    image = ImageGrab.grab((x, y, x+1, y+1)) # 1 pixel image
    return image.getpixel((0, 0))

#def CreateAll():
   # canvas.create_line(130, 290, 130, 150,width=2)
   # canvas.create_line(170, 290, 170, 150,width=2)
   # canvas.create_line(0,110,290,110,width=2)
    #canvas.create_line(0,150, 130, 150,width=2)
    #canvas.create_line(170, 150, 250, 150,width=2)
    #canvas.create_line(1,110,1,150,width=2)
    #canvas.create_line(290, 110, 290,250,width=2 )
    #canvas.create_line(250, 150, 250, 250, width=2)
    #canvas.create_line(130,290,170,290, width=2)


def Loop():
    global points, programs, programsFinal, firstStart, pointsOld, xFinish1,xFinish2,yFinish2,yFinish
    firstStart = True
    step = 0
    while points > 0:
        doNext(step, player)
        step+=1
        if canvas.coords(player)[0] >= xFinish1 and canvas.coords(player)[0] <= xFinish2 :
            if canvas.coords(player)[1] >= yFinish and canvas.coords(player)[1] <= yFinish2:
                if (points > pointsOld):
                    with open("points.txt", "w", encoding="UTF-8") as file:
                        file.write(str(points))
                        pointsOld = points
                    programsFinal.clear()
                    for s in programs:
                        programsFinal.append(s)
                    print(programsFinal)
                    with open("ProgramsFinal.txt", "w", encoding="UTF-8") as file:
                        for p in programsFinal:
                            file.write(p +"\n")
                break
        elif canvas.coords(player)[0] <=0 :
            points -= 10
            canvas.move(player, 5,0)
        elif canvas.coords(player)[2] >=300:
            points -= 10
            canvas.move(player, -5, 0)
        elif canvas.coords(player)[1] >=300:
            points -=10
            canvas.move(player, 0, -5)
        elif canvas.coords(player)[3] <=0:
            points -=10
            canvas.move(player, 0, 5)
        #xFinish1-=1
        #xFinish2-=1
        canvas.coords(finish, xFinish1, yFinish, xFinish2, yFinish2)
        root.update()
        time.sleep(0.05)
        points -= 1
        #print(int(points))
    points = 1000
    #xFinish1 = 250
    #xFinish2 = 270
    #yFinish = 150
    #yFinish2 = 170
    canvas.coords(player,145, 270, 155,280 )
    canvas.coords(finish, xFinish1, yFinish, xFinish2, yFinish2)
    Loop()

def doNext(i, player):
    global firstStart
    if firstStart:
        firstStart = False
        num = 0
        if num == 0:
            p = random.randint(0, 3)
            if p == 0:
                programs.insert(i + 1, "forward")
            if p == 1:
                programs.insert(i + 1, "back")
            if p == 2:
                programs.insert(i + 1, "right")
            if p == 3:
                programs.insert(i + 1, "left")
    if programs[i] == "forward":
        canvas.move(player, 0,-7)
    elif programs[i] == "back":
        canvas.move(player, 0,7)
    elif programs[i] == "right":
        canvas.move(player, 7,0)
    elif programs[i] == "left":
        canvas.move(player, -7,0)
    num = random.randint(1,5)
    if len(programsFinal) <= i+1:
        num = 5
    if num % 6 == 0:
        p = random.randint(0, 3)
        if p == 0:
            programs.insert(i+1, "forward")
        elif p == 1:
            programs.insert(i + 1, "back")
        elif p == 2:
            programs.insert(i+1, "right")
        elif p == 3:
            programs.insert(i+1, "left")
    else:
        #print(programsFinal)
        programs.insert(i+1, programsFinal[i+1])

def binds(event):
    if event.keysym == "w":
        canvas.move(player, 0, -7)
        programs.append("forward")
    if event.keysym == "s":
        canvas.move(player, 0, 7)
        programs.append("back")
    if event.keysym == "d":
        canvas.move(player, 7, 0)
        programs.append("right")
    if event.keysym == "a":
        canvas.move(player, -7, 0)
        programs.append("left")

root = Tk()
root.geometry("300x300")
root.title("Супер лабиринт")
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=300, bg="whitesmoke",highlightthickness=0)
canvas.pack()

xFinish1 = 80
xFinish2 = 100
yFinish = 250
yFinish2 = 270
points = 1000
pointsOld = 0
programs = []
programsFinal = []
with open("ProgramsFinal.txt", "r", encoding="UTF-8") as file:
    listProgrmas = file.readlines()
    for p in listProgrmas:
        programsFinal.append(p.strip())
with open("points.txt","r", encoding="UTF-8") as file:
    pointsOld = int(file.readline())


player = canvas.create_rectangle(145, 270, 155,280, fill="green")

finish = canvas.create_rectangle(xFinish1,yFinish,xFinish2,yFinish2,fill="gold", width=5, outline="gold")

root.bind("<KeyPress>", binds)
Loop()