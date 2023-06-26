from tkinter import *
import random


window = Tk()
window.title("Football Game")
window.geometry("600x400")


canvas = Canvas(window, width=600, height=400)
canvas.pack()


grass = canvas.create_rectangle(0, 0, 600, 400, fill="green")
goalpost1 = canvas.create_rectangle(50, 150, 70, 250, fill="white")
goalpost2 = canvas.create_rectangle(480, 150, 500, 250, fill="white")
goalnet1 = canvas.create_polygon(70, 150, 100, 150, 100, 250, 70, 250, fill="white")
goalnet2 = canvas.create_polygon(500, 150, 470, 150, 470, 250, 500, 250, fill="white")


audience1 = canvas.create_oval(80, 80, 100, 100, fill="red")
audience2 = canvas.create_oval(100, 100, 120, 120, fill="red")
audience3 = canvas.create_oval(120, 80, 140, 100, fill="red")
audience4 = canvas.create_oval(160, 80, 180, 100, fill="red")
audience5 = canvas.create_oval(180, 100, 200, 120, fill="red")
audience6 = canvas.create_oval(200, 80, 220, 100, fill="red")
audience7 = canvas.create_oval(260, 80, 280, 100, fill="red")
audience8 = canvas.create_oval(280, 100, 300, 120, fill="red")
audience9 = canvas.create_oval(300, 80, 320, 100, fill="red")
audience10 = canvas.create_oval(340, 80, 360, 100, fill="red")
audience11 = canvas.create_oval(360, 100, 380, 120, fill="red")
audience12 = canvas.create_oval(380, 80, 400, 100, fill="red")


player = canvas.create_oval(50, 175, 70, 195, fill="yellow")
player_x = 0
player_y = 0
player_speed = 10


football = canvas.create_oval(50, 180, 60, 190, fill="white")
football_x = 0
football_y = 0
football_speed = 5


def move_player():
    global player_x, player_y
    canvas.move(player, player_x, player_y)
    player_coords = canvas.coords(player)
    if player_coords[0] < 0 or player_coords[1] < 0 or player_coords[2] > 600 or player_coords[3] > 400:
        player_x = 0
        player_y = 0
    canvas.after(player_speed, move_player)

def move_football():
    global football_x, football_y
    canvas.move(football, football_x, football_y)
    football_coords = canvas.coords(football)
    
    
    if canvas.find_overlapping(football_coords[0], football_coords[1], football_coords[2], football_coords[3]) == (2, 3):
        print("GOAL!")
        canvas.create_text(300, 50, text="YOU WIN!", font=("Arial", 20), fill="white")
        canvas.after(2000, window.destroy)  # End the program after 2 seconds

    if football_coords[0] < 0 or football_coords[1] < 0 or football_coords[2] > 600 or football_coords[3] > 400:
        football_x = -football_x
        football_y = -football_y
    
    canvas.after(football_speed, move_football)
