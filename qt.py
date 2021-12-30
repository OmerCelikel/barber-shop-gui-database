import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# root window
root = tk.Tk()
root.geometry('800x400')
root.resizable(False, False)
root.title('Demo')

my_img = ImageTk.PhotoImage(Image.open("photos/adam-winger--THiqda3iGM-unsplash.jpg"))
my_label = Label(image = my_img)
my_label.pack(
    ipadx=5,
    ipady=5,
    expand=True
    )

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

