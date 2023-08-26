from tkinter import *

def display(num):
    
    global text_var
    text_var = text_var + str(num)
    text_lab.set(text_var)

def equal():

    try:
        global text_var
        result = str(eval(text_var))
        text_lab.set(result)
        text_var = result

    except ZeroDivisionError:
        text_lab.set("Can't Divide By Zero")

    except SyntaxError:
        text_lab.set("Syntax Error")

def clear():
    
    global text_var
    text_lab.set("")
    text_var = ""

window = Tk()

text_var = ""

text_lab = StringVar()

Label(window,text="GUI Calculator",font=("helvetica",20)).pack()

label = Label(window,textvariable=text_lab,bg="white",width=24,height=2,font=("Consolas",20))
label.pack()

frame = Frame(window)
frame.pack()

Button(frame,text="Clear",height=4,width=9,font=35,command = clear).grid(row=0,column=0)
Button(frame,text="%",height=4,width=9,font=35,command = lambda : display("%")).grid(row=0,column=1)
Button(frame,text="/",height=4,width=9,font=35,command = lambda : display("/")).grid(row=0,column=2)
Button(frame,text="X",height=4,width=9,font=35,command = lambda : display("*")).grid(row=0,column=3)
Button(frame,text=7,height=4,width=9,font=35,command = lambda : display(7)).grid(row=1,column=0)
Button(frame,text=8,height=4,width=9,font=35,command = lambda : display(8)).grid(row=1,column=1)
Button(frame,text=9,height=4,width=9,font=35,command = lambda : display(9)).grid(row=1,column=2)
Button(frame,text="-",height=4,width=9,font=35,command = lambda : display("-")).grid(row=1,column=3)
Button(frame,text=4,height=4,width=9,font=35,command = lambda : display(4)).grid(row=2,column=0)
Button(frame,text=5,height=4,width=9,font=35,command = lambda : display(5)).grid(row=2,column=1)
Button(frame,text=6,height=4,width=9,font=35,command = lambda : display(6)).grid(row=2,column=2)
Button(frame,text="+",height=4,width=9,font=35,command = lambda : display("+")).grid(row=2,column=3)
Button(frame,text=1,height=4,width=9,font=35,command = lambda : display(1)).grid(row=3,column=0)
Button(frame,text=2,height=4,width=9,font=35,command = lambda : display(2)).grid(row=3,column=1)
Button(frame,text=3,height=4,width=9,font=35,command = lambda : display(3)).grid(row=3,column=2)
Button(frame,text=".",height=4,width=9,font=35,command = lambda : display(".")).grid(row=3,column=3)
Button(frame,text=0,height=4,width=9,font=35,command = lambda : display(0)).grid(row=4,column=0)
Button(frame,text="00",height=4,width=9,font=35,command = lambda : display(00)).grid(row=4,column=1)
Button(frame,text="=",height=4,width=9,font=35,command = equal).grid(row=4,column=2)

window.mainloop()