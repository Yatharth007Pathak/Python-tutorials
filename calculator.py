import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Choose operation (+, -, *, /):")
label_operation.pack()

operation_var = tk.StringVar(root)
entry_operation = tk.Entry(root, textvariable=operation_var)
entry_operation.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

# Run the main loop
root.mainloop()