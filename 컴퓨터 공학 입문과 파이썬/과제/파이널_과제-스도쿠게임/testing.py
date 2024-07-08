import tkinter as tk
from tkinter import Menu

def show_popup(event):
    try:
        # Post the menu at the position of the event (button click)
        popup_menu.tk_popup(event.x_root, event.y_root)
    finally:
        # Release the grab (tk_popup sets a local grab)
        popup_menu.grab_release()

# Create the main window
root = tk.Tk()
root.title("Popup Menu Example")
root.geometry("300x200")

# Create the popup menu
popup_menu = Menu(root, tearoff=0)
popup_menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
popup_menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
popup_menu.add_separator()
popup_menu.add_command(label="Option 3", command=lambda: print("Option 3 selected"))

# Create a button
button = tk.Button(root, text="Right Click Me")
button.pack(pady=50)

# Bind the button to the right-click event (Button-3 on Windows, Mac, and most Unix systems)
button.bind("<Button-1>", show_popup)

# Start the Tkinter event loop
root.mainloop()

