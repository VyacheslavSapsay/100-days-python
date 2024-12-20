import turtle
import pandas

screen = turtle.Screen()

screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_file_data = pandas.read_csv('50_states.csv')
states = states_file_data.state.to_list()
guessed_states = []

while True:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/{len(states)} states correct', prompt='Enter the state name')
    answer_state = answer_state.title()
    if answer_state == 'Exit':
        break
    elif answer_state not in states:
        continue
    
    state_data = states_file_data[states_file_data.state == answer_state]
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.setposition(float(state_data.x), float(state_data.y))
    text.write(answer_state, align="center", font=("Courier", 16, "normal"))
    guessed_states.append(answer_state)

states_to_learn = {'state': list(set(states) - set(guessed_states))}

pandas.DataFrame(states_to_learn).to_csv('states_to_learn.csv')
