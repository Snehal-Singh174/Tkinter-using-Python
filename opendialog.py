from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()

def open():
    global my_img
    root.filename=filedialog.askopenfilename(initialdir="C:/Users/Snehal/Pictures",title="Select a file",filetype=(("jpg files","*.png"),("all files","*.*")))
    mylabel=Label(root,text=root.filename).pack()
    my_img=ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label=Label(image=my_img).pack()

my_btn=Button(root,text="open file",command=open).pack()
