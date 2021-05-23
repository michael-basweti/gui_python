from tkinter import *
from tkinter import filedialog, Text
import os

root = Tk()
apps = []

def addApp():
    # for widget in frame.winfo_children():
    #     widget.destory()
    children = frame.winfo_children()
    for label in children:
        print(label)
        label.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables",".exe"),("all files","*")))
    apps.append(filename)


    for app in apps:
        label = Label(frame, text=app, bg='gray')
        label.pack()
        print(label)

canvas = Canvas(root, height=700, width=700, bg="#439cd3")
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = Button(root, text='Open File', padx=10,pady=5,fg="white", bg="#439cd3", command=addApp)
openFile.pack()

runApps = Button(root, text='Run Apps', padx=10,pady=5,fg="white", bg="#439cd3")

runApps.pack()

root.mainloop()