import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []


while len(guess_states) < 50:
    ans = screen.textinput(title=f" {len(guess_states)}/{len(all_states)} Guess the state",
                           prompt="What's another state's name?").title()

    # If ans is one of the states in all states of the 50_states.csv
    # If they got is right:
    if ans == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)
        # State to learn.csv
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    if ans in all_states:
        guess_states.append(ans)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
        t.goto(int(state_data.x), int(state_data.y))
        # Create a turtle to write name of state on map
        t.write(state_data.state.item())




# # Find the co-ordinates of states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()






