import tkinter as tk

# Create the Tkinter window
root = tk.Tk()

# Create the canvas widget
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Draw the x and y axes
canvas.create_line(300, 0, 300, 600, width=2, arrow=tk.LAST)
canvas.create_line(0, 300, 600, 300, width=2, arrow=tk.LAST)

# Draw the x and y axis labels
canvas.create_text(290, 310, text="0")
canvas.create_text(590, 310, text="x")
canvas.create_text(310, 10, text="y")
canvas.create_text(310, 590, text="0")

# Draw the x and y axis tick marks
for i in range(-6, 7):
    canvas.create_line(100*i+300, 295, 100*i+300, 305)
    canvas.create_text(100*i+300, 315, text=str(i))
    canvas.create_line(295, 100*i+300, 305, 100*i+300)
    canvas.create_text(315, 100*i+300, text=str(-i))

# Draw the graph of y = -6/x
prev_x, prev_y = None, None
for x in range(-600, 601):
    if x == 0:
        continue
    y = -6 / x
    x_pixel = x + 300 # Scale x to fit the canvas
    y_pixel = -y * 100 + 300 # Scale y to fit the canvas
    if prev_x is not None and prev_y is not None:
        canvas.create_line(prev_x, prev_y, x_pixel, y_pixel, width=2) # Draw a line between the previous and current points
    prev_x, prev_y = x_pixel, y_pixel

# Start the Tkinter event loop
root.mainloop()
