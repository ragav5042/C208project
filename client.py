import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window=Tk()

    window.title('Music Window')
    window.geometry("500x350")
    window.configure(bg='LightSkyBlue')

    selectlabel = Label (window, text="Select Song",bg='LightSkyBlue', font = ("Calibri",0)) 
    selectlabel.place (x=2, y=1)

    listbox=Listbox (window, height =10, width =39, activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font=("Calibri",10)) 
    listbox.place (x=10,y=18)

    scrollbarl = Scrollbar (listbox)
    scrollbarl.place (relheight=1,relx=1)
    scrollbarl.config(command = listbox.yview)

    playButton=Button(window, text="Play", width=10,bd=1,bg="SkyBlue", font=("Calibri",10)) 
    playButton.place(x=30,y=200)

    stop=Button (window, text="Stop",bd=1,width=10,bg="SkyBlue", font = ("Calibri",10)) 
    stop.place (x=200,y=200)

    upload=Button (window, text="Upload",width=10,bd=1,bg='SkyBlue', font= ("Calibri",10)) 
    upload.place (x=30,y=250)

    download =Button (window, text="Download", width=10,bd=1,bg="SkyBlue", font = ("Calibri",10)) 
    download.place (x=200,y=250)

    infoLabel= Label (window, text="",fg= "blue", font =("Calibri",8))
    infoLabel.place (x=4, y=280)

    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
    

setup()
