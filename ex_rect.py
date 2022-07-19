#import turtle

#tw = turtle.Screen()

def rect():
  player = turtle.Turtle()

  #player.shape('square')

  player.color("green")
  player.width(4)

  player.pendown()

  player.forward(150)
  player.left(90)
  player.forward(100)
  player.left(90)
  player.forward(150)
  player.left(90)
  player.forward(100)
  player.left(90)
  player.hideturtle()
