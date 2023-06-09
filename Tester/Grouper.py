import tkinter as tk
import random

def shuffle_names():
    names = entry.get().split(",")  # Get names from the entry field and split them by comma
    random.shuffle(names)  # Shuffle the names randomly
    shuffled_names.set(", ".join(names))  # Set the shuffled names in the label

def draw_groups():
    names = shuffled_names.get().split(", ")  # Get the shuffled names from the label
    num_groups = int(group_entry.get())  # Get the number of groups
    group_size = len(names) // num_groups  # Calculate the group size

    groups = [names[i:i+group_size] for i in range(0, len(names), group_size)]  # Split names into groups

    # Set the groups in the result label
    result.set("\n".join([f"Group {i+1}: {', '.join(group)}" for i, group in enumerate(groups)]))

# Create the main window
window = tk.Tk()
window.title("Name Shuffler")

# Create the name entry field
entry_label = tk.Label(window, text="Enter names (comma-separated):")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the shuffle button
shuffle_button = tk.Button(window, text="Shuffle", command=shuffle_names)
shuffle_button.pack()

# Create the shuffled names label
shuffled_names = tk.StringVar()
shuffled_names_label = tk.Label(window, textvariable=shuffled_names)
shuffled_names_label.pack()

# Create the group entry field
group_label = tk.Label(window, text="Enter the number of groups:")
group_label.pack()
group_entry = tk.Entry(window)
group_entry.pack()

# Create the draw groups button
draw_button = tk.Button(window, text="Draw Groups", command=draw_groups)
draw_button.pack()

# Create the result label
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Start the main loop
window.mainloop()
