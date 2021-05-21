from turtle import Screen, Turtle
import colorgram
import random



# timmy.colormode(255)
screen = Screen()


# colors = colorgram.extract("damienhirst.jpg", 30)

# first_color = colors[0]
# rgb = first_color.rgb



# final_color = []

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color = (r, g, b)
#
#     final_color.append(color)
#
# print(final_color)
# color_list = [(197, 13, 32), (249, 237, 21), (40, 76, 188), (39, 216, 69), (238, 227, 5), (228, 160, 48),
#               (244, 247, 253), (28, 40, 155), (213, 75, 13), (16, 153, 16), (198, 15, 11), (242, 34, 163),
#               (226, 19, 121), (75, 9, 31), (59, 15, 9), (224, 141, 208), (11, 97, 62), (220, 158, 10), (18, 18, 42),
#               (49, 212, 232), (238, 156, 218), (11, 228, 239), (80, 74, 213), (75, 211, 166), (83, 234, 199),
#               (58, 232, 241), (5, 67, 42)]
# timmy.speed("fastest")
# timmy.hideturtle()
# timmy.penup()

# for i in range(10):
#     for k in range(10):
#         color = random.choice(color_list)
#         timmy.dot(7, color)
#         timmy.forward(10)
#
#     timmy.backward(100)
#     timmy.right(90)
#     timmy.forward(10)
#     timmy.left(90)

#
# timmy.setheading(225)
# timmy.forward(300)
# timmy.setheading(0)
# times = 100
#
# for dot in range(1, times + 1):
#     color = random.choice(color_list)
#     timmy.dot(20, color)
#     timmy.forward(50)
#
#     if dot % 10 == 0:
#         timmy.back(50 * 10)
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(0)
#


""""Creating events listeners """

#
# def move_fd():
#     timmy.forward(20)
#
#
# def move_back():
#     timmy.back(20)
#
#
# def clockwise():
#     new_dir = timmy.heading() + 30
#     timmy.setheading(new_dir)
#
#
# def c_clockwise():
#     timmy.left(20)
#
#
# def clear():
#     screen.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_fd)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=c_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)

'''Turtle racing game '''


screen.setup(width=500, height=400)
guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
pos = 0
my_turtles = []
is_game_on = False

for item in colors:
    turtle_n = Turtle(shape="turtle")
    turtle_n.color(item)
    turtle_n.penup()
    pos += 40
    turtle_n.goto(x=-235, y=-130 + pos)
    my_turtles.append(turtle_n)



if guess:
    is_game_on = True

while is_game_on:
    for turtle in my_turtles:

        if turtle.xcor() > 230:
            is_game_on = False
            winner = turtle.pencolor()
            if winner == guess:
                print(f"You've Won! The {winner} turtle is the winner ")
            else:
                print(f"You've Lost! The {winner} turtle is the winner ")

        distance = random.randint(0, 20)
        turtle.forward(distance)


""""Inherinting classes"""
#
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water.")
#
# nemo = Fish()
# nemo.breathe()


screen.exitonclick()