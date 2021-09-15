from tkinter import *


#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#def Refresh():
#def Back():
#def open_register():

#RECORDS FRAME ATTRIBUTES
recordsframe = Tk()
recordsframe.geometry("700x450")
recordsframe.configure(bg = "#ffffff")
recordsframe.title("Linkdemic: Records Frame")
canvas = Canvas(recordsframe,
    bg = "#ffffff",height = 450,width = 700,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundrec.png")
background = canvas.create_image(350.0, 225.0,image=background_img)

#BUTTONS
imgback = PhotoImage(file = f"recmg0.png")
backbutton = Button(image = imgback,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
backbutton.place(x = 72, y = 371,width = 69,height = 58)

imgrefresh = PhotoImage(file = f"recmg1.png")
refreshbutton = Button(image = imgrefresh,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
refreshbutton.place(x = 545, y = 371,width = 76,height = 58)

imgregister = PhotoImage(file = f"recmg2.png")
registerbutton = Button(image = imgregister,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
registerbutton.place(x = 253, y = 369,width = 194,height = 62)

#LOOP
recordsframe.resizable(False, False)
recordsframe.mainloop()
