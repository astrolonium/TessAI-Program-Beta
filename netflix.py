from tkinter import *
import time

# Define the function to display the Netflix intro
def show_intro(name):
    # Create the window
    window = Tk()
    window.title("Netflix Intro")
    window.geometry("800x600")

    # Create the canvas
    canvas = Canvas(window, width=800, height=600, bg="#000000")
    canvas.pack()

    # Create the "Netflix" text
    netflix_text = canvas.create_text(400, 200, text="Netflix", font=("Helvetica", 70, "bold"), fill="#E50914")
    canvas.update()
    time.sleep(1)

    # Create the "Original" text
    original_text = canvas.create_text(400, 300, text="Original", font=("Helvetica", 30, "bold"), fill="#FFFFFF")
    canvas.update()
    time.sleep(1)

    # Create the user's name
    name_text = canvas.create_text(400, 400, text=name, font=("Helvetica", 70, "bold"), fill="#FFFFFF")
    canvas.update()
    time.sleep(1)

    # Wait for 15 seconds and then close the window
    time.sleep(7)
    window.destroy()

# Define the function to get the user's name and show the intro
def show_name():
    name = name_entry.get()
    show_intro(name)

# Create the window
root = Tk()
root.title("Netflix Intro Name")
root.geometry("800x600")

# Create the name input field
name_label = Label(root, text="Enter your name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Create the button to show the intro
intro_button = Button(root, text="Show Intro", command=show_name)
intro_button.pack()

# Start the main loop
root.mainloop()
