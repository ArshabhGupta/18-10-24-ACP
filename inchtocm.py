from tkinter import *


root = Tk()
root.title("Length Converter")
root.geometry('400x300')

lb1 = Label(text = "Hey there!", fg = "red", bg = "aqua", height = 1, width = 300)

label1 = Label(text = "Enter Inches" , bg = "white")
a = Entry()

def display():
    a1 = int(a.get())
    global message
    message = "Welcome to the application! "
    text_box.insert(END, a1 * 2.54)
    text_box.insert(END, "cm")

text_box = Text(height = 3)
btn = Button(text = "Convert", command = display, height = 1, bg = "aqua", fg = "blue")

lb1.pack()
label1.pack()
a.pack()
btn.pack()
text_box.pack()
root.mainloop()