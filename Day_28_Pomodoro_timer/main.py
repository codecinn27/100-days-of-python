
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TITLE = ["Pomodoro Timer", "FOCUS", "Break", "Long Break"]
COUNTDOWN_FOCUS = [00,5] # change here for you focus minutes time
COUNTDOWN_BREAK = [00,3] #change here for the short break time
COUNTDOWN_LONG_BREAK = [00,10] #change here for the long break time 
LONG_BREAK_INTERVAL = 5 #change here for how many pomodoro you need before taking long break

from tkinter import *

window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20, bg=YELLOW)


canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112, image= tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white" , font=("Courier", 36, "bold"))
canvas.grid(row=1,column=1)

title = Label(text=TITLE[0], font=("Courier",20, "bold"), bg=YELLOW ,fg=GREEN)
title.grid(row=0, column=1)


tick = 0
after_id = None  # Store `after()` ID for countdown
break_id = None  # Store `after()` ID for break timer

def update_tick():
    global tick  #must declare as global variable
    tick +=1 
    record["text"] = "✓"*tick
    
def reset_clock():
    canvas.itemconfig(timer_text, text=f"{COUNTDOWN_FOCUS[0]:02d}:{COUNTDOWN_FOCUS[1]:02d}")
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down_25mins(min, seconds):
    global tick, after_id # use global to track the scheduled task
    
    title["text"] = TITLE[1]
    if seconds<=0 and min>0:
        min -=1
        seconds += 59
    
    if seconds>0 and min>=0:
        # add 02d to have 2 significant figure even is drop to a ones or zeroes
        canvas.itemconfig(timer_text, text=f"{min:02d}:{seconds:02d}")
        after_id = window.after(1000,count_down_25mins,min, seconds-1)
    
    if seconds==0 and min==0:
        update_tick()
        if tick%LONG_BREAK_INTERVAL == 0: 
            long_breaktime(COUNTDOWN_LONG_BREAK[0], COUNTDOWN_LONG_BREAK[1])
        else:
            breaktime(COUNTDOWN_BREAK[0], COUNTDOWN_BREAK[1])
        
def reset_everything():
    global tick, after_id, break_id
    
    title["text"] = TITLE[0]
    
    if after_id:
        window.after_cancel(after_id)
        after_id = None # reset the stored ID
    
    if break_id:
        window.after_cancel(break_id)
        break_id = None 
    
    reset_clock()
    
    tick = 0 
    record["text"] = "✓"*tick
    
def breaktime(min, seconds):
    global break_id
    
    title["text"] = TITLE[2]

    if seconds<=0 and min>0:
        min -=1
        seconds += 59
    
    if seconds>0 and min>=0:
        # add 02d to have 2 significant figure even is drop to a ones or zeroes
        canvas.itemconfig(timer_text, text=f"{min:02d}:{seconds:02d}")    
        break_id = window.after(1000, breaktime, min, seconds-1)
        
    if seconds==0 and min==0:
        count_down_25mins(COUNTDOWN_FOCUS[0], COUNTDOWN_FOCUS[1])
        
def long_breaktime(min, seconds):
    global break_id
    
    title["text"] = TITLE[3]

    if seconds<=0 and min>0:
        min -=1
        seconds += 59
    
    if seconds>0 and min>=0:
        # add 02d to have 2 significant figure even is drop to a ones or zeroes
        canvas.itemconfig(timer_text, text=f"{min:02d}:{seconds:02d}")    
        break_id = window.after(1000, long_breaktime, min, seconds-1)
        
    if seconds==0 and min==0:
        count_down_25mins(COUNTDOWN_FOCUS[0], COUNTDOWN_FOCUS[1])
        
# ✅ Uses lambda to prevent immediate execution
start_btn = Button(text="Start", command= lambda: count_down_25mins(COUNTDOWN_FOCUS[0], COUNTDOWN_FOCUS[1]))
start_btn.grid(row=2, column=0)

record = Label(fg="green", bg=YELLOW)
record.grid(row=2, column=1)

reset_btn = Button(text="Reset", command=reset_everything)
reset_btn.grid(row=2,column=2)


        
    

window.mainloop()

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #