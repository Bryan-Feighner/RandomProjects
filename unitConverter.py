from tkinter import *
def convert(value, type1, type2):
    global convertedValue
    if(type1 == "Kilometers" and type2 == "Meters"):
        convertedValue = value * 1000
    elif(type1 == "Kilometers" and type2 == "Centimeters"):
        convertedValue = value * 1000 * 100
    elif(type1 == "Kilometers" and type2 == "Miles"):
        convertedValue = value * .621
    elif(type1 == "Kilometers" and type2 == "Yards"):
        convertedValue = (value * .621) * 1760
    elif(type1 == "Kilometers" and type2 == "Feet"):
        convertedValue = (value * .621) * 5280
    elif(type1 == "Kilometers" and type2 == "Inches"):
        convertedValue = (value * .621) * 5280 * 12
    convertedValue.set(convertedValue)
window = Tk()
value = StringVar()
metric1 = StringVar()
metric2 = StringVar()
convertedValue = StringVar()
greeting = Label(text ="Unit Converter", font = ('Times', 30))
greeting.pack()
frame = Frame(master= window, width = 250, height= 250)
frame.pack()
expressionFrame1 = Entry(frame, textvariable=value, font= ('Arial', 25))
expressionFrame1.grid(row=0,columnspan=4)
expressionFrame2 = Entry(frame, textvariable=convertedValue, font= ('Arial', 25))
expressionFrame2.grid(row=1,columnspan=4)
metricChosen1 = Label(frame, textvariable=metric1, font= ('Arial', 25))
metricChosen1.grid(row=0,column = 4,columnspan=1)
metricChosen2 = Label(frame, textvariable=metric2, font= ('Arial', 25))
metricChosen2.grid(row=1,column = 4,columnspan=1)

options = [
    "Kilometers",
    "Meters",
    "Centimeters",
    "Miles",
    "Yards",
    "Feet",
    "Inches",
]
dropdown1 = OptionMenu(frame, metric1, *options)
dropdown1.grid(row = 0, column=5)
dropdown2 = OptionMenu(frame, metric2, *options)
dropdown2.grid(row = 1, column= 5)
buttonConv = Button(master=frame,
    text="Convert",
    width=15,
    height=5,
    bg="gray",
    fg="white",
    relief=RAISED,command=lambda: convert(value, metric1, metric2))
buttonConv.grid(row = 3, column= 2)

mainloop()