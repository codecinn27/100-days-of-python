import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

circle = canvas.create_oval(50, 50, 100, 100, fill="red")

def animate():
    canvas.move(circle, 5, 0)  # Move right
    root.after(100, animate)  # Repeat every 100ms

animate()
root.mainloop()
