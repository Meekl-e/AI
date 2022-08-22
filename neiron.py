from tkinter import *
import time
import random

finishX = 240
finishY = 30

def ClearAll():
    with open("ProgramsFinal.txt", "w", encoding="UTF-8") as file:
        file.close()
    with open("points.txt", "w", encoding="UTF-8") as file:
        file.write("0")
        file.close()
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
                    with open("ProgramsFinal.txt", "w", encoding="UTF-8") as file:
                        for p in programsFinal:
                            file.write(p +"\n")
                break
        elif canvas.coords(player)[0] <=0 :
            points -= 100

        elif canvas.coords(player)[2] >=300:
            points -= 100

        elif canvas.coords(player)[1] >=300:
            points -=100

        elif canvas.coords(player)[3] <=0:
            points -=100

        #xFinish1-=1
        #xFinish2-=1
        canvas.coords(finish, xFinish1, yFinish, xFinish2, yFinish2)
        root.update()
        if learningInt.get() == 0:
            time.sleep(0.05)
        points -= 1
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
    if demonstrationInt.get() == 1:
        num = 6
    if len(programsFinal) <= i+1:
        num = 5
    if num % 5 == 0:
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

demonstrationInt = IntVar()
learningInt = IntVar()

settings = LabelFrame(root, height=30)
demonstrTk = Checkbutton(settings, text="Демонстрация",  font=('Arial',10,'bold'),
                     bg='whitesmoke', variable=demonstrationInt, onvalue=1,offvalue=0)


learningTk = Checkbutton(settings, text="Обучение",  font=('Arial',10,'bold'),
                     bg='whitesmoke', variable=learningInt, onvalue=1,offvalue=0)

clearBtn = Button(settings, text="Очистить", font=('Arial',10,'bold'),
                     bg='whitesmoke', command=ClearAll)

demonstrTk.pack(side=LEFT)
learningTk.pack(side=LEFT)
clearBtn.pack(side=LEFT)

settings.pack(anchor=W)

demonstrTk.pack()
canvas = Canvas(root, height=270, width=300, bg="whitesmoke",highlightthickness=0)
canvas.pack()

xFinish1 = finishX - 20
xFinish2 = finishX + 20
yFinish = finishY - 20
yFinish2 = finishY + 20
points = 1000
pointsOld = 0
programs = []
programsFinal = []
try:
    open("ProgramsFinal.txt", "x", encoding="UTF-8")
    file = open("points.txt", "x", encoding="UTF-8")
    file.write("0")
except FileExistsError:
    e = 1

with open("ProgramsFinal.txt", "r", encoding="UTF-8") as file:
    listProgrmas = file.readlines()
    for p in listProgrmas:
        programsFinal.append(p.strip())
with open("points.txt","r", encoding="UTF-8") as file:
    pointsOld = int(file.readline())


player = canvas.create_rectangle(145, 230, 155,240, fill="green")

finish = canvas.create_rectangle(xFinish1,yFinish,xFinish2,yFinish2,fill="gold", width=5, outline="gold")

root.bind("<KeyPress>", binds)
Loop()