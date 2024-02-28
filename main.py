import tkinter as tk 
def button_click(symbol):
    current = entry_variable.get()
    entry_variable.set(current+symbol)

def clear():
    entry_variable.set("")

def calc():
    try:
        res = eval(entry_variable.get())
        entry_variable.set(str(res))
    except:
        entry_variable.set("Error")
root = tk.Tk()

root.title("Calculator")
entry_variable = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_variable, font=("Arial", 15))
entry.grid(row=0, column=0, columnspan=4, sticky='nesw')
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ("/", 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ('-', 3, 3),
    ("0", 4, 0), ('.', 4, 1), ("=", 4, 2), ("+", 4, 3),
]
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 15), command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column, sticky='nswe')
clearBtn = tk.Button(root, text="C", font=("Arial", 15), command=clear)
clearBtn.grid(row=5, column=0, columnspan=2, sticky='nswe')

calcBtn = tk.Button(root, text="=", font=("Arial", 15), command=calc)
calcBtn.grid(row=5, column=2, columnspan=2, sticky='nswe')

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
