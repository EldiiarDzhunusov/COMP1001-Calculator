from tkinter import *
import trigonometrypage
import polynomialpage
import mathlab

def page():

    # ploting the graphing
    graphing = Tk()
    graphing.title("Graphing")
    graphing.geometry("1400x1000")
    graphing.configure(background="khaki1")
    heading = Label(graphing, text="Choose a type of a Graph",
                    font=("Helvetica", 20, "bold"), fg="black",
                    width="83",
                    height="3",background="khaki1")
    heading.place(x=0, y=0)

    def exit():
        graphing.destroy()

    def trig1():
        graphing.destroy()
        trigonometrypage.page()

    def lin1():
        graphing.destroy()
        polynomialpage.page()

    def home():
        graphing.destroy()
        mathlab.page()
        

    # Buttons of the main menu
    button1 = Button(graphing, text="Trigonometry",
                         width="30",
                         height="5", command=trig1)
    button1.place(x=600, y=100)

    button2 = Button(graphing, text="Polynomial",
                     width="30",
                     height="5", command=lin1)
    button2.place(x=600, y=200)

    button3 = Button(graphing, text="Exit",
                     width="10",
                     height="1", command=exit)
    button3.place(x=670, y=500)
    Button(graphing, text="Home", command=home).place(x=690, y=460)

    # running the graphing
    graphing.mainloop()

