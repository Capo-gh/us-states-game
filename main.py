import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        xcor = state_data.x
        ycor = state_data.y
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(xcor), int(ycor))
        t.write(answer_state)

    missing_states = [state for state in states_list if state not in guessed_states]

    # missing_states = []
    # for state in states_list:
    #     if state not in guessed_states:
    #         missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")

