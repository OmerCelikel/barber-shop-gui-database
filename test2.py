# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("960x540")

# Add image file
bg = PhotoImage(file = "bgImagecopy.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
                height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
                    anchor = "nw")


# Create Buttons
button1 = Button( root, text = "Admin Login",)
button2 = Button( root, text = "Book Now!")
button3 = Button( root, text = "Exit")

# Display Buttons
button1_canvas = canvas1.create_window( 60, 520,
                                    anchor = "center",
                                    window = button1)

button2_canvas = canvas1.create_window( 730, 350,
                                    anchor = "center",
                                    window = button2)

button3_canvas = canvas1.create_window( 730, 450, 
                                    anchor = "center",
                                    window = button3)

# Execute tkinter
root.mainloop()
