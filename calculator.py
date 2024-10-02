import tkinter
from tkinter import *

root = Tk()
root.title("CALCULATOR (made by Sabit29)")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg = '#17161b')

equation = ""

def clear():
    global equation
    equation = ""
    label_mathisshit.config(text=equation)

def show(value):
    global equation
    equation = equation + value
    label_mathisshit.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = str(result)
        except:
            result = "error"
            equation = ""
    label_mathisshit.config(text=result)

label_mathisshit = Label(root, width = 25, height= 2 , text = "", font = ("arial", 30))
label_mathisshit.pack()


Button(root, width=5, height=1, text="C", font=("arial", 30, "bold"), bd=1, bg="#034fff", fg="#ffffff", command = lambda: clear()).place(x=10, y=100)
Button(root, width=5, height=1, text="/", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("/")).place(x=150, y=100)
Button(root, width=5, height=1, text="%", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("%")).place(x=290, y=100)
Button(root, width=5, height=1, text="*", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("*")).place(x=430, y=100)

Button(root, width=5, height=1, text="7", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("7")).place(x=10, y=200)
Button(root, width=5, height=1, text="8", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("8")).place(x=150, y=200)
Button(root, width=5, height=1, text="9", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("9")).place(x=290, y=200)
Button(root, width=5, height=1, text="-", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("-")).place(x=430, y=200)

Button(root, width=5, height=1, text="4", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("4")).place(x=10, y=300)
Button(root, width=5, height=1, text="5", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("5")).place(x=150, y=300)
Button(root, width=5, height=1, text="6", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("6")).place(x=290, y=300)
Button(root, width=5, height=1, text="+", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("+")).place(x=430, y=300)

Button(root, width=5, height=1, text="3", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("3")).place(x=10, y=400)
Button(root, width=5, height=1, text="2", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("2")).place(x=150, y=400)
Button(root, width=5, height=1, text="1", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("1")).place(x=290, y=400)

Button(root, width=11, height=1, text="0", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show("0")).place(x=10, y=500)
Button(root, width=5, height=1, text=".", font=("arial", 30, "bold"), bd=1, bg="#1f1f1f", fg="#ffffff", command = lambda: show(".")).place(x=290, y=500)
Button(root, width=5, height=3, text="=", font=("arial", 30, "bold"), bd=1, bg="#ff6c03", fg="#ffffff", command = lambda: calculate()).place(x=430, y=400)



root.mainloop()