from tkinter import *
from PIL import Image

ws = Tk()
ws.title('PythonGuides')

# ws.geometry("800x1000")

l = Label(ws, font="bold")
l.pack()

x = 1


def move():
    global x
    if x == 3:
        x = 1
    if x == 1:
        img = PhotoImage(file='./imgs/ant1.png')
        Label(ws, image=img).pack()
    elif x == 2:
        img2 = PhotoImage(file='./imgs/ant2.png')
        Label(ws, image=img2).pack()
    elif x == 3:
        img3 = PhotoImage(file='./imgs/ant3.png')
        Label(ws, image=img3).pack()

    x += 1

    ws.after(2000, move)


move()

ws.mainloop()