import tkinter as tk
import os


root = tk.Tk()
root.attributes('-fullscreen', True)


canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)


frame = tk.Frame(canvas)
frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)


def add_note():
 
    note_text = note_field.get(1.0, tk.END).strip()


    if note_text == '':
        return


    if len(os.listdir('./notes')) >= 10:
        return


    note_file = open('./notes/note_' + str(len(os.listdir('./notes')) + 1) + '.txt', 'w')
    note_file.write(note_text)
    note_file.close()

    note_field.delete(1.0, tk.END)

    update_notes()


def update_notes():
    
    for widget in notes_frame.winfo_children():
        widget.destroy()

   
    note_files = sorted(os.listdir('./notes'))

  
    for note_file in note_files:
        note_path = os.path.join('./notes', note_file)
        note_file = open(note_path, 'r')
        note_text = note_file.read()
        note_file.close()

        note_label = tk.Label(notes_frame, text=note_text[:200] + '...', wraplength=600)
        note_label.pack(fill=tk.BOTH, padx=10, pady=5)


note_label = tk.Label(frame, text='Add a note:')
note_label.pack(fill=tk.X, padx=10, pady=5)


note_field = tk.Text(frame, height=10, wrap=tk.WORD)
note_field.pack(fill=tk.BOTH, padx=10, pady=5)


add_note_button = tk.Button(frame, text='Add Note', command=add_note)
add_note_button.pack(fill=tk.X, padx=10, pady=5)


notes_frame = tk.Frame(canvas)
notes_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)


update_notes()


root.mainloop()
