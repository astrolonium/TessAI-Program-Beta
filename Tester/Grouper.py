import tkinter as tk
import random

def shuffle_names():
    names = entry.get().split(",")  
    random.shuffle(names)
    shuffled_names.set(", ".join(names)) 

def draw_groups():
    names = shuffled_names.get().split(", ") 
    num_groups = int(group_entry.get())  
    group_size = len(names) // num_groups 

    groups = [names[i:i+group_size] for i in range(0, len(names), group_size)] 

    
    result.set("\n".join([f"Group {i+1}: {', '.join(group)}" for i, group in enumerate(groups)]))


window = tk.Tk()
window.title("Name Shuffler")


entry_label = tk.Label(window, text="Enter names (comma-separated):")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()


shuffle_button = tk.Button(window, text="Shuffle", command=shuffle_names)
shuffle_button.pack()


shuffled_names = tk.StringVar()
shuffled_names_label = tk.Label(window, textvariable=shuffled_names)
shuffled_names_label.pack()


group_label = tk.Label(window, text="Enter the number of groups:")
group_label.pack()
group_entry = tk.Entry(window)
group_entry.pack()


draw_button = tk.Button(window, text="Draw Groups", command=draw_groups)
draw_button.pack()


result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()


window.mainloop()
