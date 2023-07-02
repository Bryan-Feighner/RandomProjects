import tkinter as tk


expression = ""
def buttonPress(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalsPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("You have made an error, try again.")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
window = tk.Tk()
equation = tk.StringVar()
greeting = tk.Label(text = "Calculator", font= ('Times', 30))
greeting.pack()

frame = tk.Frame(master= window, width = 250, height= 250)
frame.pack()
expressionFrame = tk.Entry(frame, textvariable=equation, font= ('Arial', 25))
expressionFrame.grid(row=0,columnspan=4)
button1 = tk.Button(master=frame,
    text="1",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(1))
button1.grid(row=1,column=0)
button2 = tk.Button(master=frame,
    text="2",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(2))
button2.grid(row=1,column=1)
button3 = tk.Button(master=frame,
    text="3",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(3))
button3.grid(row=1,column=2)
button4 = tk.Button(master=frame,
    text="4",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(4))
button4.grid(row=2,column=0)
button5 = tk.Button(master=frame,
    text="5",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(5))
button5.grid(row=2,column=1)
button6 = tk.Button(master=frame,
    text="6",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(6))
button6.grid(row=2,column=2)
button7 = tk.Button(master=frame,
    text="7",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(7))
button7.grid(row=3,column=0)
button8 = tk.Button(master=frame,
    text="8",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(8))
button8.grid(row=3,column=1)
button9 = tk.Button(master=frame,
    text="9",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(9))
button9.grid(row=3,column=2)
button0 = tk.Button(master=frame,
    text="0",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress(0))
button0.grid(row=4,column=1)
buttonPlus = tk.Button(master=frame,
    text="+",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("+"))
buttonPlus.grid(row=4,column=3)
buttonMinus = tk.Button(master=frame,
    text="-",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("-"))
buttonMinus.grid(row=3,column=3)
buttonTimes = tk.Button(master=frame,
    text="X",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("*"))
buttonTimes.grid(row=2, column=3)
buttonDivide = tk.Button(master=frame,
    text="÷",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("/"))
buttonDivide.grid(row=1,column=3)
buttonEquals = tk.Button(master=frame,
    text="=",
    width=31,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: equalsPress())
buttonEquals.grid(row=5,column=2, columnspan=2)
buttonClear = tk.Button(master=frame,
    text="Clear",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: clear())
buttonClear.grid(row=4,column=0)
buttonDecimal = tk.Button(master=frame,
    text=".",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("."))
buttonDecimal.grid(row=4,column=2)
buttonCarrot = tk.Button(master=frame,
    text="^ (Exponential)",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,command=lambda: buttonPress("**"))
buttonCarrot.grid(row=5,column=0)
buttonCarrot = tk.Button(master=frame,
    text="Square Root",
    width=15,
    height=5,
    bg="gray",
    fg="black",
    relief=tk.RAISED,comman d=lambda: buttonPress("**.5"))
buttonCarrot.grid(row=5,column=1)
tk.mainloop()
