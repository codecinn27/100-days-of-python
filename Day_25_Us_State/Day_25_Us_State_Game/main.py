from turtle import Screen, Turtle
import pandas as pd

FONT = ("Courier", 10, "normal")
ALIGNMENT = "center"

guess_correct = 0
screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
#store the full data into a pandas dataframe
full_data = pd.read_csv("50_states.csv")
correct_guess_list = []
to_learn_state = []

while guess_correct<len(full_data):
    answer_state = screen.textinput(title=f"{guess_correct}/50 States Correct",prompt="What's another state name? ")
    if answer_state == "exit" or answer_state == "Exit":
        # for index, rows in full_data.iterrows():
        #     if rows["state"] not in correct_guess_list:
        #         to_learn_state.append(rows["state"])
        to_learn_state= [y["state"] for x,y in full_data.iterrows() if y["state"] not in correct_guess_list]
        new_data = pd.DataFrame(to_learn_state)
        new_data.to_csv("to_learn_state.csv")
        break
                
            
    for index,rows in full_data.iterrows():
        if answer_state == rows["state"] and answer_state not in correct_guess_list:
            turtle.goto((rows["x"],rows["y"]))
            turtle.write(rows["state"], align=ALIGNMENT, font=FONT)
            guess_correct +=1
            correct_guess_list.append(rows["state"])
        
        
            
            
            
# game_is_on =True
# while game_is_on:
#     for index,rows in full_data.iterrows():
#         if answer_state== rows["state"]:
#             turtle.goto((rows["x"],rows["y"]))
#             turtle.write(rows["state"], align=ALIGNMENT ,font=FONT)
#             guess_correct +=1
#             answer_state = screen.textinput(title=f"{guess_correct}/50 States Correct",prompt="What's another state name? ")






# state_names = full_data["state"]
# print(full_data)
# print(state_names)

# temp = full_data[full_data["state"]=="Alabama"]
# print(temp)

#to iterate all the data through each in dataframe using .iterrows()
# for index, row in full_data.iterrows():
#     state = row["state"]
#     x = row["x"]
#     y = row["y"]
#     print(f"State: {state}, Coordinates: ({x}, {y})")

# steps 
# Turtle screen to get input from user "What's another state name ? "
# turtle class to display the map screen
# add state name into the list then check user input 
# if is in the list, turtle go to the coordinate and write the state name  