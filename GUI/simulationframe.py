from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#def Back()
#def Prev():
#def Next():

#SIMULATION FRAME ATTRIBUTES
simulationframe = Tk()
simulationframe.geometry("700x450")
simulationframe.configure(bg = "#ffffff")
simulationframe.title("Linkdemic: Simulation Frame")
canvas = Canvas(simulationframe,
    bg = "#ffffff",height = 450,width = 700,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundsim.png")
background = canvas.create_image(
    350.0, 225.0,
    image=background_img)

#BUTTONS
imgback = PhotoImage(file = f"simimg0.png")
backbutton = Button(image = imgback,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
backbutton.place(x = 40, y = 371,width = 132,height = 58)

imgprev = PhotoImage(file = f"simimg1.png")
prevbutton = Button(image = imgprev,
    borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
prevbutton.place(x = 557, y = 371,width = 122,height = 58)

imgnext = PhotoImage(file = f"simimg2.png")
nextbutton = Button(image = imgnext,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
nextbutton.place(x = 448, y = 371,width = 109,height = 58)

#LOOP
simulationframe.resizable(False, False)
simulationframe.mainloop()
