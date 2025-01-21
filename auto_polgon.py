import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Automation Python Turtle")

turtle_instance = turtle.Turtle()
choose = input("polgon (p) or star(s) vote = p or s: ")
num_sides = int(input("How many sides? "))
angle = 360.0 / num_sides
angle_star = 360.0 / num_sides *2
side_lenght = int(input("How long side length? :"))

def polgon():
    for i in range(num_sides):
        turtle_instance.right(angle)
        turtle_instance.forward(side_lenght)

def star():
    for i in range(num_sides):
        turtle_instance.right(angle_star)
        turtle_instance.forward(side_lenght)

if choose == "p":
    polgon()
elif choose == "s":
    star()
else:
    print("Invalid choice")

turtle.done()


