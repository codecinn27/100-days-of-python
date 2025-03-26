# can mix turtle library to display the image and tkinter library to handle the data request 

import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to handle Submit button
def submit_action():
    user_input = entry.get()
    messagebox.showinfo("User Input", f"You entered: {user_input}")
    popup.destroy()

# Function to handle Cancel button
def cancel_action():
    popup.destroy()

# Create the main Turtle screen
screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")

# Create a separate Tkinter window (popup)
popup = tk.Tk()
popup.title("User Input Popup")
popup.geometry("300x150")

# Label
label = tk.Label(popup, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(popup, width=25)
entry.pack()

# Buttons
submit_button = tk.Button(popup, text="Submit", command=submit_action)
submit_button.pack(side="left", padx=20, pady=20)

cancel_button = tk.Button(popup, text="Cancel", command=cancel_action)
cancel_button.pack(side="right", padx=20, pady=20)

# Run the popup window
popup.mainloop()

# Keeps the turtle screen open
screen.exitonclick()
