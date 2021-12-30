
from PIL import ImageTk, Image
from tkinter import *

# root window
root = Tk()
root.geometry('960x540')
root.resizable(False, False)
root.title('Demo')



bg = PhotoImage(file = "./bgImagecopy.png")
#create label

# Create a canvas
my_canvas = Canvas(root, width=960, height=540)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# add button
add_button = Button(
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
exit_button = Button(
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

