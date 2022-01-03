# Import modules
import mysql.connector
from tkinter import *

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "MySQL2020.", database = "hairDresser")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM hairdressingsalon")
for i in mycursor:
    print(i)

#functions


def hairDresserAdd():
    #clear the text boxes
    salonID.delete(0,END)
    HDSname.delete(0,END)
    address.delete(0,END)
    workingHours.delete(0,END)
    serveGender.delete(0,END)
    provincePostcode.delete(0,END)
    #strSalonID = str(salonID)
    #print(type(strSalonID))

def hairDresserDrop():
    #clear the text boxes
    salonID.delete(0,END)
    HDSname.delete(0,END)
    address.delete(0,END)
    workingHours.delete(0,END)
    serveGender.delete(0,END)
    provincePostcode.delete(0,END)

    
def adminWindow():
    #root.destroy()

    window2_main = Tk()
    window2_main.geometry("1100x400")
    window2_main.title('Demo')
    Label(window2_main).pack()


    #-----------------------------------------
    #ADD NEW HairDresser Saloon

    titleOfAddHDS = Label(window2_main, text ="Add New HairDresser Saloon")
    titleOfAddHDS.place(x = 50, y = 12)
    # Defining the first row
    lblfrstrow = Label(window2_main, text ="salonID -", )
    lblfrstrow.place(x = 50, y = 40)
    global salonID
    salonID = Entry(window2_main, width = 35)
    salonID.place(x = 150, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow = Label(window2_main, text ="name -")
    lblsecrow.place(x = 50, y = 70)
    global HDSname
    HDSname = Entry(window2_main, width = 35)
    HDSname.place(x = 150, y = 70, width = 100)

    # Defining the third row
    lblsecrow = Label(window2_main, text ="address -")
    lblsecrow.place(x = 50, y = 100)
    global address
    address = Entry(window2_main, width = 35)
    address.place(x = 150, y = 100, width = 100)


    # Defining the fourth row
    lblsecrow = Label(window2_main, text ="workingHours -")
    lblsecrow.place(x = 50, y = 130)
    global workingHours
    workingHours = Entry(window2_main, width = 35)
    workingHours.place(x = 150, y = 130, width = 100)

    # Defining the fifth row
    lblsecrow = Label(window2_main, text ="serveGender -")
    lblsecrow.place(x = 50, y = 160)
    global serveGender
    serveGender = Entry(window2_main, width = 35)
    serveGender.place(x = 150, y = 160, width = 100)


    # Defining the sixth row
    lblsecrow = Label(window2_main, text ="provincePostco -")
    lblsecrow.place(x = 50, y = 190)
    global provincePostcode
    provincePostcode = Entry(window2_main, width = 35)
    provincePostcode.place(x = 150, y = 190, width = 100)



    # Add new HairDresser Saloon Button
 
    hairDresserAddButton = Button(window2_main, text ="Add", command = hairDresserAdd)
    hairDresserAddButton.place(x = 150, y = 220, width = 55)

    hairDresserDropButton = Button(window2_main, text ="Drop", command = hairDresserDrop)
    hairDresserDropButton.place(x = 200, y = 220, width = 55)

    #-----------------------------------------

    #ADD NEW Employee

    titleOfAddHDS2 = Label(window2_main, text ="Add New Employee")
    titleOfAddHDS2.place(x = 350, y = 12)
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

 
    newEmployeeAddButton = Button(window2_main, text ="Add")
    newEmployeeAddButton.place(x = 450, y = 165, width = 55)

    newEmployeeDropButton = Button(window2_main, text ="Drop")
    newEmployeeDropButton.place(x = 500, y = 165, width = 55)

    #-----------------------------------------

    #Services

    titleOfAddHDS3 = Label(window2_main, text ="Services")
    titleOfAddHDS3.place(x = 350, y = 230)
    

    # Defining the first row
    lblfrstrow3 = Label(window2_main, text ="name -", )
    lblfrstrow3.place(x = 350, y = 260)
 
    serviceName = Entry(window2_main, width = 35)
    serviceName.place(x = 450, y = 260, width = 100)
  
    # Defining the second row
    lblsecrow3 = Label(window2_main, text ="price -")
    lblsecrow3.place(x = 350, y = 290)
 
    price = Entry(window2_main, width = 35)
    price.place(x = 450, y = 290, width = 100)

    # Defining the third row
    lblthirdrow3 = Label(window2_main, text ="processingTime -")
    lblthirdrow3.place(x = 350, y = 320)
 
    processingTime = Entry(window2_main, width = 35)
    processingTime.place(x = 450, y = 320, width = 100)

    servicesAddButton = Button(window2_main, text ="Add")
    servicesAddButton.place(x = 450, y = 350, width = 55)

    servicesDropButton = Button(window2_main, text ="Drop")
    servicesDropButton.place(x = 500, y = 350, width = 55)


    #-----------------------------

    # Campaign

    titleOfAddHDS4 = Label(window2_main, text ="Add Campaign")
    titleOfAddHDS4.place(x = 600, y = 12)
    
    # Defining the first row
    lblfrstrow4 = Label(window2_main, text ="campaignID -", )
    lblfrstrow4.place(x = 600, y = 40)
 
    campaignID = Entry(window2_main, width = 35)
    campaignID.place(x = 700, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow2 = Label(window2_main, text ="type -")
    lblsecrow2.place(x = 600, y = 70)
 
    campaignType = Entry(window2_main, width = 35)
    campaignType.place(x = 700, y = 70, width = 100)

    # Defining the third row
    lblthirdrow2 = Label(window2_main, text ="expirationTime -")
    lblthirdrow2.place(x = 600, y = 100)
 
    expirationTime = Entry(window2_main, width = 35)
    expirationTime.place(x = 700, y = 100, width = 100)

 
    campaignAddButton = Button(window2_main, text ="Add")
    campaignAddButton.place(x = 700, y = 135, width = 55)

    campaignDropButton = Button(window2_main, text ="Drop")
    campaignDropButton.place(x = 750, y = 135, width = 55)

    #-----------------------------

    # Makeupartist

    titleOfAddHDS5 = Label(window2_main, text ="Add Makeup Artist")
    titleOfAddHDS5.place(x = 600, y = 230)

    # Defining the first row
    lblfrstrow5 = Label(window2_main, text ="makeupSSN -", )
    lblfrstrow5.place(x = 600, y = 260)
 
    makeupSSN = Entry(window2_main, width = 35)
    makeupSSN.place(x = 700, y = 260, width = 100)

    lblsecrow5 = Label(window2_main, text ="certificateOfExpertise -", )
    lblsecrow5.place(x = 600, y = 290)
 
    certificateOfExpertise = Entry(window2_main, width = 35)
    certificateOfExpertise.place(x = 700, y = 290, width = 100)

    makeupArtistaddButton = Button(window2_main, text ="Add")
    makeupArtistaddButton.place(x = 700, y = 320, width = 55)

    makeupArtistDropButton = Button(window2_main, text ="Drop")
    makeupArtistDropButton.place(x = 750, y = 320, width = 55)


    #--------------------------------
    # Hairdresser

    titleOfAddHDS6 = Label(window2_main, text ="Add Hairdresser")
    titleOfAddHDS6.place(x = 850, y = 12)
    
    # Defining the first row
    lblfrstrow6 = Label(window2_main, text ="expertSSN -", )
    lblfrstrow6.place(x = 850, y = 40)
 
    expertSSN = Entry(window2_main, width = 35)
    expertSSN.place(x = 950, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow6 = Label(window2_main, text ="certificateOfExpertise -")
    lblsecrow6.place(x = 850, y = 70)
 
    certificateOfExpertise = Entry(window2_main, width = 35)
    certificateOfExpertise.place(x = 950, y = 70, width = 100)

 
    hairDresserAddButton = Button(window2_main, text ="Add")
    hairDresserAddButton.place(x = 950, y = 100, width = 55)

    hairDresserDropButton = Button(window2_main, text ="Drop")
    hairDresserDropButton.place(x = 1000, y = 100, width = 55)

    #-----------------------------


    
    # exit button
    adminPanelExitButton = Button(
        window2_main,
        text='Exit',
        command=lambda: window2_main.destroy()
    )

    adminPanelExitButton.place(x = 1000, y = 350)
    window2_main.mainloop()


def bookWindow():
    #root.destroy()
    bookWindow = Tk()
    bookWindow.geometry("960x540")
    bookWindow.title('Book Window')
    #Label(bookWindow).pack()
    #fieldnames = ['salonID', 'name', 'address',"workingHours","serveGender","PostCode","Stars"]
    mycursor.execute("SELECT * FROM hairdressingsalon limit 0,15")
    i=0 
    for hairDressers in mycursor: 
        for j in range(len(hairDressers)):
            e = Entry(bookWindow, width=10, fg='white') 
            e.grid(row=i, column=j) 
            e.insert(END, hairDressers[j])
        i=i+1
    #salonID,name,address,workingHours,serveGender,provincePostcode,SCfavorNumber
    """
    #goBackButton = Button( root, text = "<--",command = )

    frame = Frame(bookWindow)
    frame.pack()

    listNodes = Listbox(frame, width=120, height=20, font=("Helvetica", 12))
    listNodes.pack(side="left", fill="y")

    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=listNodes.yview)
    scrollbar.pack(side="right", fill="y")

    listNodes.config(yscrollcommand=scrollbar.set)

    for x in range(30):
        print(" ")
        listNodes.insert(END, str(x))"""
        


    bookWindow.mainloop()


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
button2 = Button( root, text = "Book Now!", command = bookWindow)
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
