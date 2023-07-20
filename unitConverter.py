from tkinter import *
# Unit Conversion Math
def convert(value, type1, type2):
    global convertedValue
    valueFloat = float(value)
    if(type1 == "Kilometers" and type2 == "Meters"):
        convValue = valueFloat * 1000
    elif(type1 == "Kilometers" and type2 == "Centimeters"):
        convValue = valueFloat * 1000 * 100
    elif(type1 == "Kilometers" and type2 == "Miles"):
        convValue = valueFloat * .621
    elif(type1 == "Kilometers" and type2 == "Yards"):
        convValue = (valueFloat * .621) * 1760
    elif(type1 == "Kilometers" and type2 == "Feet"):
        convValue = (valueFloat * .621) * 5280
    elif(type1 == "Kilometers" and type2 == "Inches"):
        convValue = (valueFloat * .621) * 5280 * 12
    elif(type1 == "Meters" and type2 == "Kilometers"):
        convValue = valueFloat / 1000
    elif(type1 == "Meters" and type2 == "Centimeters"):
        convValue = valueFloat * 100
    elif(type1 == "Meters" and type2 == "Miles"):
        convValue = valueFloat * .000621
    elif(type1 == "Meters" and type2 == "Yards"):
        convValue = (valueFloat * 1.09361)
    elif(type1 == "Meters" and type2 == "Feet"):
        convValue = (valueFloat * 3.28084)
    elif(type1 == "Meters" and type2 == "Inches"):
        convValue = (valueFloat * 39.3701)
    elif(type1 == "Centimeters" and type2 == "Meters"):
        convValue = valueFloat / 100
    elif(type1 == "Centimeters" and type2 == "Kilometers"):
        convValue = (valueFloat / 100) / 1000
    elif(type1 == "Centimeters" and type2 == "Miles"):
        convValue = valueFloat * .000006213
    elif(type1 == "Centimeters" and type2 == "Yards"):
        convValue = (valueFloat * .01093)
    elif(type1 == "Centimeters" and type2 == "Feet"):
        convValue = (valueFloat * .0328)
    elif(type1 == "Centimeters" and type2 == "Inches"):
        convValue = (valueFloat * .3937)
    elif(type1 == "Miles" and type2 == "Meters"):
        convValue = valueFloat * 1609.34
    elif(type1 == "Miles" and type2 == "Centimeters"):
        convValue = valueFloat * 160934
    elif(type1 == "Miles" and type2 == "Kilometers"):
        convValue = valueFloat * 1.60634
    elif(type1 == "Miles" and type2 == "Yards"):
        convValue = (valueFloat * 1760)
    elif(type1 == "Miles" and type2 == "Feet"):
        convValue = (valueFloat * 1760) * 3
    elif(type1 == "Miles" and type2 == "Inches"):
        convValue = (valueFloat * 1760) * 3 * 12
    elif(type1 == "Yards" and type2 == "Meters"):
        convValue = valueFloat * .9144
    elif(type1 == "Yards" and type2 == "Centimeters"):
        convValue = valueFloat * 91.44
    elif(type1 == "Yards" and type2 == "Miles"):
        convValue = valueFloat / 1760
    elif(type1 == "Yards" and type2 == "Kilometers"):
        convValue = (valueFloat * .0009144)
    elif(type1 == "Yards" and type2 == "Feet"):
        convValue = (valueFloat * 3)
    elif(type1 == "Yards" and type2 == "Inches"):
        convValue = (valueFloat * 3) * 12
    elif(type1 == "Feet" and type2 == "Meters"):
        convValue = valueFloat * .3048
    elif(type1 == "Feet" and type2 == "Centimeters"):
        convValue = valueFloat * 30.48
    elif(type1 == "Feet" and type2 == "Miles"):
        convValue = valueFloat / 5280
    elif(type1 == "Feet" and type2 == "Yards"):
        convValue = (valueFloat / 3)
    elif(type1 == "Feet" and type2 == "Kilometers"):
        convValue = (valueFloat * .0003048)
    elif(type1 == "Feet" and type2 == "Inches"):
        convValue = (valueFloat * 12)
    elif(type1 == "Inches" and type2 == "Meters"):
        convValue = valueFloat / 39.37
    elif(type1 == "Inches" and type2 == "Centimeters"):
        convValue = valueFloat * 2.54
    elif(type1 == "Inches" and type2 == "Miles"):
        convValue = valueFloat / 63360
    elif(type1 == "Inches" and type2 == "Yards"):
        convValue = (valueFloat / 36)
    elif(type1 == "Inches" and type2 == "Feet"):
        convValue = (valueFloat / 12)
    elif(type1 == "Inches" and type2 == "Kilometers"):
        convValue = (valueFloat * .0000254)
# Temperature conversion
    elif(type1 == "Fahrenheit" and type2 == "Celsius"):
        convValue = (valueFloat - 32) * (5/9)
    elif(type1 == "Celsius" and type2 == "Fahrenheit"):
        convValue = (valueFloat * (9/5)) + 32
# Adding 3D converiond 
    elif(type1 == "Square Kilometers" and type2 == "Square Miles"):
        convValue = (valueFloat - 32) * (5/9)
    elif(type1 == "Celsius" and type2 == "Fahrenheit"):
        convValue = (valueFloat * (9/5)) + 32
    convertedValue.set(convValue)
# Create master frame
window = Tk()
# Create variables and set labels for metrics
value = StringVar()
metric1 = StringVar()
metric2 = StringVar()
metric1.set("Kilometers")
metric2.set("Meters")
convertedValue = StringVar()
# Create greeting title
greeting = Label(text ="Unit Converter", font = ('Times', 30))
greeting.pack()
# Create subframe into which all buttons and text boxes will be placed
frame = Frame(master= window, width = 250, height= 250)
frame.pack()
# Create and place text boxes
expressionFrame1 = Entry(frame, textvariable=value, font= ('Arial', 25))
expressionFrame1.grid(row=0,columnspan=4)
expressionFrame2 = Entry(frame, textvariable=convertedValue, font= ('Arial', 25))
expressionFrame2.grid(row=1,columnspan=4)
# Create labels for selected unit
metricChosen1 = Label(frame, textvariable=metric1, font= ('Arial', 25))
metricChosen1.grid(row=0,column = 4,columnspan=1)
metricChosen2 = Label(frame, textvariable=metric2, font= ('Arial', 25))
metricChosen2.grid(row=1,column = 4,columnspan=1)
# Create array of units for drop down menus
options = [
    "Kilometers",
    "Meters",
    "Centimeters",
    "Miles",
    "Yards",
    "Feet",
    "Inches",
    "Fahrenheit",
    "Celsius"
]
# Create drop down menu's 
dropdown1 = OptionMenu(frame, metric1, *options)
dropdown1.grid(row = 0, column=5)
dropdown2 = OptionMenu(frame, metric2, *options)
dropdown2.grid(row = 1, column= 5)
# Create clickable button to begin conversion
buttonConv = Button(master=frame,
    text="Convert",
    width=45,
    height=5,
    bg="gray",
    fg="white",
    relief=RAISED,command=lambda: convert(value.get(), metric1.get(), metric2.get()))
buttonConv.grid(row = 3, column= 1, columnspan= 4)

mainloop()