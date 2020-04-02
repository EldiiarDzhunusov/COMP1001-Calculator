from tkinter import *
import math
import mathlab


def page():
    class Area:
        def a_circle():
            try:
                pi = 3.14
                r = radius.get()
                area_circle = pi *float(r)* float(r)
                answer.insert(INSERT, "\nArea of the circle is pi *r *r = " )
                answer.insert(INSERT, pi)
                answer.insert(INSERT, "*")
                answer.insert(INSERT, r)
                answer.insert(INSERT, "*")
                answer.insert(INSERT, r)
                answer.insert(INSERT, "=")
                answer.insert(INSERT, area_circle)
            except:
                answer.insert(INSERT,"\nPlease enter a valid number")


        def circleMethod():

            global radius
            valueframe1 = Frame(ar)
            value = Label(valueframe1, text = "Enter value of radius:")
            value.grid(row = 0, column = 0)
            radius = Entry(valueframe1)
            radius.grid(row = 0, column =1, ipadx = 5)
            valueframe1.pack(side =TOP, pady = 5, ipadx=5)
            result = Button(valueframe1, text = "Get answer", bg = "red", command = Area.a_circle)
            result.grid(row = 0, column = 2, padx = 5)
            circle.config(state = DISABLED)


        def a_square():
            try:
                s = side.get()
                area_square = float(s) * float(s)
                answer.insert(INSERT, "\nArea of the square is s * s = ")
                answer.insert(INSERT, s)
                answer.insert(INSERT, "*")
                answer.insert(INSERT, s)
                answer.insert(INSERT, "=")
                answer.insert(INSERT, area_square)
            except:
                answer.insert(INSERT,"\nPlease enter a valid number")

        def squareMethod():
            global side
            valueframe = Frame(ar)
            value = Label(valueframe, text = "Enter value of side:")
            value.grid(row = 0, column = 0)
            side = Entry(valueframe)
            side.grid(row = 0, column =1, ipadx = 5)
            valueframe.pack(side =TOP, pady = 5, ipadx=5)
            result = Button(valueframe, text = "Get answer", bg = "red", command = Area.a_square)
            result.grid(row = 0, column = 2, padx = 5)
            square.config(state = DISABLED)
        def a_rectangular():
            try:
                a = length.get()
                b = width.get()
                area_rectangular = float(a) * float(b)
                answer.insert(INSERT, "\nArea of the rectangular is a * b = ")
                answer.insert(INSERT, a)
                answer.insert(INSERT, "*")
                answer.insert(INSERT, b)
                answer.insert(INSERT, "=")
                answer.insert(INSERT, area_rectangular)
            except:
                answer.insert(INSERT,"\nPlease enter a valid number")

        def rectangularMethod():
            global length
            global   width
            valueframe = Frame(ar)
            value = Label(valueframe, text="Enter the length of side:")
            value.grid(row=0, column=0)
            length = Entry(valueframe)
            length.grid(row=0, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the width of side:")
            value.grid(row=1, column=0)
            width = Entry(valueframe)
            width.grid(row=1, column=1, ipadx=5)
            result = Button(valueframe, text="Get answer", bg="red", command=Area.a_rectangular)
            result.grid(row=0, column=2, padx=5)
            valueframe.pack(side=TOP, pady=5, ipadx=5)
            rectangular.config(state=DISABLED)



        def a_triangle():
            try:
                a= float(side1.get())
                b = float(side2.get())
                c = float(side3.get())
                p = (a+b+c)/2
                area_triangle  = math.sqrt(p*(p-a)*(p-b)*(p-c))
                answer.insert(INSERT,"\nThe area of the triangle is sqrt(p*(p-a)*(p-b)*(p-c)) = ")
                answer.insert(INSERT,"sqrt(")
                answer.insert(INSERT, p)
                answer.insert(INSERT, "*(")
                answer.insert(INSERT, p)
                answer.insert(INSERT, "-")
                answer.insert(INSERT, a)
                answer.insert(INSERT, ")*(")
                answer.insert(INSERT, p)
                answer.insert(INSERT, "-")
                answer.insert(INSERT, b)
                answer.insert(INSERT, ")*(")
                answer.insert(INSERT, p)
                answer.insert(INSERT, "-")
                answer.insert(INSERT, c)
                answer.insert(INSERT, "))=")
                answer.insert(INSERT, area_triangle)
            except:
                answer.insert(INSERT,"\nPlease enter a valid number")

        def triangleMethod():
            global side1
            global side2
            global side3
            valueframe = Frame(ar)
            value = Label(valueframe, text="Enter the side1:")
            value.grid(row=0, column=0)
            side1 = Entry(valueframe)
            side1.grid(row=0, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the side2:")
            value.grid(row=1, column=0)
            side2 = Entry(valueframe)
            side2.grid(row=1, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the side3:")
            value.grid(row=3, column=0)
            side3 = Entry(valueframe)
            side3.grid(row=3, column=1, ipadx=5)
            result = Button(valueframe, text="Get answer", bg="red", command=Area.a_triangle)
            result.grid(row=0, column=2, padx=5)
            valueframe.pack(side=TOP, pady=5, ipadx=5)
            triangle.config(state=DISABLED)

    def refresh():
        ar.destroy()
        page()



    ar = Tk()
    ar.title ("Area")
    ar.geometry("1400x1000")
    ar.configure(background = "LightGoldenrod1")
    frame1 = Frame (ar, background = "LightGoldenrod1")
    title = Label(frame1, text = "Calculate Area of Different Shapes", font =("arial",20, "bold"), fg = "green", background = "LightGoldenrod1")
    title.grid(row = 0, column = 0)
    choice = Label(frame1, text = "What shape do you have?",font =("arial",20), fg= "blue", background = "LightGoldenrod1")
    choice.grid(row = 1, column = 0)
    frame1.pack(side = TOP, pady =10, padx = 5, ipadx = 5)

    frame2 = Frame (ar)
    ref = Button(frame2, font=("arial", 15), text="Refresh", bg="red", command=refresh)
    ref.grid(row=0, column=5, padx=0)
    circle = Button(frame2, font =("arial", 15), text = "Circle", bg = "grey", command = Area.circleMethod)
    circle.grid(row = 0, column = 0)
    square = Button(frame2, font =("arial", 15), text = "Square", bg = "red", command=Area.squareMethod)
    square.grid(row = 0, column = 1)
    triangle = Button(frame2, font =("arial", 15), text = "Triangle", bg = "yellow", command = Area.triangleMethod)
    triangle.grid(row = 0, column = 2)
    rectangular = Button(frame2, font =("arial", 15), text = "Rectangular", bg = "skyblue", command = Area.rectangularMethod)
    rectangular.grid(row = 0, column = 3)
    frame2.pack(side = TOP)

    def home():
        ar.destroy()
        mathlab.page()


    frame3 = Frame(ar, bg = "lightblue")
    answer = Text(frame3, height = 10, wrap = WORD)
    answer.grid(padx = 5, ipadx = 5, pady = 5, ipady =5)
    home = Button(frame3, font =("arial", 15), text = "Home", bg = "yellow",command = home)
    home.grid(row = 0, column = 2)
    frame3.place(x = 350, y =300)
    ar.mainloop()
