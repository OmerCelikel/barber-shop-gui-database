from tkinter import *
window2_main = Tk()
window2_main.geometry("1100x400")
window2_main.title('Demo')
Label(window2_main).pack()

def cal_sum():

    print(type(salonID))
    t2=str(salonID.get())
    print(t2)
    print(type(t2))
#-----------------------------------------
#ADD NEW HairDresser Saloon

titleOfAddHDS = Label(window2_main, text ="Add New HairDresser Saloon")
titleOfAddHDS.place(x = 50, y = 12)
# Defining the first row
lblfrstrow = Label(window2_main, text ="salonID -", )
lblfrstrow.place(x = 50, y = 40)

salonID = Entry(window2_main, width = 35)
salonID.place(x = 150, y = 40, width = 100)

 
hairDresserAddButton = Button(window2_main, text ="Add",command = cal_sum)
hairDresserAddButton.place(x = 950, y = 100, width = 55)

hairDresserDropButton = Button(window2_main, text ="Drop")
hairDresserDropButton.place(x = 1000, y = 100, width = 55)

#-----------------------------

window2_main.mainloop()