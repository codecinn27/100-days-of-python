# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

FONT_NAME = "Arial"
FONT_SIZE = 10
FONT_STURC = (FONT_NAME, FONT_SIZE)

with open("data.txt", mode="a+") as file:
    file.seek(0)  # Move the file pointer to the start
    temp = file.read()
    print(temp)
    
def saving_file():
    website_temp = website_input.get()
    email_temp = email_input.get()
    password_temp = password_input.get()
    
    if len(website_temp) ==0 or len(password_temp) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #answer the popup for confirmation before appeding data to the file
        pop_up = messagebox.askquestion(title="Data Appeding Confirmation", message="Do you want to store this password in your file?")
        if pop_up=="yes":
            #able to read and append
            with open("data.txt", mode="a+") as file:
                file.write(f"\n{website_temp}  |  {email_temp}  |  {password_temp}")
                website_input.delete(0,END)
                password_input.delete(0,END)    
        else:
            pass
    
def show_password():
    password_input.config(show="")
    show_password_btn.config(text="hide" ,command=hide_password)

def hide_password():
    password_input.config(show="*")
    show_password_btn.config(text="show", command=show_password)
      
def generate_password():
    no_letters = random.randint(8,10)
    no_numbers = random.randint(2,4)
    no_symbols = random.randint(2,4)
    password_list = []
    password_list += [random.choice(letters) for _ in range(no_letters)]
    password_list += [random.choice(numbers) for _ in range(no_numbers)]
    password_list += [random.choice(symbols) for _ in range(no_symbols)]

    # Shuffle the password list to mix characters randomly
    random.shuffle(password_list)

    # Convert list to string
    password_temp = "".join(password_list)
    print(password_temp)
    password_input.delete(0,END)
    password_input.insert(0,password_temp)
    pyperclip.copy(password_temp)
    
    
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas( width=200, height=200) #the layout of the container
# Load image
img = PhotoImage(file="logo.png")  # Use .png format
# Place image on canvas
canvas.create_image(100,100, image=img) # the size of the image
canvas.grid(row=0, column=1, padx=20)

website = Label(text="Website:", font=FONT_STURC)
website.grid(row=1,column=0)
website_input = Entry(width=63)
website_input.grid(row=1, column=1, columnspan=3)
website_input.focus() #the cursor point to this input when the apps is run

email = Label(text="Email/Username:", font=FONT_STURC)
email.grid(row=2, column=0)
email_input = Entry(width=63)
email_input.insert(0,"@gmail.com")
email_input.grid(row=2, column=1, columnspan=3)

password = Label(text="Password:", font= FONT_STURC)
password.grid(row=3, column=0)
password_input = Entry(width=39, show="*")
password_input.grid(row=3, column=1)
show_password_btn = Button(text="show", command=show_password)
show_password_btn.grid(row=3,column=2)
generate_pass_btn = Button(text="Generate Password", command=generate_password)
generate_pass_btn.grid(row=3, column=3)

add_btn = Button(text="Add", font=FONT_STURC, width=48, command=saving_file)
add_btn.grid(row=4, column=1, columnspan=3)

window.mainloop()
