import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

guesses_correct = 0

while guesses_correct != 50:
    answer_state = screen.textinput(title=f"{guesses_correct}/50 States Correct", prompt="What is another state name?")
    if answer_state == "exit":

        

        break
    if answer_state.title() in states:
        guesses_correct += 1
        state_data = data[data.state == answer_state.title()]
        state_turtle = turtle.Turtle(visible=False)
        state_turtle.penup()
        state_turtle.goto(x=int(state_data.x), y=int(state_data.y))
        state_turtle.write(answer_state.title(), font=('Arial', 14, 'normal'))

