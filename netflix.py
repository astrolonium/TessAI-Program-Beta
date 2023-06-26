from tkinter import *
import time


def show_intro(name):

    window = Tk()
    window.title("Netflix Intro")
    window.geometry("800x600")


    canvas = Canvas(window, width=800, height=600, bg="#000000")
    canvas.pack()


    netflix_text = canvas.create_text(400, 200, text="Netflix", font=("Helvetica", 70, "bold"), fill="#E50914")
    canvas.update()
    time.sleep(1)


    original_text = canvas.create_text(400, 300, text="Original", font=("Helvetica", 30, "bold"), fill="#FFFFFF")
    canvas.update()
    time.sleep(1)

    name_text = canvas.create_text(400, 400, text=name, font=("Helvetica", 70, "bold"), fill="#FFFFFF")
    canvas.update()
    time.sleep(1)


    time.sleep(7)
    window.destroy()


def show_name():
    name = name_entry.get()
    show_intro(name)


root = Tk()
root.title("Netflix Intro Name")
root.geometry("800x600")


name_label = Label(root, text="Enter your name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()


intro_button = Button(root, text="Show Intro", command=show_name)
intro_button.pack()


root.mainloop()
