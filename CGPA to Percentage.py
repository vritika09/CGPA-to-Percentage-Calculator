from tkinter import *
import tkinter


root = Tk()
root.title("CGPA to Percentage Calculator")
root.geometry("500x300")
root.resizable(0,0)

def Calculate():

    v = float(cgpavalue.get())
    result = v * 9.5
    Label(text=f"Result = {result:.2f}", font='arial 20 bold').place(x = 150, y = 90)


cgpa = Label(root, text= "Enter Your CGPA :", font='arial 18').place(x= 20, y = 30)


cgpavalue = StringVar()
cgpaentry = Entry(root,width=15, font='arial 18',textvariable=cgpavalue).place(x = 250, y = 30)


Button(root, text="Calculate Percentage", font='arial 14',command=Calculate).place(x = 100, y = 150)
Button(root, text="Exit", font="arial 14", padx = 15,command=lambda:exit()).place(x = 350 ,y = 150)



root.mainloop()