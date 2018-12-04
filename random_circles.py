import random, time
from tkinter import *


def randomColor():
	red = hex(round(random.random() * 255))[2:]
	green = hex(round(random.random() * 255))[2:]
	blue = hex(round(random.random() * 255))[2:]
	
	if len(red) < 2:
		red = '0' + red
	if len(green) < 2:
		green = '0' + green
	if len(blue) < 2:
		blue = '0' + blue
	
	return '#' + red + green + blue


def randomXY():
	x = round(random.random() * 600)
	y = round(random.random() * 400)
	return x, y


def randomR():
	r = round(random.random() * 30) + 5
	return r


def draw():
	x, y = randomXY()
	r = randomR()
	color = randomColor()

	can.create_arc(x-r, y-r, x+r, y+r,
		style=CHORD,
		start=0,
		extent=359,
		fill = color)


root = Tk()
root.title("Random circles")
can = Canvas(root, width=600, height=400)
can.pack()


for i in range(10):
	draw()
	time.sleep(0.1)


def close():
    root.destroy()
    root.quit()

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()

