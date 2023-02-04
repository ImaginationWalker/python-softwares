from guizero import *
from tkinter import *

root = Tk()
root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(background='white')
def hello():
    print("hello!")


menubar = Menu(root, relief=FLAT, bd=0)

# Sets menubar background color and active select but does not remove 3d  effect/padding
menubar.config(bg="GREEN", fg='white', activebackground='blue', activeforeground='white',relief=FLAT)

filemenu = Menu(menubar, tearoff=0, relief=FLAT, font=("Verdana", 12),activebackground='red')
filemenu.config(bg="GREEN")
filemenu.add_command(label="New (Ctrl + N)", command=hello)
filemenu.add_command(label="Save(Ctrl + S)", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0, bg='green',fg='white')

helpmenu.add_command(label="Report bug", command=hello)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.activebackground='red'

label = Label(root, text='First Name', background='white', fg='black')
label.place(relx=0.2, rely=0.5, relheight=0.04, relwidth=0.25)

name = Entry(root, bg='white', fg='black')
name.place(relx=0.4, rely=0.51, relheight=0.03, relwidth=0.2)

label1 = Label(root, text='Last Name', background='white', fg='black')
label1.place(relx=0.2, rely=0.6, relheight=0.04, relwidth=0.25)

name1 = Entry(root, bg='white', fg='black')
name1.place(relx=0.4, rely=0.61, relheight=0.03, relwidth=0.2)

label2 = Button(root, text='Submit', background='green', activeforeground='white', activebackground='brown',
                highlightthickness=0)
label2.place(relx=0.4, rely=0.71, relheight=0.04, relwidth=0.2)

root.mainloop()
