from tkinter import *
from tkinter import ttk
import mysql.connector


db = mysql.connector.connect(host = "localhost",user = "root",passwd = "MySQL2020.", database = "hairDresser")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM hairdressingsalon")
records = mycursor.fetchall()
for i in records:
	print(i)



#  c    - mycursor, 
#  conn - db
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


root = Tk()
root.title('Codemy.com - TreeBase')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x500")


# Add Some Style
style = ttk.Style()

# Pick A Theme
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
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("salonID", "Name", "Address", "workingHours", "serveGender", "Stars", "PostCode")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("salonID", anchor=W, width=140)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("Address", anchor=CENTER, width=100)
my_tree.column("workingHours", anchor=CENTER, width=140)
my_tree.column("serveGender", anchor=CENTER, width=140)
my_tree.column("Stars", anchor=CENTER, width=140)
my_tree.column("PostCode", anchor=CENTER, width=140)


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
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")





# Run to pull data from database on start
query_database()


root.mainloop()