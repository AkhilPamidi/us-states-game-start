from turtle import Turtle
import pandas
import turtle

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
length = len(data.state)
all_states = data.state.tolist()
you_guessed = 0
lives = 5
answers = []
while lives > 0:
    answer = screen.textinput(title="guess the state", prompt=f"your total guess is {you_guessed}/50").title()
    if answer in all_states:
        all_states.remove(answer)
        check = data[data.state == answer]
        new = Turtle("circle")
        new.shapesize(0.2)
        new.penup()
        new.color("black")
        new.goto(x=float(check.x), y=float(check.y))
        new.write(answer)
        answers.append(answer)
        you_guessed += 1
    if answer == "Exit":
        print(all_states)
        break
    if lives == 0:
        print(all_states)
    else:
        lives -= 1
screen.exitonclick()
