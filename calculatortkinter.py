import tkinter as tk

mainWindow=tk.Tk()
mainWindow.title("Calculator")

heading_lable=tk.Label(mainWindow,text="Welcome To The Calculator")
heading_lable.pack()

heading_lable=tk.Label(mainWindow,text="Enter First variable=")
heading_lable.pack()

var1=tk.Entry(mainWindow)
var1.pack()

heading_lable=tk.Label(mainWindow,text="Enter Second variable=")
heading_lable.pack()

var2=tk.Entry(mainWindow)
var2.pack()

def addition():
    try:
        first=float(var1.get())
        second=float(var2.get())
        result=first+second
        print(result)
    except ValueError:
        print("Please enter Integer or Float values only.")


def substraction():
    try:
        first=float(var1.get())
        second=float(var2.get())
        result=first-second
        print(result)
    except ValueError:
        print("Please enter Integer or Float values only.")

def multiplication():
    try:
        first=float(var1.get())
        second=float(var2.get())
        result=first*second
        print(result)
    except ValueError:
        print("Please enter Integer or Float values only.")

def division():
    try:
        first=float(var1.get())
        second=float(var2.get())
        if(second!=0):
            result=first/second
            print(result)
        else:
            print("value of the second variable can't be zero.")

    except ValueError:
        print("Please enter Integer or Float values only.")

def modulus():
    try:
        first = float(var1.get())
        second = float(var2.get())
        if (second != 0):
            result = first % second
            print(result)
        else:
            print("value of the second variable can't be zero.")

    except ValueError:
        print("Please enter Integer or Float values only.")

label1=tk.Label(mainWindow,text="ADDITION:").pack(pady=(0,10))
button1=tk.Button(mainWindow,text="+",command=lambda: addition())
button1.pack(pady=(0,10))
label2=tk.Label(mainWindow,text="SUBSTRACTION:").pack(pady=(0,10))
button2=tk.Button(mainWindow,text="-",command=lambda: substraction())
button2.pack(pady=(0,10))
label3=tk.Label(mainWindow,text="MULTIPLICATION:").pack(pady=(0,10))
button3=tk.Button(mainWindow,text="*",command=lambda: multiplication())
button3.pack(pady=(0,10))
label4=tk.Label(mainWindow,text="DIVISION:").pack(pady=(0,10))
button4=tk.Button(mainWindow,text="/",command=lambda: division())
button4.pack(pady=(0,10))
label5=tk.Label(mainWindow,text="MODULOUS:").pack(pady=(0,10))
button5=tk.Button(mainWindow,text="%",command=lambda: modulus())
button5.pack()

mainWindow.mainloop()
