from tkinter import *
import random, time

#func = "sin(x)"
func = input("f(x) = ")

foo_s = "from math import *\n" +\
	"\n\ndef f(x):\n\ttry:\n\n\t\treturn " + func +\
	"\n\texcept ZeroDivisionError:\n\t\treturn None"

open("foo.py","w").write(foo_s)


import foo

#WIDTH = int(input("Width: "))
WIDTH = 1000
#HEIGHT = int(input("Height: "))
HEIGHT = 480
#SCALE = int(input("Scale: "))
SCALE = 30


def color():
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


def Build():
	print("Build")


def Clean():
	canvas.create_rectangle(0, 0, WIDTH+2, HEIGHT+2, fill="#ffffff")
	drawLines()


root = Tk()
root.title("Построение графиков")

menu = Menu(root)
root.config(menu=menu)

menu.add_command(label="Build", command=Build)
menu.add_command(label="Clean", command=Clean)

canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg="#ffffff")


def getMin():
	if SCALE in range(0, 40):
		return 1
	if SCALE in range(40, 70):
		return 5
	return 10


def drawLines():
	minCol = getMin()

	for x in range((WIDTH//2)%(SCALE//minCol), WIDTH, SCALE//minCol):
		canvas.create_line(x, 0, x, HEIGHT, fill = "#eeeeee") if x > 0 else 0

	for y in range((HEIGHT//2)%(SCALE//minCol), HEIGHT, SCALE//minCol):
		canvas.create_line(0, y, WIDTH, y, fill = "#eeeeee") if y > 0 else 0

	for x in range((WIDTH//2)%SCALE, WIDTH, SCALE):
		canvas.create_line(x, 0, x, HEIGHT, fill = "#bbbbbb") if x > 0 else 0

	for y in range((HEIGHT//2)%SCALE, HEIGHT, SCALE):
		canvas.create_line(0, y, WIDTH, y, fill = "#bbbbbb") if y > 0 else 0

	canvas.create_line(WIDTH / 2, HEIGHT, WIDTH / 2, 0, arrow = LAST, fill="#555555")
	canvas.create_line(0, HEIGHT / 2, WIDTH, HEIGHT / 2, arrow = LAST, fill="#555555")



def go(func, f=False):

	lastY = 0

	for x in range(0, WIDTH, 1):
		y = func((x - WIDTH / 2) / SCALE)
		if y == None:
			lastY = None
			continue
		y = HEIGHT / 2 - y * SCALE
		try:
			y = round(y)
		except TypeError:
			lastY = None
			continue

		col = '#000000' #color()

		if lastY != None:
			canvas.create_line(x - 1, lastY, x, y, fill = col, width=2)

		lastY = y

		#time.sleep(0)
		if f:
			root.update()


def resizePlus(e):
	global SCALE, WIDTH, HEIGHT, canvas
	canvas.create_rectangle(0, 0, WIDTH+2, HEIGHT+2, fill="#ffffff")
	SCALE += 10 if SCALE < HEIGHT // 2 else 0
	drawLines()
	go(foo.f)


def resizeMinus(e):
	global SCALE, WIDTH, HEIGHT, canvas
	canvas.create_rectangle(0, 0, WIDTH+2, HEIGHT+2, fill="#ffffff")
	SCALE -= 10 if SCALE > 10 else 0
	drawLines()
	go(foo.f)


def resizeZero(e):
	global SCALE, WIDTH, HEIGHT, canvas
	canvas.create_rectangle(0, 0, WIDTH+2, HEIGHT+2, fill="#ffffff")
	SCALE = 30
	drawLines()
	go(foo.f)




root.bind('<Control-=>', resizePlus)
root.bind('<Control-Key-->', resizeMinus)
root.bind('<Control-0>', resizeZero)


canvas.pack()





drawLines()
go(foo.f, True)





def close():
    root.destroy()
    root.quit()

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()
