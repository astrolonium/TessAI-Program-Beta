from tkinter import *
import random


window = Tk()
window.title("Student Lottery")
window.geometry("400x400")


name_label = Label(window, text="Enter Student Name:")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

age_label = Label(window, text="Enter Student Age:")
age_label.pack()
age_entry = Entry(window)
age_entry.pack()

grade_label = Label(window, text="Enter Student Grade:")
grade_label.pack()
grade_entry = Entry(window)
grade_entry.pack()


student_list = []

def add_student():
    student = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "grade": grade_entry.get()
    }
    student_list.append(student)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    grade_entry.delete(0, END)

add_button = Button(window, text="Add Student", command=add_student)
add_button.pack()


def select_student():
    if student_list:
        selected_student = random.choice(student_list)
        cob_message = f"Congratulations {selected_student['name']}! You have won the cob."
        cob_label.config(text=cob_message)

select_button = Button(window, text="Select Student", command=select_student)
select_button.pack()


cob_label = Label(window, text="")
cob_label.pack()


window.mainloop()
