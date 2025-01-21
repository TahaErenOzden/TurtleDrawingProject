import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Square Python Turtle")
#first turtle
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
#second turtle
turtle_instance2 = turtle.Turtle()
turtle_instance2.left(90)
turtle_instance2.forward(100)
#third turtle
turtle_instance3 = turtle.Turtle()
turtle_instance3.left(90)
turtle_instance3.forward(100)
turtle_instance3.left(270)
turtle_instance3.forward(100)
#fourth turtle
turtle_instance4 = turtle.Turtle()
turtle_instance4.left(90)
turtle_instance4.forward(100)
turtle_instance4.left(270)
turtle_instance4.forward(100)
turtle_instance4.left(270)
turtle_instance4.forward(100)

turtle.done()