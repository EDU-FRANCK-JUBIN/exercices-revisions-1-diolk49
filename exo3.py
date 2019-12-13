import turtle as tu

a = tu.Turtle()

a.speed(20)
a.pensize(3)

def arbre(a, start = (0,0), size = 300, color="brown", leaf_color="green"):
  a.up()
  a.setpos(start)

  a.down()
  a.pencolor(color)
  a.setheading(90)
  a.forward(size)

  roue(a, start=a.pos(), size = size/5, color=leaf_color)

  a.up()
  a.pencolor(color)
  a.setpos(start[0], size/1.5)
  a.setheading(160)
  a.down()
  a.forward(50)

  roue(a, start=a.pos(), size = size/8, color=leaf_color, heading=70)

  a.up()
  a.pencolor(color)
  a.setpos(start[0], size/3)
  a.setheading(160)
  a.down()
  a.forward(50)

  roue(a, start=a.pos(), size = size/8, color=leaf_color, heading=70)

def roue(a, start = (0, 0), size = 50, color="black", heading=0):
  a.setheading(heading)
  a.up()
  a.setpos(start)
  a.down()

  a.pencolor(color)

  for i in range(0, 6):
    if i == 0:
      a.left(30)
    else:
      a.left(60)
    a.forward(size)

  a.left(30)
  for i in range(0, 3):
    a.left(90)
    a.forward(size * 2)
  
    a.up()
    a.left(120)
    a.forward(size)
    a.left(30)
    a.down()

  a.up()

def bike(a, start = (0,0), size=200, color = "black", wheel_color="black"):
  a.setheading(0)

  # first wheel
  print(start)
  roue(a, start=start, size=(size/4), color=wheel_color)
  # second wheel
  a.up()
  a.home()
  start_second_wheel = (start[0] + size, start[1])
  roue(a, start=start_second_wheel, size=(size/4), color=wheel_color)

  a.up()

  # draw bike
  a.pencolor(color)
  a.setpos(start[0], start[1] + size / 4)
  a.left(62.5)
  a.down()
  a.forward(size/2)

  #draw handlebar
  a.right(25)
  lastPos = a.pos()
  a.pencolor("red")
  a.forward(size/6)
  a.setpos(lastPos)

  # draw bike
  a.pencolor(color)
  a.right(37.5)
  a.forward(size/2)

  #draw saddle
  a.left(35)
  lastPos = a.pos()
  a.pencolor("red")
  a.forward(size/6)
  a.left(145)
  a.forward(size/6)
  a.up()
  a.setpos(lastPos)
  a.down()

  # draw bike
  a.pencolor(color)
  a.right(242.5)
  a.forward(size/2)
  a.right(117.5)
  a.forward(size/2)
  a.right(62.5)
  a.forward(size/2)
  a.right(117.5)
  a.forward(size/2)
  a.right(120)
  a.forward(size/2)

arbre(a, start=(500, 0))

bike(a, color="orange", wheel_color="yellow")

roue(a, (20, 240), 30, "blue")
roue(a, (-20, 300), 30, "blue")
roue(a, (60, 310), 30, "blue")
roue(a, (100, 240), 30, "blue")
roue(a, (140, 320), 30, "blue")

tu.done()
