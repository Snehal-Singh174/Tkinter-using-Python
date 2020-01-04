from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("First Window")

def open():
    global my_img
    top=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("C:/Users/Snehal/Pictures/img3.jpg"))
    top.title("Second Window")
    my_label=Label(top,image=my_img).pack()

btn=Button(root,text="Open Second Window",command=open).pack()

root.mainloop()
