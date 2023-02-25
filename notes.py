import tkinter as tk
import os

# Create a main window with full screen
root = tk.Tk()
root.attributes('-fullscreen', True)

# Create a canvas to hold the notes
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a frame to hold the notes
frame = tk.Frame(canvas)
frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create a function to add a note
def add_note():
    # Get the text from the note field
    note_text = note_field.get(1.0, tk.END).strip()

    # Check if the note field is empty
    if note_text == '':
        return

    # Check if the user has already added 10 notes
    if len(os.listdir('./notes')) >= 10:
        return

    # Create a new note file
    note_file = open('./notes/note_' + str(len(os.listdir('./notes')) + 1) + '.txt', 'w')
    note_file.write(note_text)
    note_file.close()

    # Clear the note field
    note_field.delete(1.0, tk.END)

    # Update the list of notes
    update_notes()

# Create a function to update the list of notes
def update_notes():
    # Clear the list of notes
    for widget in notes_frame.winfo_children():
        widget.destroy()

    # Get the list of note files
    note_files = sorted(os.listdir('./notes'))

    # Display the list of notes
    for note_file in note_files:
        note_path = os.path.join('./notes', note_file)
        note_file = open(note_path, 'r')
        note_text = note_file.read()
        note_file.close()

        note_label = tk.Label(notes_frame, text=note_text[:200] + '...', wraplength=600)
        note_label.pack(fill=tk.BOTH, padx=10, pady=5)

# Create a label for the note field
note_label = tk.Label(frame, text='Add a note:')
note_label.pack(fill=tk.X, padx=10, pady=5)

# Create a note field
note_field = tk.Text(frame, height=10, wrap=tk.WORD)
note_field.pack(fill=tk.BOTH, padx=10, pady=5)

# Create a button to add a note
add_note_button = tk.Button(frame, text='Add Note', command=add_note)
add_note_button.pack(fill=tk.X, padx=10, pady=5)

# Create a frame to hold the list of notes
notes_frame = tk.Frame(canvas)
notes_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Update the list of notes
update_notes()

# Start the main event loop
root.mainloop()
