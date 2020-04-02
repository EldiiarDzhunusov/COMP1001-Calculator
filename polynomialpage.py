
from tkinter import *
import linearpage
import quadraticpage
import cubicpage
import mainmenu


def page():

    poly1 = Tk()
    poly1.title("Polynomial Functions")
    poly1.geometry("1400x1000")
    poly1.configure(background = "pale green")

    def exitpage():
        poly1.destroy()

    def home():
        poly1.destroy()
        mainmenu.page()

    def lin1():
        poly1.destroy()
        linearpage.page()

    def qua1():
        poly1.destroy()
        quadraticpage.page()

    def cub1():
        poly1.destroy()
        cubicpage.page()

    heading = Label(poly1, text="Choose a type of Polynomial function",
                                font=("Helvetica", 20, "bold"), fg="black",background = "pale green",
                                width="83",
                                height="3")
    heading.grid(column=0, row=0)

    button1 = Button(poly1, text="Linear Function",
                     width="30",
                     height="5", command=lin1)
    button1.place(x=600, y=100)

    button2 = Button(poly1, text="Quadratic Function",
                     width="30",
                     height="5", command=qua1)
    button2.place(x=600, y=200)

    button3 = Button(poly1, text="Cubic",
                     width="30",
                     height="5", command=cub1)
    button3.place(x=600, y=300)

    Button(poly1, text="Home", command=home).place(x=685, y=425)
    Button(poly1, text="Exit", command=exitpage).place(x=690, y=465)

    poly1.mainloop()
