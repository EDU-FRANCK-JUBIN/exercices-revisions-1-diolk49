import turtle as tu

a = tu.Turtle()

dic = [
  ['black', 0, 0, 80, 80],
  ['red', 20, -40, 40, 40],
]

for t in dic:
	a.speed(20)
	a.up()
	a.setpos(t[1], t[2])

	a.down()

	a.pencolor(t[0])

	a.forward(t[3])
	a.right(90)
	a.forward(t[4])
	a.right(90)
	a.forward(t[3])
	a.right(90)
	a.forward(t[4])
	a.right(90)

a.up()
a.home()

a.left(60)
a.down()
a.pencolor("green")
a.forward(80)
a.right(120)
a.forward(80)


tu.done()
