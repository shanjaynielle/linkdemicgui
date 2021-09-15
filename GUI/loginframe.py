from tkinter import *

#FUNCTIONS
def MainFrame():
    print("Button Clicked")
    #temp_un = username.get()
    #temp_pw = password.get()

    #if(temp_un == "admin" and temp_pw == "admin"):
            #username.set("")
            #password.set("")
                                    
            #hide_window()
            #main_window = MainFrame()
    #else:
        #print("Invalid credentials")

def hide_window(self):
        self.withdraw()

#LOGIN FRAME ATTRIBUTES
loginframe = Tk()
loginframe.geometry("730x490")
loginframe.configure(bg = "#cbebef")
loginframe.title("Linkdemic: Login Frame")
canvaslogin = Canvas(loginframe,
    bg = "#cbebef",height = 490,width = 730,
    bd = 0,highlightthickness = 0,relief = "ridge")
canvaslogin.place(x = 0, y = 0)

#VARIABLES
#username = StringVar()
#password = StringVar()

#BACKGROUND
background_img = PhotoImage(file = f"backgroundl.png")
background = canvaslogin.create_image(304.0, 247.0,image=background_img)

#TEXTBOX
username = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0,
    font="Helvetica", fg="#04BFAD")
username.place(x = 450, y = 218,width = 215,height = 34)

password = Entry(
    bd = 0,bg = "#ffffff",highlightthickness = 0, show="*",
    fg="#04BFAD")
password.place(x = 450, y = 298,width = 215,height = 34)

#BUTTON
imgbutton = PhotoImage(file = f"limg0.png")
loginbutton = Button(image = imgbutton,borderwidth = 0,highlightthickness = 0,
command = MainFrame,relief = "flat")
loginbutton.place(x = 478, y = 381,width = 120,height = 54)

#LOOP
loginframe.resizable(False, False)
loginframe.mainloop()
