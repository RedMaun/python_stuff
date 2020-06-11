import random
import sys
from tkinter import Tk, Canvas, Frame, BOTH

player_pos = [0,0]
master = Tk()
square = []

def check(c, a, j, h):
    for i in range(0, len(c)):
        if abs(a - c[i][j]) < h:
            return False
    return True

def randd(n,r,h):
    if r/h <= n:
        return "error"
    c =[]
    for  i in range(0, n):
        if i == 0:
            a = random.randint(0,r)
            b = random.randint(0,r)
            c.append([a,b])
        else:
            a = random.randint(0,r)
            b = random.randint(0,r)
            for g in range(0, len(c)):
                while check(c, a, 0, h) == False:
                    a = random.randint(0,r)
                while check(c, b, 1, h) == False:
                    b = random.randint(0,r)
            c.append([a,b])
    return c

def is_cross(a,b):
    ax1,ay1,ax2,ay2 = a[0],a[1],a[2],a[3]       
    bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]   

    xA = [ax1,ax2]  
    xB = [bx1,bx2]  

    yA = [ay1, ay2]  
    yB = [by1, by2]  

    if max(xA)<min(xB) or min(xA) > max(xB) or max(yA) < min(yB) or min(yA) > max(yB):
        return False    

    elif max(xA)>min(xB) and min(xA)<min(xB):
        dx = max(xA)-min(xB)
        return True     
    else:
        return True    

def check_move():
    for i in square:
        if is_cross(canvas.coords(player), canvas.coords(i)) == True:
            canvas.itemconfig(i, fill='#2f3333')

def key_pressed(event):
    if event.char == 'w':
        canvas.move(player, 0, -10)
    if event.char == 'a':
        canvas.move(player, -10, 0)
    if event.char == 'd':
        canvas.move(player, 10, 0)
    if event.char == 's':
        canvas.move(player, 0, 10)
    check_move()

if len(sys.argv) == 1:
    col = 30
    ras = 500
    gaps = 10
else:
    col = int(sys.argv[1])
    ras = int(sys.argv[2])
    gaps = int(sys.argv[3])

b = randd(col, ras, gaps)
master.bind("<KeyPress>", key_pressed)
canvas = Canvas(master, bg="#1e1e1e", height=ras, width=ras)
player = canvas.create_rectangle(player_pos[0], player_pos[1], player_pos[0]+10, player_pos[1]+10, fill="#ff00ff")
canvas.pack()
for i in range(0, len(b)):
    square.append(canvas.create_rectangle(b[i][0], b[i][1], b[i][0]+10, b[i][1]+10, fill="#bcecff"))
    canvas.pack()
master.mainloop()