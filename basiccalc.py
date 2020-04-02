from tkinter import *
import mathlab
def page():
    calc1 = Tk()
    calc1.geometry("1400x1000")
    calc1.configure(background= "skyblue")

    def evaluate1():
        res.configure(text="Answer: " + str(eval(entry.get())),background= "skyblue")

    def evaluate(event):
        res.configure(text="Answer: " + str(eval(entry.get())),background= "skyblue")

    def home():
        calc1.destroy()
        mathlab.page()
        
    but1 = Button(calc1, text="Enter", width=10, height=2)
    but1.place(x=650, y=100)
    but1.config(command=evaluate1)
    Button(calc1, text="Home" , command = home,width=10, height=2).place(x=650, y= 175)
    

    Label(calc1, text="Your Expression:",background= "skyblue").pack()
    entry = Entry(calc1)
    entry.bind("<Return>", evaluate)
    entry.pack()
    res = Label(calc1)
    res.pack()
    calc1.mainloop()

    
