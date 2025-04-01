from tkinter import *

def show():
    entry.config(show='')
    check.config(command=hide, text='hide password')

def hide():
    entry.config(show='*')
    check.config(command=show, text='show password')


window = Tk()
window.title('The Title')
window.geometry('400x400')
window.resizable(False, False)

entry = Entry(show='*')
entry.pack()

check = Checkbutton(text='show password',
        command=show)
check.pack()


window.mainloop()