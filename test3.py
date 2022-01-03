from tkinter import *
successfullWindow = Tk()
successfullWindow.geometry("360x300")
successfullWindow.title('successful')
data_frame = LabelFrame(successfullWindow, text=" Thank You ! :) :) ")
data_frame.pack(fill="x", expand="yes", padx=10)

update_button2 = Button(data_frame, text="Quit",command=lambda: successfullWindow.destroy())
update_button2.grid(row=0, column=0, padx=130, pady=10)
successfullWindow.mainloop()