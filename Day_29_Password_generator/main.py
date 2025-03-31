# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 10
FONT_STURC = (FONT_NAME, FONT_SIZE)

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas( width=200, height=200) #the layout of the container
# Load image
img = PhotoImage(file="logo.png")  # Use .png format
# Place image on canvas
canvas.create_image(100,100, image=img) # the size of the image
canvas.grid(row=0, column=1, padx=20)

website = Label(text="Website:", font=FONT_STURC)
website.grid(row=1,column=0)
website_input = Entry(width=58)
website_input.grid(row=1, column=1, columnspan=3)

email = Label(text="Email/Username:", font=FONT_STURC)
email.grid(row=2, column=0)
email_input = Entry(width=58)
email_input.grid(row=2, column=1, columnspan=3)

password = Label(text="Password:", font= FONT_STURC)
password.grid(row=3, column=0)
password_input = Entry(width=39)
password_input.grid(row=3, column=1)
generate_pass_btn = Button(text="Generate Password")
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", font=FONT_STURC, width=43)
add_btn.grid(row=4, column=1, columnspan=3)

window.mainloop()

# 53 ,35