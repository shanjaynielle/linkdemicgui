from tkinter import *
from tkinter import messagebox


#FUNCTIONS
def Clear():
    msgBox = messagebox.askquestion('Confirm', 'Clear entry?', icon = 'info')
    if msgBox == 'yes':
        enternum.delete(0, END)

def Register():
    msgBox = messagebox.askquestion('Confirm', 'Do you want to register number?', icon = 'info')
    if msgBox == 'yes':
        messagebox.showinfo('Confirm', 'Number registered successfully!', icon = 'info')
        registerframe.destroy()

def Exit():
    msgBox = messagebox.askquestion('Exit', 'Are you sure you want to exit?', icon = 'error')
    if msgBox == 'yes':
        registerframe.destroy()
       # recordsframe.show()

#REGISTER FRAME ATTRIBUTES
registerframe = Tk()
registerframe.geometry("340x450")
registerframe.configure(bg = "#ffffff")
canvas = Canvas(registerframe,
    bg = "#ffffff",height = 450,width = 340,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundreg.png")
background = canvas.create_image(170.0, 226.0,image=background_img)

#BUTTONS
imgregnum = PhotoImage(file = f"regimg0.png")
registernumbutton = Button(image = imgregnum,borderwidth = 0,highlightthickness = 0,
    command = Register,relief = "flat")
registernumbutton.place(x = 87, y = 367,width = 189,height = 62)

imgclear = PhotoImage(file = f"regimg1.png")
clearbutton = Button(image = imgclear,borderwidth = 0,highlightthickness = 0,
    command = Clear,relief = "flat")
clearbutton.place(x = 7, y = 305,width = 174,height = 62)

imgexit = PhotoImage(file = f"regimg2.png")
exitbutton = Button(image = imgexit,borderwidth = 0,highlightthickness = 0,
    command = Exit,relief = "flat")
exitbutton.place(x = 184, y = 305,width = 162,height = 62)

#TEXTBOX
entrynum_img = PhotoImage(file = f"img_textBox0.png")
enternum = canvas.create_image(182.0, 168.0,image = entrynum_img)
enternum = Entry(bd = 0,bg = "#cbebef",highlightthickness = 0)
enternum.place(x = 76, y = 150,width = 212,height = 34)

#LOOP
registerframe.resizable(False, False)
registerframe.mainloop()
