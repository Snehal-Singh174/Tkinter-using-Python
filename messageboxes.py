from tkinter import *
from tkinter import messagebox

root=Tk()

#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def info():
    response=messagebox.showinfo("This is my popup","Snehal")
    Label(root,text=response).pack()
def warning():
    response=messagebox.showwarning("This is my popup","Don't xxxx")
    Label(root,text=response).pack()
def error():
    response=messagebox.showerror("This is my popup","Hello World")
    Label(root,text=response).pack()
def question():
    response=messagebox.askquestion("This is my popup","Your program is still running!\n Do you want to kill it?")
    Label(root,text=response).pack()
    if response == 1:
        Label(root,text="You clicked Yes").pack()
    else:
        Label(root,text="You clicked No").pack()
def ok():
    response=messagebox.askokcancel("This is my popup","Your program is still running!\n Do you want to kill it?")
    Label(root,text=response).pack()
    if response == 1:
        Label(root,text="You clicked OK").pack()
    else:
        Label(root,text="You clicked Cancel").pack()
def yes():
    response=messagebox.askyesno("This is my popup","Your program is still running!\n Do you want to kill it?")
    Label(root,text=response).pack()
    if response == 1:
        Label(root,text="You clicked Yes").pack()
    else:
        Label(root,text="You clicked No").pack()

b=Button(root,text="info",command=info).pack(pady=10)
b=Button(root,text="warning",command=warning).pack(pady=10)
b=Button(root,text="error",command=error).pack(pady=10)
b=Button(root,text="question",command=question).pack(pady=10)
b=Button(root,text="ok/cancel",command=ok).pack(pady=10)
b=Button(root,text="yes/no",command=yes).pack(pady=10)

root.mainloop()
