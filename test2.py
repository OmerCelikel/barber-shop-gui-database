# Import module
from tkinter import *

#functions

def adminWindow():
    #root.destroy()

    window2_main = Tk()
    window2_main.geometry("1200x600")
    window2_main.title('Demo')
    Label(window2_main).pack()

    #ADD NEW HairDresser Saloon

    titleOfAddHDS = Label(window2_main, text ="Add New HairDresser Saloon")
    titleOfAddHDS.place(x = 50, y = 12)
    # Defining the first row
    lblfrstrow = Label(window2_main, text ="salonID -", )
    lblfrstrow.place(x = 50, y = 40)
 
    salonID = Entry(window2_main, width = 35)
    salonID.place(x = 150, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow = Label(window2_main, text ="name -")
    lblsecrow.place(x = 50, y = 70)
 
    name = Entry(window2_main, width = 35)
    name.place(x = 150, y = 70, width = 100)

    # Defining the third row
    lblsecrow = Label(window2_main, text ="address -")
    lblsecrow.place(x = 50, y = 100)
 
    address = Entry(window2_main, width = 35)
    address.place(x = 150, y = 100, width = 100)


    # Defining the fourth row
    lblsecrow = Label(window2_main, text ="workingHours -")
    lblsecrow.place(x = 50, y = 130)
 
    workingHours = Entry(window2_main, width = 35)
    workingHours.place(x = 150, y = 130, width = 100)

    # Defining the fifth row
    lblsecrow = Label(window2_main, text ="serveGender -")
    lblsecrow.place(x = 50, y = 160)
 
    serveGender = Entry(window2_main, width = 35)
    serveGender.place(x = 150, y = 160, width = 100)


    # Defining the sixth row
    lblsecrow = Label(window2_main, text ="provincePostco -")
    lblsecrow.place(x = 50, y = 190)
 
    provincePostcode = Entry(window2_main, width = 35)
    provincePostcode.place(x = 150, y = 190, width = 100)



    # Add new HairDresser Saloon Button
 
    addButton = Button(window2_main, text ="Add")
    addButton.place(x = 150, y = 225, width = 55)

    dropButton = Button(window2_main, text ="Drop")
    dropButton.place(x = 200, y = 225, width = 55)



    #-----------------------------------------

    #ADD NEW Employee

    titleOfAddHDS = Label(window2_main, text ="Add New Employee")
    titleOfAddHDS.place(x = 350, y = 12)
    # Defining the first row
    lblfrstrow = Label(window2_main, text ="SSN -", )
    lblfrstrow.place(x = 350, y = 40)
 
    SSN = Entry(window2_main, width = 35)
    SSN.place(x = 450, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow2 = Label(window2_main, text ="salonID -")
    lblsecrow2.place(x = 350, y = 70)
 
    salonID = Entry(window2_main, width = 35)
    salonID.place(x = 450, y = 70, width = 100)

    # Defining the third row
    lblthirdrow2 = Label(window2_main, text ="name -")
    lblthirdrow2.place(x = 350, y = 100)
 
    nameE = Entry(window2_main, width = 35)
    nameE.place(x = 450, y = 100, width = 100)


    # Defining the fourth row
    lblfourthrow2 = Label(window2_main, text ="gender -")
    lblfourthrow2.place(x = 350, y = 130)
 
    gender = Entry(window2_main, width = 35)
    gender.place(x = 450, y = 130, width = 100)



    # Add new HairDresser Saloon Button
 
    addButton2 = Button(window2_main, text ="Add")
    addButton2.place(x = 450, y = 165, width = 55)

    dropButton2 = Button(window2_main, text ="Drop")
    dropButton2.place(x = 500, y = 165, width = 55)

    #-----------------------------------------

    #Services

    titleOfAddHDS = Label(window2_main, text ="Services")
    titleOfAddHDS.place(x = 350, y = 190)
    

    # Defining the first row
    lblfrstrow3 = Label(window2_main, text ="name -", )
    lblfrstrow3.place(x = 350, y = 220)
 
    serviceName = Entry(window2_main, width = 35)
    serviceName.place(x = 450, y = 220, width = 100)
  
    # Defining the second row
    lblsecrow3 = Label(window2_main, text ="price -")
    lblsecrow3.place(x = 350, y = 250)
 
    price = Entry(window2_main, width = 35)
    price.place(x = 450, y = 250, width = 100)

    # Defining the third row
    lblthirdrow3 = Label(window2_main, text ="processingTime -")
    lblthirdrow3.place(x = 350, y = 280)
 
    processingTime = Entry(window2_main, width = 35)
    processingTime.place(x = 450, y = 280, width = 100)

    addButton3 = Button(window2_main, text ="Add")
    addButton3.place(x = 450, y = 310, width = 55)

    dropButton3 = Button(window2_main, text ="Drop")
    dropButton3.place(x = 500, y = 310, width = 55)


    #-----------------------------

    
    # exit button
    exit_button = Button(
        window2_main,
        text='Exit',
        command=lambda: window2_main.destroy()
    )

    exit_button.place(x = 1100, y = 550)
    window2_main.mainloop()


# Create object
root = Tk()

# Adjust size
root.geometry("960x540")
root.title('Demo')
# Add image file
bg = PhotoImage(file = "bgImagecopy.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
                height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")


# Create Buttons
button1 = Button( root, text = "Admin Login",command = adminWindow)
button2 = Button( root, text = "Book Now!")
button3 = Button( root, text = "Exit",command=lambda: root.quit())

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
