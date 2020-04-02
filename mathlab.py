from tkinter import *
import mainmenu
import area
import volume
import derivative
import basiccalc

def page():

    # ploting the graphing
    graphing = Tk()
    graphing.title("Math Lab")
    graphing.geometry("1400x1000")
    graphing.configure(background = "MistyRose2")
    heading = Label(graphing, text="Welcome to the Math Lab",
                    font=("Helvetica", 20, "bold"), fg="blue",
                    width="83",
                    height="3",background = "MistyRose2")
    heading.place(x=0, y=0)

    def exit():
        graphing.destroy()

    def are1():
        graphing.destroy()
        area.page()

    def vol1():
        graphing.destroy()
        volume.page()

    def der1():
        graphing.destroy()
        derivative.page()

    def gra1():
        graphing.destroy()
        mainmenu.page()

    def cal1():
        graphing.destroy()
        basiccalc.page()

    # Buttons of the main menu
    button1 = Button(graphing, text="Area",
                         width="30",
                         height="5", command=are1)
    button1.place(x=600, y=100)

    button2 = Button(graphing, text="Volume",
                     width="30",
                     height="5", command=vol1)
    button2.place(x=600, y=200)

    button3 = Button(graphing, text="Derivative",
                     width="30",
                     height="5", command=der1)
    button3.place(x=600, y=300)

    button4 = Button(graphing, text="Graphing",
                     width="30",
                     height="5", command=gra1)
    button4.place(x=600, y=400)
    
    button5 = Button(graphing, text="Calculator",
                     width="30",
                     height="5", command=cal1)
    button5.place(x=600, y=500)

    button6 = Button(graphing, text="Exit",
                     width="10",
                     height="1", command=exit)
    button6.place(x=675, y=600)

    # running the graphing
    graphing.mainloop()



