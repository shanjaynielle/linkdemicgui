from tkinter import *

#FUNCTIONS
def btn_clicked():
    print("Button Clicked")

#def Refresh():
#def Back():
#def StartSimulation():

#CLUSTERING FRAME ATTRIBUTES
clusteringframe = Tk()
clusteringframe.geometry("700x450")
clusteringframe.configure(bg = "#ffffff")
clusteringframe.title("Linkdemic: Clustering Frame")
canvas = Canvas(clusteringframe,
    bg = "#ffffff",height = 450,width = 700,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#BACKGROUND
background_img = PhotoImage(file = f"backgroundscf.png")
background = canvas.create_image(350.0, 225.0,image=background_img)

#BUTTONS
imgback = PhotoImage(file = f"scimg0.png")
backbutton = Button(image = imgback,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
backbutton.place(x = 72, y = 371,width = 69,height = 58)

imgrefresh = PhotoImage(file = f"scimg1.png")
refreshbutton = Button(image = imgrefresh,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
refreshbutton.place(x = 545, y = 371,width = 76,height = 58)

imgstart = PhotoImage(file = f"scimg2.png")
startbutton = Button(image = imgstart,borderwidth = 0,highlightthickness = 0,
    command = btn_clicked,relief = "flat")
startbutton.place(x = 253, y = 369,width = 194,height = 62)

#LOOP
clusteringframe.resizable(False, False)
clusteringframe.mainloop()
