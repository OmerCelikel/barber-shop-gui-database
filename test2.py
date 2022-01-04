# Import modules
import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as box

#connecting with database
#Type your password in the password field.
db = mysql.connector.connect(host = "localhost",user = "root",passwd = "MySQL2020.", database = "hairDresser")
mycursor = db.cursor()

#functions

#When the operation is successful
def last(SSN, Name, Surname, Gender):

    newSSN =str(SSN.get())
    newName = str(Name.get())
    newSurname = str(Surname.get())
    newGender = str(Gender.get())

    successfullWindow.destroy()
    lastWindow = Tk()
    lastWindow.geometry("360x300")
    lastWindow.title('successful')
    data_frame = LabelFrame(lastWindow, text=" Thank You ! :) :) ")
    data_frame.pack(fill="x", expand="yes", padx=10)

    update_button2 = Button(data_frame, text="Quit",command=lambda: lastWindow.destroy())
    update_button2.grid(row=0, column=0, padx=130, pady=10)


    mycursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s)", (int(newSSN), newName, newSurname, newGender))
    db.commit()

    lastWindow.mainloop()

#admin name password check
def dialog1(Username,Password):
    username=Username.get()
    password = Password.get()
    if (username == 'adminOmer' and  password == '1234'):
        adminLoginWindow.destroy()
        box.showinfo('info','Correct Login')
        adminWindow()
    else:
        box.showinfo('info','Invalid Login')

def adminLoginWindow():
    global adminLoginWindow
    adminLoginWindow = Tk()
    adminLoginWindow.title('Admin Login')

    frame = Frame(adminLoginWindow)

    Label1 = Label(adminLoginWindow,text = 'Username:')
    Label1.pack(padx=15,pady= 5)
    entry1 = Entry(adminLoginWindow,bd =5)
    entry1.pack(padx=15, pady=5)



    Label2 = Label(adminLoginWindow,text = 'Password: ')
    Label2.pack(padx = 15,pady=6)

    entry2 = Entry(adminLoginWindow, bd=5)
    entry2.pack(padx = 15,pady=7)




    btn = Button(frame, text = 'Check Login',command=lambda  Username = entry1, Password = entry2 : dialog1(Username,Password))


    btn.pack(side = RIGHT , padx =5)
    frame.pack(padx=100,pady = 19)
    adminLoginWindow.mainloop()

# the following 3 functions open a new page and show the database information
def showCustDB():
    showcustomerDB = Tk()
    showcustomerDB.geometry("450x340")
    showcustomerDB.title('Database')

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
    tree_frame = Frame(showcustomerDB)
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    global my_treeC
    my_treeC = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_treeC.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_treeC.yview)

    # Define Our Columns
    my_treeC['columns'] = ("SSN", "Name", "Surname", "Gender")

    # Format Our Columns
    my_treeC.column("#0", width=0, stretch=NO)
    my_treeC.column("SSN", anchor=W, width=80)
    my_treeC.column("Name", anchor=W, width=120)
    my_treeC.column("Surname", anchor=W, width=120)
    my_treeC.column("Gender", anchor=CENTER, width=80)



    # Create Headings
    my_treeC.heading("#0", text="", anchor=W)
    my_treeC.heading("SSN", text="SSN", anchor=W)
    my_treeC.heading("Name", text="Name", anchor=W)
    my_treeC.heading("Surname", text="Surname", anchor=CENTER)
    my_treeC.heading("Gender", text="Gender", anchor=CENTER)


    # Create Striped Row Tags
    my_treeC.tag_configure('oddrow', background="#0c661b")
    my_treeC.tag_configure('evenrow', background="#364238")

    # Run to pull data from database on start
    query_databaseForCustomer()
def showemployeeDB():
    showemployeeDB = Tk()
    showemployeeDB.geometry("900x240")
    showemployeeDB.title('Database')
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
    tree_frame = Frame(showemployeeDB)
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    global my_treeE
    my_treeE = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_treeE.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_treeE.yview)

    # Define Our Columns
    my_treeE['columns'] = ("SSN", "salonID", "Name", "Gender")

    # Format Our Columns
    my_treeE.column("#0", width=0, stretch=NO)
    my_treeE.column("SSN", anchor=W, width=80)
    my_treeE.column("salonID", anchor=W, width=200)
    my_treeE.column("Name", anchor=CENTER, width=220)
    my_treeE.column("Gender", anchor=CENTER, width=100)



    # Create Headings
    my_treeE.heading("#0", text="", anchor=W)
    my_treeE.heading("SSN", text="SSN", anchor=W)
    my_treeE.heading("salonID", text="salonID", anchor=W)
    my_treeE.heading("Name", text="Name", anchor=CENTER)
    my_treeE.heading("Gender", text="Gender", anchor=CENTER)


    # Create Striped Row Tags
    my_treeE.tag_configure('oddrow', background="#0c661b")
    my_treeE.tag_configure('evenrow', background="#364238")

    # Run to pull data from database on start
    query_databaseForEmployee()
def showHDSDB():
    showHDSDB = Tk()
    showHDSDB.geometry("900x240")
    showHDSDB.title('Database')
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
    tree_frame = Frame(showHDSDB)
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

# Window where addition
def addWindow():
    print("Added Successfully")
    transaction = Tk()
    transaction.geometry("360x300")
    transaction.title('successful')
    data_frame = LabelFrame(transaction, text=" Added Successfully ! ")
    data_frame.pack(fill="x", expand="yes", padx=10)

    update_button2 = Button(data_frame, text="Quit",command=lambda: transaction.destroy())
    update_button2.grid(row=0, column=0, padx=130, pady=10)
    transaction.mainloop()

def dropWindow():
    print("Dropped Successfully!")
    transaction = Tk()
    transaction.geometry("360x300")
    transaction.title('successful')
    data_frame = LabelFrame(transaction, text=" Dropped Successfully ! ")
    data_frame.pack(fill="x", expand="yes", padx=10)

    update_button2 = Button(data_frame, text="Quit",command=lambda: transaction.destroy())
    update_button2.grid(row=0, column=0, padx=130, pady=10)
    transaction.mainloop()

def delete():
   # Get selected item to Delete
   selected_item = my_tree2.selection()[0]
   print(selected_item)
   deletedItem = selected_item
   my_tree2.delete(selected_item)
   print(deletedItem)

# Retrieves user information
def bookedSuccessfully(serviceName, hairDresserName, bookedTime):
    serviceName = str(serviceName.get())
    hairDresserName = str(hairDresserName.get())
    bookedTime = str(bookedTime.get())
    global hairdresserSSN
    mycursor.execute("SELECT * FROM employee")
    for i in mycursor:
        if(hairDresserName == i[2]):
            hairdresserSSN = i[0]
            print(hairDresserName, hairdresserSSN)
            hairdresserSSN = str(hairdresserSSN)
    print("bookedTime : ", bookedTime, type(bookedTime))
    
    print("ssn : ", hairdresserSSN, type(hairdresserSSN))
    #mycursor.execute("SELECT * FROM avbDates")
    mycursor.execute("SELECT employee.SSN, employee.name, avbDates.datetime FROM avbDates, employee WHERE employee.name = '%s' AND avbDates.datetime =  '%s'" %(hairDresserName,bookedTime))
    for i in mycursor:
        print(i)
    mycursor.execute("DELETE FROM avbDates WHERE avbDates.employeeSSN = '%s' AND avbDates.datetime =  '%s'" %(hairdresserSSN,bookedTime))
    db.commit()
    salonWindow.destroy()
    global successfullWindow
    successfullWindow = Tk()
    successfullWindow.geometry("460x400")
    successfullWindow.title('successful mu')

    # Add Record Entry Boxes
    data_framea = LabelFrame(successfullWindow, text="  Registration  ")
    data_framea.pack(fill="x", expand="yes", padx=10)
    global fn_entrya
    global fn_entry2a
    global fn_entry3a
    global fn_entry4a

    global SSN
    global Name
    global Surname
    global Gender
    fn_labela = Label(data_framea, text=" SSN -")
    fn_labela.grid(row=0, column=0, padx=10, pady=10)
    fn_entrya = Entry(data_framea)
    fn_entrya.grid(row=0, column=1, padx=10, pady=10)

    fn_label2a = Label(data_framea, text=" Name -")
    fn_label2a.grid(row=1, column=0, padx=10, pady=10)
    fn_entry2a = Entry(data_framea)
    fn_entry2a.grid(row=1, column=1, padx=10, pady=10)

    fn_label3a = Label(data_framea, text="Surname -")
    fn_label3a.grid(row=2, column=0, padx=10, pady=10)
    fn_entry3a = Entry(data_framea)
    fn_entry3a.grid(row=2, column=1, padx=10, pady=10)

    fn_label4a = Label(data_framea, text="Gender -")
    fn_label4a.grid(row=3, column=0, padx=10, pady=10)
    fn_entry4a = Entry(data_framea)
    fn_entry4a.grid(row=3, column=1, padx=10, pady=10)


    update_button3 = Button(data_framea, 
        text="Next", 
        command=lambda 
        SSN = fn_entrya,
        Name = fn_entry2a,
        Surname = fn_entry3a,
        Gender = fn_entry4a: last(SSN, Name, Surname, Gender) )
    update_button3.grid(row=4, column=1, padx=100, pady=10)
    successfullWindow.mainloop()
    
    """
    # 2022-01-06 11:00:00
    successfullWindow = Tk()
    successfullWindow.geometry("360x300")
    successfullWindow.title('successful')
    data_frame = LabelFrame(successfullWindow, text=" Thank You ! :) :) ")
    data_frame.pack(fill="x", expand="yes", padx=10)

    update_button2 = Button(data_frame, text="Quit",command=lambda: successfullWindow.destroy())
    update_button2.grid(row=0, column=0, padx=130, pady=10)
    successfullWindow.mainloop()"""

# selects selectable hairdresser, time, service
def nextSalonSelected(salonName):
    global salonWindow
    mycursor.execute("SELECT * FROM hairdressingsalon")
    mySalonName = str(salonName.get())
    print(" ",mySalonName)
    salonNames = []
    mySalonID = 0

    for i in mycursor:
        if(mySalonName == i[1]):
            print(i)
            
            mySalonID = i[0]
            print(mySalonID)
            myWorkingHours = i[3]
            print(myWorkingHours)
            #print("working time", myWorkingHours[:2]," - ",myWorkingHours[:2])
        salonNames.append(i[1])
    print(salonNames)


    for i in salonNames:
        if(mySalonName == i):
            print("found")
            print
            salonWindow = Tk()
            salonWindow.geometry("960x700")
            salonWindow.title('Book Window')
            mycursor.execute("SELECT * FROM Services")
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
            tree_frame = Frame(salonWindow)
            tree_frame.pack(padx= 0, pady=10)

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
            my_tree['columns'] = ("ServiceName","Price","processingTime")

            # Format Our Columns
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("ServiceName", anchor=W, width=180)
            my_tree.column("Price", anchor=W, width=120)
            my_tree.column("processingTime", anchor=W, width=140)


            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("ServiceName", text="ServiceName", anchor=W)
            my_tree.heading("Price", text="Price", anchor=W)
            my_tree.heading("processingTime", text="processingTime", anchor=W)
            salonSelected_query_database()

            # Create a Treeview Frame
            tree_frame2 = Frame(salonWindow)
            tree_frame2.pack(padx= 0, pady=10)

            # Create a Treeview Scrollbar
            tree_scroll2 = Scrollbar(tree_frame2)
            tree_scroll2.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            global my_tree2
            my_tree2 = ttk.Treeview(tree_frame2, yscrollcommand=tree_scroll2.set, selectmode="extended")
            my_tree2.pack()

            # Configure the Scrollbar
            tree_scroll2.config(command=my_tree2.yview)

            # Define Our Columns
            my_tree2['columns'] = ("HairdresserName","Gender","AVtime")

            # Format Our Columns
            my_tree2.column("#0", width=0, stretch=NO)
            my_tree2.column("HairdresserName", anchor=W, width=180)
            my_tree2.column("Gender", anchor=W, width=180)
            my_tree2.column("AVtime", anchor=W, width=180)


            # Create Headings
            my_tree2.heading("#0", text="", anchor=W)
            my_tree2.heading("HairdresserName", text="HairdresserName", anchor=W)
            my_tree2.heading("Gender", text="Gender", anchor=W)
            my_tree2.heading("AVtime", text="AVtime", anchor=W)
            salonSelected_query_database2(mySalonID)

            # Add Record Entry Boxes
            data_frame = LabelFrame(salonWindow, text="  Choose Service, Hairdresser and Time  ")
            data_frame.pack(fill="x", expand="yes", padx=10)

            fn_label = Label(data_frame, text="Service Name")
            fn_label.grid(row=0, column=0, padx=10, pady=10)
            fn_entry = Entry(data_frame)
            fn_entry.grid(row=0, column=1, padx=10, pady=10)

            fn_label2 = Label(data_frame, text="Hairdresser Name")
            fn_label2.grid(row=0, column=2, padx=10, pady=10)
            fn_entry2 = Entry(data_frame)
            fn_entry2.grid(row=0, column=3, padx=10, pady=10)

            fn_label3 = Label(data_frame, text="Booking Time")
            fn_label3.grid(row=1, column=0, padx=10, pady=10)
            fn_entry3 = Entry(data_frame)
            fn_entry3.grid(row=1, column=1, padx=10, pady=10)


            update_button2 = Button(data_frame, 
                text="Next", 
                command=lambda serviceName = fn_entry,
                hairDresserName = fn_entry2,
                bookedTime = fn_entry3: bookedSuccessfully(serviceName, hairDresserName, bookedTime))
            
            """            
            update_button2 = Button(data_frame, 
            text="Next", 
            command=lambda serviceName = fn_entry,
            hairDresserName = fn_entry2,
            bookedTime = fn_entry3: [bookedSuccessfully(serviceName, hairDresserName, bookedTime), delete()])"""


            update_button2.grid(row=1, column=3, padx=100, pady=10)
            
#The following 3 functions show the sql codes needed to create the tables
def salonSelected_query_database2(mysalonID):
    mycursor.execute("SELECT employee.name, employee.gender, avbDates.datetime FROM employee, avbDates WHERE employee.SSN = avbDates.employeeSSN and employee.salonID = '%s'" % mysalonID)
    #SELECT employee.name, employee.gender, avbDates.datetime FROM employee, avbDates WHERE employee.SSN = avbDates.employeeSSN
    records2 = mycursor.fetchall()
    print(records2)
    # Add our data to the screen
    global count
    count = 0

    for record in records2:
        if count % 2 == 0:
            my_tree2.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]) , tags=('evenrow',))
        else:
            my_tree2.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],record[2]), tags=('oddrow',))
        # increment counter
        count += 1
def salonSelected_query_database():
    mycursor.execute("SELECT * FROM Services")
    records = mycursor.fetchall()
    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        # increment counter
        count += 1
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

def query_databaseForCustomer():
    mycursor.execute("SELECT * FROM customer")
    records = mycursor.fetchall()
    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_treeC.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_treeC.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        # increment counter
        count += 1

def query_databaseForEmployee():
    mycursor.execute("SELECT * FROM employee")
    records = mycursor.fetchall()
    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_treeE.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_treeE.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        # increment counter
        count += 1


def hairDresserAdd(mySalonID,myHDSname,myAdress,myWorkingHours,myServeGender,myProvincePostCode):
    SCfavorNumber = 1
    newmySalonID =str(mySalonID.get())
    newmyHDSname = str(myHDSname.get())
    newmyAdress = str(myAdress.get())
    newmyWorkingHours = str(myWorkingHours.get())
    newmyServeGender = str(myServeGender.get())
    newmyProvincePostCode = str(myProvincePostCode.get())
    
    mycursor.execute("INSERT INTO HairdressingSalon VALUES(%s,%s,%s,%s,%s,%s,%s)", (int(newmySalonID), newmyHDSname, newmyAdress,int(newmyWorkingHours),newmyServeGender,SCfavorNumber,int(newmyProvincePostCode)))
    db.commit()
    salonID.delete(0,END)
    HDSname.delete(0,END)
    address.delete(0,END)
    workingHours.delete(0,END)
    serveGender.delete(0,END)
    #stars
    provincePostcode.delete(0,END)
    addWindow()
def hairDresserDrop(mySalonID2):
    newmySalonID =str(mySalonID2.get())
    mycursor.execute("DELETE FROM HairdressingSalon WHERE HairdressingSalon.salonID= '%s'" % newmySalonID)
    db.commit()
    print("DELETED")
    #clear the text boxes
    salonID.delete(0,END)
    HDSname.delete(0,END)
    address.delete(0,END)
    workingHours.delete(0,END)
    serveGender.delete(0,END)
    provincePostcode.delete(0,END)
    dropWindow()

def employeeAdd(mySSN,mysalonID2,mynameE,mygender):
    newmySSN =str(mySSN.get())
    newmysalonID2 = str(mysalonID2.get())
    newmynameE = str(mynameE.get())
    newmygender = str(mygender.get())
    mycursor.execute("INSERT INTO employee VALUES(%s,%s,%s,%s)", (int(newmySSN), int(newmysalonID2), newmynameE,newmygender))
    db.commit()
    SSN.delete(0,END)
    salonID2.delete(0,END)
    nameE.delete(0,END)
    gender.delete(0,END)
    addWindow()
def employeeDrop(mySSN,mynameE):
    # %(hairDresserName,bookedTime)
    newmySSN =str(mySSN.get())
    newmynameE = str(mynameE.get())
    intSSN = int(newmySSN)
    mycursor.execute("DELETE FROM employee WHERE employee.SSN= '%s' AND employee.name = '%s'" %(intSSN,newmynameE))
    db.commit()
    SSN.delete(0,END)
    salonID2.delete(0,END)
    nameE.delete(0,END)
    gender.delete(0,END)
    dropWindow()

# Window where add or drop all thinks.
def adminWindow():
    window2_main = Tk()
    window2_main.geometry("1100x500")
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
 
    hairDressingSalonAddButton = Button(window2_main, text ="Add", 
        command=lambda 
        mySalonID = salonID, 
        myHDSname = HDSname, 
        myAdress = address, 
        myWorkingHours = workingHours, 
        myServeGender = serveGender, 
        myProvincePostCode = provincePostcode: 
        hairDresserAdd(mySalonID,myHDSname,myAdress,myWorkingHours,myServeGender,myProvincePostCode))
    hairDressingSalonAddButton.place(x = 150, y = 220, width = 55)

    hairDressingSalonDropButton = Button(window2_main, text ="Drop", command=lambda  mySalonID2 = salonID : hairDresserDrop(mySalonID2))
    hairDressingSalonDropButton.place(x = 200, y = 220, width = 55)

    showHDSDBbtn = Button(window2_main, text ="Show Database", command = showHDSDB)
    showHDSDBbtn.place(x = 145, y = 250, width = 120)

    #-----------------------------------------

    #ADD NEW Employee
    titleOfAddHDS2 = Label(window2_main, text ="Add New Employee")
    titleOfAddHDS2.place(x = 350, y = 12)
    # Defining the first row
    lblfrstrow = Label(window2_main, text ="SSN -", )
    lblfrstrow.place(x = 350, y = 40)
    global SSN
    SSN = Entry(window2_main, width = 35)
    SSN.place(x = 450, y = 40, width = 100)
  
    # Defining the second row
    lblsecrow2 = Label(window2_main, text ="salonID -")
    lblsecrow2.place(x = 350, y = 70)
    global salonID2
    salonID2 = Entry(window2_main, width = 35)
    salonID2.place(x = 450, y = 70, width = 100)

    # Defining the third row
    lblthirdrow2 = Label(window2_main, text ="name -")
    lblthirdrow2.place(x = 350, y = 100)
    global nameE
    nameE = Entry(window2_main, width = 35)
    nameE.place(x = 450, y = 100, width = 100)
    # Defining the fourth row
    lblfourthrow2 = Label(window2_main, text ="gender -")
    lblfourthrow2.place(x = 350, y = 130)
    global gender
    gender = Entry(window2_main, width = 35)
    gender.place(x = 450, y = 130, width = 100)
    
    newEmployeeAddButton = Button(window2_main, text ="Add", command=lambda 
        mySSN = SSN, 
        mysalonID2 = salonID2, 
        mynameE = nameE, 
        mygender = gender:
        employeeAdd(mySSN,mysalonID2,mynameE,mygender) )
    newEmployeeAddButton.place(x = 450, y = 165, width = 55)
    newEmployeeDropButton = Button(window2_main, text ="Drop", command=lambda
        mySSN = SSN,
        mynameE = nameE:
        employeeDrop(mySSN,mynameE)
        )
    newEmployeeDropButton.place(x = 500, y = 165, width = 55)

    showHDSDBbtn2 = Button(window2_main, text ="Show Database", command = showemployeeDB)
    showHDSDBbtn2.place(x = 445, y = 195, width = 120)

    #-----------------------------------------

    #Services

    titleOfAddHDS3 = Label(window2_main, text ="Services")
    titleOfAddHDS3.place(x = 350, y = 270)
    

    # Defining the first row
    lblfrstrow3 = Label(window2_main, text ="name -", )
    lblfrstrow3.place(x = 350, y = 300)
 
    serviceName = Entry(window2_main, width = 35)
    serviceName.place(x = 450, y = 300, width = 100)
  
    # Defining the second row
    lblsecrow3 = Label(window2_main, text ="price -")
    lblsecrow3.place(x = 350, y = 330)
 
    price = Entry(window2_main, width = 35)
    price.place(x = 450, y = 330, width = 100)

    # Defining the third row
    lblthirdrow3 = Label(window2_main, text ="processingTime -")
    lblthirdrow3.place(x = 350, y = 360)
 
    processingTime = Entry(window2_main, width = 35)
    processingTime.place(x = 450, y = 360, width = 100)

    servicesAddButton = Button(window2_main, text ="Add")
    servicesAddButton.place(x = 450, y = 390, width = 55)

    servicesDropButton = Button(window2_main, text ="Drop")
    servicesDropButton.place(x = 500, y = 390, width = 55)


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
    titleOfAddHDS5.place(x = 600, y = 270)

    # Defining the first row
    lblfrstrow5 = Label(window2_main, text ="makeupSSN -", )
    lblfrstrow5.place(x = 600, y = 300)
 
    makeupSSN = Entry(window2_main, width = 35)
    makeupSSN.place(x = 700, y = 300, width = 100)

    lblsecrow5 = Label(window2_main, text ="certificateOfExpertise -", )
    lblsecrow5.place(x = 600, y = 330)
 
    certificateOfExpertise = Entry(window2_main, width = 35)
    certificateOfExpertise.place(x = 700, y = 330, width = 100)

    makeupArtistaddButton = Button(window2_main, text ="Add")
    makeupArtistaddButton.place(x = 700, y = 360, width = 55)

    makeupArtistDropButton = Button(window2_main, text ="Drop")
    makeupArtistDropButton.place(x = 750, y = 360, width = 55)


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

    adminPanelExitButton.place(x = 1000, y = 450)

    showHDSDBbtn2 = Button(window2_main, text ="Show Customers", command = showCustDB)
    showHDSDBbtn2.place(x = 45, y = 450, width = 120)

    window2_main.mainloop()

#Shows barber list
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
    my_tree['columns'] = ("salonID", "Name", "Address", "workingHours", "serveGender", "Rating", "PostCode")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("salonID", anchor=W, width=80)
    my_tree.column("Name", anchor=W, width=200)
    my_tree.column("Address", anchor=CENTER, width=220)
    my_tree.column("workingHours", anchor=CENTER, width=100)
    my_tree.column("serveGender", anchor=CENTER, width=100)
    my_tree.column("Rating", anchor=CENTER, width=70)
    my_tree.column("PostCode", anchor=CENTER, width=70)


    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("salonID", text="salonID", anchor=W)
    my_tree.heading("Name", text="Name", anchor=W)
    my_tree.heading("Address", text="Address", anchor=CENTER)
    my_tree.heading("workingHours", text="workingHours", anchor=CENTER)
    my_tree.heading("serveGender", text="serveGender", anchor=CENTER)
    my_tree.heading("Rating", text="Rating", anchor=CENTER)
    my_tree.heading("PostCode", text="PostCode", anchor=CENTER)


    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="#0c661b")
    my_tree.tag_configure('evenrow', background="#364238")


    # Run to pull data from database on start
    query_database()


    # Add Record Entry Boxes
    data_frame = LabelFrame(bookWindow, text="  Choose the Salon  ")
    data_frame.pack(fill="x", expand="yes", padx=180)

    fn_label = Label(data_frame, text="Hair Dressing Salon Name")
    fn_label.grid(row=0, column=0, padx=10, pady=10)
    fn_entry = Entry(data_frame)
    fn_entry.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(data_frame, text="Next", command=lambda salonName = fn_entry: nextSalonSelected(salonName))
    update_button.grid(row=0, column=50, padx=100, pady=10)
        


    bookWindow.mainloop()


# Create object
root = Tk()

# Adjust size
root.geometry("960x540")
root.title('Demo')
# Add image file
bg = PhotoImage(file = "hairBG.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")


# Create Buttons
button1 = Button( root, text = "Admin Login",command = adminLoginWindow)
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
