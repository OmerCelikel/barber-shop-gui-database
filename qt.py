import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x200')
root.resizable(False, False)
root.title('Demo')

# add button
add_button = ttk.Button(
    root,
    text='Add',
    command=lambda: root.quit()#do what
)

add_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()

