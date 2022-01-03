# Import modules
import mysql.connector
from tkinter import *
from tkinter import ttk

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "MySQL2020.", database = "hairDresser")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM hairdressingsalon")
for i in mycursor:
    print(i)

#functions
def query_database():
    mycursor.execute("SELECT * FROM hairdressingsalon")
    records = mycursor.fetchall()
    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
        # increment counter
        count += 1

def hairDresserAdd(x,y):
    #clear the text boxes
    salonID.delete(0,END)
    HDSname.delete(0,END)
    address.delete(0,END)
    workingHours.delete(0,END)
    serveGender.delete(0,END)
    #stars
    provincePostcode.delete(0,END)
    text=int(x.get())
    print(text)

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
 
    hairDressingSalonAddButton = Button(window2_main, text ="Add", command=lambda x = salonID, y = HDSname: hairDresserAdd(x,y))
    hairDressingSalonAddButton.place(x = 150, y = 220, width = 55)

    hairDressingSalonDropButton = Button(window2_main, text ="Drop", command = hairDresserDrop)
    hairDressingSalonDropButton.place(x = 200, y = 220, width = 55)

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

 
    hairDresserAddButton2 = Button(window2_main, text ="Add")
    hairDresserAddButton2.place(x = 950, y = 100, width = 55)

    hairDresserDropButton2 = Button(window2_main, text ="Drop")
    hairDresserDropButton2.place(x = 1000, y = 100, width = 55)

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
    mycursor.execute("SELECT * FROM hairdressingsalon")
    records = mycursor.fetchall()
    # Add Some Style
    style = ttk.Style()

    #   Pick A Theme
    style.theme_use('default')

    # Configure the Treeview Colors
    style.configure("Treeview",
        background="#696969",
        foreground="black",
        rowheight=25,
        fieldbackground="#696969")

    # Change Selected Color
    style.map('Treeview',
        background=[('selected', "#347083")])

    # Create a Treeview Frame
    tree_frame = Frame(bookWindow)
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    global my_tree
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("salonID", "Name", "Address", "workingHours", "serveGender", "Stars", "PostCode")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("salonID", anchor=W, width=80)
    my_tree.column("Name", anchor=W, width=200)
    my_tree.column("Address", anchor=CENTER, width=220)
    my_tree.column("workingHours", anchor=CENTER, width=100)
    my_tree.column("serveGender", anchor=CENTER, width=100)
    my_tree.column("Stars", anchor=CENTER, width=70)
    my_tree.column("PostCode", anchor=CENTER, width=70)


    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("salonID", text="salonID", anchor=W)
    my_tree.heading("Name", text="Name", anchor=W)
    my_tree.heading("Address", text="Address", anchor=CENTER)
    my_tree.heading("workingHours", text="workingHours", anchor=CENTER)
    my_tree.heading("serveGender", text="serveGender", anchor=CENTER)
    my_tree.heading("Stars", text="Stars", anchor=CENTER)
    my_tree.heading("PostCode", text="PostCode", anchor=CENTER)


    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="#0c661b")
    my_tree.tag_configure('evenrow', background="#364238")


    # Run to pull data from database on start
    query_database()
        


    bookWindow.mainloop()


# Create object
root = Tk()

# Adjust size
root.geometry("960x540")
root.title('Demo')
# Add image file
bg = PhotoImage(file = "hairBG.png")

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
