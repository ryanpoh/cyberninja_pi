from tkinter import *
import os

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Cyberninja GUI")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="QUIT", command=self.client_exit)
        quitButton.place(x=0,y=0)

        gamingButton = Button(self, text="gaming", command=self.parsec_liquidsky)
        gamingButton.place(x=0,y=50)

        generalButton = Button(self, text="general", command=self.parsec_general_shadow)
        generalButton.place(x=0,y=100)


    def client_exit(self):
        exit()

    def parsec_liquidsky(self):
        os.system("parsec server_id=YOUR_SERVER_ID")



    def parsec_general_shadow(self):
        os.system("parsec server_id=YOUR_SERVER_ID")



root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()