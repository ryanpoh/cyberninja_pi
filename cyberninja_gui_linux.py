from tkinter import *
from PIL import Image, ImageTk
import os

img_path = '/home/pi/Downloads/cyberninja_gui.png'

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Cyberninja Beta")
        self.pack(fill=BOTH, expand=1)
        
        
        helpButton = Button(self, text="Help", command=self.show_help)
        helpButton.pack(side="top", fill="x", expand=False)
        #helpButton.place(x=40,y=0) 
        

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0,y=0)

        connectButton = Button(self, text="Connect to Cyberninja Pro", command=self.parsec_connect)
        connectButton.place(relx=0.5, rely=0.5, anchor=CENTER)  #center the widget


    def client_exit(self):
        exit()

    def parsec_connect(self):
        os.system("parsec server_id=580615")
        
    def show_help(self):
        text = Label(self, text="Contact us at ryan.poh@gmail.com or yewwey@gmail.com")
        text.pack()
        
##    def first_time_login(self):
##        os.system('printf ryan.poh@gmail.com\nuc"u^S-H`3,Q4z2m\n1 | ./parsec')
##        os.system("""parsec & ryan.poh@gmail.com & uc"u^S-H`3,Q4z2m & 1""")
##        
##        os.system("ryan.poh@gmail.com")
##        os.system('uc"u^S-H`3,Q4z2m')
##        
##    def showImg(self):
##        load = Image.open('photo6316383144533665842.jpg')
##        render = ImageTk.PhotoImage(load)
##        
##        img = Label(self, image=render)
##        img.image = render
##        img.place(x=100, y=150)
        
        


root = Tk()
root.geometry("400x300")

img = ImageTk.PhotoImage(Image.open(img_path))
panel = Label(root, image=img, height=100)
panel.pack(side = "bottom", fill = "x", expand=0)


app = Window(root)
root.mainloop()