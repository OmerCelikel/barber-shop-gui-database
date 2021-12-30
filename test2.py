#Import the required library
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#Create an instance of tkinter window
win= Tk()
#Define the geometry of the window
win.geometry("960x540")
#Load the image
bg= ImageTk.PhotoImage(file="./bgImagecopy.png")
#Create a canvas
canvas= Canvas(win,width= 400, height= 200)
canvas.pack(expand=True, fill= BOTH)
#Add the image in the canvas
canvas.create_image(0,0,image=bg, anchor="nw")


# exit button
exit_button = ttk.Button(
    text='Exit',
    command=lambda: quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


win.mainloop()