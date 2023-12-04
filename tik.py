# # import tkinter as tk
# # class Application(tk.Frame):
# #     def __init__(self, master=None):
# #         super().__init__(master)
# #         self.pack()
# #         self.create_widgets()

# #     def create_widgets(self):
# #         self.hi_there = tk.Button(self)
# #         self.hi_there["text"] = "Hello World\n(click me!!!!!!)"
# #         self.hi_there["command"] = self.say_hi
# #         self.hi_there.pack(side="left")

# #         self.quit = tk.Button(self, text="QUIT", fg="yellow",
# #                               command=root.destroy)
# #         self.quit.pack(side="bottom")

# #     def say_hi(self):
# #         print("hi there, everyone!")

# # root = tk.Tk()
# # app = Application(master=root)
# # app.mainloop()

# from tkinter import *
# from PIL import ImageTk,Image
# window=Tk()
# # add widgets here

# lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)

# but=Label(window,text="hello world",fg='blue')
# but.place(x=80,y=100)

# txtfld=Entry(window, text="This is Entry Widget", bd=5)
# txtfld.place(x=80, y=150)


# frame = Frame(window, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

# img=ImageTk.PhotoImage(Image.open("./tl.png"))
# label=Label(frame,image=img)
# label.pack()

# txtfld2=Entry(window, text="This is Entry Widget", bd=5)
# txtfld2.place(x=80, y=150)

# def goTo():
#     global Entry
#     print(txtfld2.get())
#     # print("This is Entry Widget")
# but2=Button(window,text="This is Entry Widget" ,command=goTo())
# but2.place(x=50,y=80)
# window.title('Hello Python')
# window.geometry("300x200+70+60")
# window.mainloop()


#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry

   string= entry.get()
   print('string')
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()
