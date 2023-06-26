import tkinter as tk
from tkinter import ttk
import random

class RandomGroupsGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Random Groups Generator")
        self.master.geometry("800x600")


        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.gradient = tk.PhotoImage(file="gradient.png")
        self.canvas.create_image(0, 0, image=self.gradient, anchor="nw")


        self.header = ttk.Label(self.master, text="Random Groups Generator", font=("Helvetica", 30, "bold"), foreground="white")
        self.header.place(relx=0.5, rely=0.1, anchor="center")

      
        self.student_label = ttk.Label(self.master, text="Enter Student Names (separated by commas):", font=("Helvetica", 18), foreground="white")
        self.student_label.place(relx=0.3, rely=0.3, anchor="w")

        self.student_entry = tk.Text(self.master, height=5, width=50, font=("Helvetica", 14))
        self.student_entry.place(relx=0.3, rely=0.4, anchor="w")

        self.group_label = ttk.Label(self.master, text="Number of Groups:", font=("Helvetica", 18), foreground="white")
        self.group_label.place(relx=0.3, rely=0.6, anchor="w")

        self.group_entry = tk.Spinbox(self.master, from_=1, to=10, font=("Helvetica", 14), width=5)
        self.group_entry.place(relx=0.6, rely=0.6, anchor="w")

        self.generate_button = ttk.Button(self.master, text="Generate Groups", command=self.generate_groups, style="TButton")
        self.generate_button.place(relx=0.5, rely=0.8, anchor="center")

    def generate_groups(self):
        student_list = self.student_entry.get("1.0", "end").strip().split(",")
        group_num = int(self.group_entry.get())

  
        random.shuffle(student_list)

      
        groups = [student_list[i::group_num] for i in range(group_num)]

      
        self.show_groups(student_list, groups)

    def show_groups(self, student_list, groups):
     
        for widget in self.canvas.winfo_children():
            widget.destroy()

       
        names_label = ttk.Label(self.canvas, text="List of Names", font=("Helvetica", 18), foreground="white")
        names_label.place(relx=0.2, rely=0.2, anchor="center")

        names_text = tk.Text(self.canvas, height=5, width=50, font=("Helvetica", 14))
        names_text.insert("end", "\n".join(student_list))
        names_text.place(relx=0.2, rely=0.3, anchor="center")

        
        groups_label = ttk.Label(self.canvas, text="Groups", font=("Helvetica", 18), foreground="white")
        groups_label.place(relx=0.8, rely=0.2, anchor="center")


def create_groups(names, num_groups):
    random.shuffle(names) 
    groups = [[] for i in range(num_groups)]  
    for i, name in enumerate(names):
        groups[i % num_groups].append(name) 
    return groups


def select_winner(groups, canvas):
    winner = random.choice(groups[0])
  
    canvas.create_text(300, 200, text=f"Congratulations, {winner}!", font=("Helvetica", 24), fill="white")
    

def on_submit():
    num_groups = int(group_entry.get())
    names = name_entry.get().split(", ")
    groups = create_groups(names, num_groups)
    select_winner(groups, canvas)
    

window = tk.Tk()
window.title("Group Generator")


canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()


canvas.create_text(300, 50, text="Group Generator", font=("Helvetica", 36), fill="white")


canvas.create_text(150, 100, text="Enter names:", font=("Helvetica", 18), fill="white")
name_entry = tk.Entry(window, width=30, font=("Helvetica", 16))
canvas.create_window(400, 100, window=name_entry)


canvas.create_text(150, 150, text="Number of groups:", font=("Helvetica", 18), fill="white")
group_entry = tk.Entry(window, width=5, font=("Helvetica", 16))
canvas.create_window(400, 150, window=group_entry)


submit_button = tk.Button(window, text="Generate Groups", font=("Helvetica", 18), command=on_submit)
canvas.create_window(300, 250, window=submit_button)


canvas.create_rectangle(0, 0, 600, 400, fill="white", outline="")
for i in range(10):
    canvas.create_rectangle(0, i*40, 600, (i+1)*40, fill=f"#{i*10:02x}{'ff':02x}")


window.mainloop()
