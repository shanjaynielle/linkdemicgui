from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

def Open_viewrecords():
    print("Button Clicked")

def Retrieve():
    print(combo.get())

def Logout():
    msgBox = messagebox.askquestion('Logout', 'Are you sure you want to logout?', icon = 'error')
    if msgBox == 'yes':
        mainframe.destroy()

def ChatbotPower():
    msgBox1 = messagebox.askquestion('Power', 'Power off?', icon='error')
    if msgBox1 == 'yes':
        messagebox.showwarning("Off", "Turning Off")

#MAIN FRAME ATTRIBUTES
mainframe = Tk()
mainframe.geometry("700x450")
mainframe.configure(bg = "#ffffff")
mainframe.title("Linkdemic: Main Frame")
canvas = Canvas(mainframe,
    bg = "#ffffff",height = 450,width = 700,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundmf.png")
background = canvas.create_image(350.0, 225.0,image=background_img)

#STATUS
canvas.create_text(
    125.0, 322.5,
    text = "Status: Idle",
    fill = "#04bfad",
    font = ("Medel-Regular", int(14.0)))

#BUTTONS
#POWERBUTTON
imgpower = PhotoImage(file = f"mfimg0.png")
powerbutton = Button(image = imgpower, borderwidth = 0,highlightthickness = 0,
    command = ChatbotPower,relief = "flat")
powerbutton.place(x = 77, y = 213,width = 95,height = 84)

#VIEW RECORDS BUTTON
imgvr = PhotoImage(file = f"mfimg1.png")
viewrecbutton = Button(image = imgvr,borderwidth = 0,highlightthickness = 0,
    command = Open_viewrecords,relief = "flat")
viewrecbutton.place(x = 71, y = 340,width = 107,height = 43)

#START GEOCODES BUTTON
imgsg = PhotoImage(file = f"mfimg2.png")
startgeobutton = Button(image = imgsg,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
startgeobutton.place(x = 292, y = 225,width = 117,height = 53)

#VIEW GEOCODES BUTTON
imgvg = PhotoImage(file = f"mfimg3.png")
viewgeobutton = Button(image = imgvg,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
viewgeobutton.place(x = 291, y = 281,width = 118,height = 44)

#START CLUSTERING BUTTON
imgscb = PhotoImage(file = f"mfimg4.png")
startclusbutton = Button(image = imgscb,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
startclusbutton.place(x = 514, y = 233,width = 122,height = 45)

#VIEW MAP BUTTON
imgvm = PhotoImage(file = f"mfimg5.png")
viewmapbutton = Button(image = imgvm,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
viewmapbutton.place(x = 514, y = 285,width = 122,height = 40)

#LOGOUT BUTTON
imglogout = PhotoImage(file = f"mfimg6.png")
logoutbutton = Button(image = imglogout,borderwidth = 0,highlightthickness = 0,
    command = Logout,relief = "flat")
logoutbutton.place(x = 561, y = 105,width = 118,height = 33)


#DISEASE DROP DOWN
list = ["COVID-19", "DENGUE","LEPTOSPIROSIS", "TUBERCULOSIS"]
combo = ttk.Combobox(mainframe, values=list, state="readonly")
combo.set("Disease")
combo.place(x=130, y=108)

#SUBMIT BUTTON
imgsub = PhotoImage(file=f"imgsubmit.png")
diseasebutton = Button(mainframe, image=imgsub,
    command=Retrieve, relief="flat")
diseasebutton.place(x=290, y=95)


#LOOP
mainframe.resizable(False, False)
mainframe.mainloop()
