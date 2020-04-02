from tkinter import *
import sinpage
import cospage
import tanpage
import mainmenu


def page():

    trig1 = Tk()
    trig1.title("Trigonometry")
    trig1.geometry("1400x1000")
    trig1.configure(background = "MediumPurple1")

    def exitpage():
        trig1.destroy()

    def home():
        trig1.destroy()
        mainmenu.page()

    def sinpage1():
        trig1.destroy()
        sinpage.page()

    def cospage1():
        trig1.destroy()
        cospage.page()

    def tanpage1():
        trig1.destroy()
        tanpage.page()


    heading = Label(trig1, text="Choose a type of Trigonometric function",
                                font=("Helvetica", 20, "bold"), fg="black",
                                width="83",
                                height="3",background = "MediumPurple1")
    heading.grid(column=0, row=0)

    button1 = Button(trig1, text="Sine",
                     width="30",
                     height="5", command=sinpage1)
    button1.place(x=600, y=100)

    button2 = Button(trig1, text="Cosine",
                     width="30",
                     height="5", command=cospage1)
    button2.place(x=600, y=200)

    button3 = Button(trig1, text="Tangent",
                     width="30",
                     height="5", command=tanpage1)
    button3.place(x=600, y=300)

    Button(trig1, text="Home", command=home).place(x=685, y=500)
    Button(trig1, text="Exit", command=exitpage).place(x=693, y=460)


    trig1.mainloop()
