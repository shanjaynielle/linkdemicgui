from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#def Refresh():
#def Back():

#GEOCODES FRAME ATTRIBUTES
geocodesframe = Tk()
geocodesframe.geometry("700x450")
geocodesframe.configure(bg = "#ffffff")
geocodesframe.title("Linkdemic: Geocodes Frame")
canvas = Canvas(geocodesframe,
    bg = "#ffffff",height = 450,width = 700,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundgeo.png")
background = canvas.create_image(350.0, 225.0,image=background_img)

#BUTTONS
imgback = PhotoImage(file = f"geoimg0.png")
backbutton = Button(image = imgback,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
backbutton.place(x = 72, y = 371,width = 69,height = 58)

imgrefresh = PhotoImage(file = f"geoimg1.png")
refreshbutton = Button(image = imgrefresh,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
refreshbutton.place(x = 545, y = 371,width = 76,height = 58)

geocodesframe.resizable(False, False)
geocodesframe.mainloop()
