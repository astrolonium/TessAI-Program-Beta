import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.entry = tk.Entry(self.master, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            "sin", "cos", "tan", "log",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "(", ")", "^", "="
        ]
        row = 1
        col = 0
        for button_text in buttons:
            command = lambda x=button_text: self.button_click(x)
            button = tk.Button(self.master, text=button_text, width=5, command=command)
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                row += 1
                col = 0

    def button_click(self, button_text):
        if button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text == "=":
            self.calculate()
        else:
            self.entry.insert(tk.END, button_text)

    def calculate(self):
        try:
            expression = self.entry.get()
            expression = expression.replace("^", "**")
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as e:
            print(e)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
