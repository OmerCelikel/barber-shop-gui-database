import mysql.connector
import tkinter as tk
from tkinter import ttk



db = mysql.connector.connect(host = "localhost",user = "root",passwd = "MySQL2020.", database = "test")



mycursor = db.cursor()


#mycursor.execute("SELECT * FROM Bars")
#mycursor.execute("INSERT INTO Bars (name,adress,license) VALUES (%s,%s,%s)", ("YT","Malatya","Dev"))
#db.commit() #save changes

def allBars(): 
    savequery = "INSERT INTO Bars (name,adress,license) VALUES (%s,%s,%s)"
    val = ("aa","bb","cc")
    try:
        mycursor.execute(savequery, val)
        db.commit()
        myresult = mycursor.fetchall()
        
         
    except:
        db.rollback()
        print("Error occured")


mycursor.execute("SELECT * FROM Bars")
for i in mycursor:
	print(i)

# root window
root = tk.Tk()
root.geometry('400x200')
root.resizable(False, False)
root.title('Demo')

# add button
add_button = ttk.Button(
    root,
    text='Add New Bar',
    command= allBars
)
db.commit()
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
