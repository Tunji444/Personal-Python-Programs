import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the GUI
root = tk.Tk()
root.title("Calculator")

# Create the entry widget for display
entry = tk.Entry(root, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(root, text=str(i), padx=20, pady=10, command=lambda num=i: button_click(num))
    button.grid(row=(9-i)//3 + 1, column=(i-1)%3)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, padx=20, pady=10, command=lambda op=operator: button_click(op))
    button.grid(row=i+1, column=3)

# Create additional buttons
button_zero = tk.Button(root, text='0', padx=20, pady=10, command=lambda: button_click(0))
button_zero.grid(row=4, column=0)

button_clear = tk.Button(root, text='C', padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=1)

button_equal = tk.Button(root, text='=', padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2)

root.mainloop()