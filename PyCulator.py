import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Global variables
expression = ""
input_var = tk.StringVar()

# Input field
input_field = tk.Entry(root, textvar=input_var, font=("Arial", 20), justify="right", bd=8, relief=tk.SUNKEN)
input_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(expand=True, fill="both")
    for button_text in row:
        button = tk.Button(button_row, text=button_text, font=("Arial", 18), relief=tk.RAISED, border=3)
        button.pack(side=tk.LEFT, expand=True, fill="both")
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
