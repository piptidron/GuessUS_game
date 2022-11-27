import turtle
import pandas
import scoreboard

game_is_on = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

guess = turtle.Turtle()
scoreboard = scoreboard.Scoreboard()

data = pandas.read_csv("50_states.csv")
list_data = data.state.to_list()
list_x = data.x.to_list()
list_y = data.y.to_list()

while scoreboard.number_guess <= 50 and game_is_on:

    answer_state = screen.textinput("Guess the state", "Enter the name of the state:").title()

    for state in list_data:
        if state == answer_state:
            index = list_data.index(answer_state)
            guess.hideturtle()
            guess.penup()
            guess.goto(list_x[index], list_y[index])
            guess.color("red")
            guess.write(f"{answer_state}", align='left', font=('Arial', 12, 'normal'))
            scoreboard.update_scoreboard()

    if scoreboard.number_guess == 50:
        turtle.write("You guessed all the states! ", align='center', font=('Arial', 50, 'normal'))
        game_is_on = False

    if answer_state == "Exit":
        turtle.write(f"Game over! You guessed {scoreboard.number_guess}", align='center', font=('Arial', 50, 'normal'))
        game_is_on = False

screen.exitonclick()


