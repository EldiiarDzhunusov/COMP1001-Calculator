from tkinter import*
import mathlab
def page():
    class Volume:
        def v_sphere():
            pi = 3.14
            r = float(radius.get())
            v = 4/3 * pi * r**3
            answer.insert(INSERT,"The volume of the sphere is V = 4/3 *pi*r^3\n")
            answer.insert(INSERT, "V = ")
            answer.insert(INSERT, "4/3*")
            answer.insert(INSERT, pi)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "=")
            answer.insert(INSERT, v)

        def sphere():
            global radius
            valueframe1 = Frame(vol)
            value = Label(valueframe1, text="Enter value of radius of the sphere:", font =("arial",14, "bold"))
            value.grid(row=0, column=0)
            radius = Entry(valueframe1)
            radius.grid(row=0, column=1, ipadx=5)
            valueframe1.pack(side=TOP, pady=5, ipadx=5)
            result = Button(valueframe1, text="Get answer", bg="red", command = Volume.v_sphere)
            result.grid(row=1, column=1, padx=5)
            sphere.config(state=DISABLED)
        def v_prism():
            l = float(length.get())
            w = float(width.get())
            h = float(height.get())

            v = l * w * h
            answer.insert(INSERT, "\nThe volume of the prism is V = length * width * height \n")
            answer.insert(INSERT, "V= ")
            answer.insert(INSERT, l)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, w)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, h)
            answer.insert(INSERT, "=")
            answer.insert(INSERT, v)

        def prism():
            global length
            global width
            global height
            valueframe = Frame(vol)
            value = Label(valueframe, text="Enter the length:",font =("arial",12, "bold"))
            value.grid(row=0, column=0)
            length = Entry(valueframe)
            length.grid(row=0, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the width:",font =("arial",12, "bold"))
            value.grid(row=1, column=0)
            width = Entry(valueframe)
            width.grid(row=1, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the height:",font =("arial",12, "bold"))
            value.grid(row=3, column=0)
            height = Entry(valueframe)
            height.grid(row=3, column=1, ipadx=5)
            result = Button(valueframe, text="Get answer", bg="red", command=Volume.v_prism)
            result.grid(row=1, column=2, padx=5)
            valueframe.pack(side=TOP, pady=5, ipadx=5)
            prism.config(state=DISABLED)

        def cone():
            global height
            global radius
            valueframe = Frame(vol)
            value = Label(valueframe, text="Enter the height :")
            value.grid(row=0, column=0)
            height = Entry(valueframe)
            height.grid(row=0, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the radius of side:")
            value.grid(row=1, column=0)
            radius = Entry(valueframe)
            radius.grid(row=1, column=1, ipadx=5)
            result = Button(valueframe, text="Get answer", bg="red", command = Volume.v_cone)
            result.grid(row=0, column=2, padx=5)
            valueframe.pack(side=TOP, pady=5, ipadx=5)
            cone.config(state=DISABLED)

        def v_cone():
            r = float(radius.get())
            h = float(height.get())
            pi = 3.14
            volume_cone = 1/3*pi *r**2*h
            answer.insert(INSERT, "\nVolume of the cone is 1/3 * pi * r*r *h = ")
            answer.insert(INSERT, "1/3")
            answer.insert(INSERT, "*")
            answer.insert(INSERT, "3.14")
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, h)
            answer.insert(INSERT, "=")
            answer.insert(INSERT, volume_cone)
        def cylinder():
            global height
            global radius
            valueframe = Frame(vol)
            value = Label(valueframe, text="Enter the height :")
            value.grid(row=0, column=0)
            height = Entry(valueframe)
            height.grid(row=0, column=1, ipadx=5)
            value = Label(valueframe, text="Enter the radius of side:")
            value.grid(row=1, column=0)
            radius = Entry(valueframe)
            radius.grid(row=1, column=1, ipadx=5)
            result = Button(valueframe, text="Get answer", bg="red", command=Volume.v_cylinder)
            result.grid(row=0, column=2, padx=5)
            valueframe.pack(side=TOP, pady=5, ipadx=5)
            cone.config(state=DISABLED)

        def v_cylinder():
            r = float(radius.get())
            h = float(height.get())
            pi = 3.14
            volume_cylinder =  pi * r ** 2 * h
            answer.insert(INSERT, "\nVolume of the cone is 1/3 * pi * r*r *h = ")
            answer.insert(INSERT, "3.14")
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, r)
            answer.insert(INSERT, "*")
            answer.insert(INSERT, h)
            answer.insert(INSERT, "=")
            answer.insert(INSERT, volume_cylinder)




    vol = Tk()
    vol.title ("Volume")
    vol.geometry("1400x1000")
    vol.configure(background="gold2")
    frame1 = Frame(vol, background="gold2")
    title = Label(frame1, text = "Calculate the Volume of Different Shapes", font =("helvetica",20, "bold"), fg = "green", background="gold2")
    title.grid(row = 0, column = 0)
    choice = Label(frame1, text = "What shape do you have?",font =("arial",20), fg= "blue",background="gold2")
    choice.grid(row = 1, column = 0)
    frame1.pack(side = TOP, pady =10, padx = 5, ipadx = 5)

    def refresh():
        vol.destroy()
        page()


    frame2 = Frame (vol)
    ref = Button(frame2, font=("arial", 15), text="Refresh", bg="red", command=refresh)
    ref.grid(row=0, column=5, padx=0)
    sphere = Button(frame2, font =("arial", 15), text = "Sphere", bg = "cyan", command = Volume.sphere)
    sphere.grid(row = 0, column = 0, padx = 0)
    prism = Button(frame2, font =("arial", 15), text = "Prism", bg = "tomato",command = Volume.prism)
    prism.grid(row = 0, column = 1, padx = 0)
    cone = Button(frame2, font =("arial", 15), text = "Cone", bg = "yellow", command = Volume.cone)
    cone.grid(row = 0, column = 2, padx =0)
    cylinder = Button(frame2, font =("arial", 15), text = "Cylinder", bg = "salmon", command = Volume.cylinder)
    cylinder.grid(row = 0, column = 4, padx =0)
    frame2.pack(side = TOP)

    def home():
        vol.destroy()
        mathlab.page()


    frame3 = Frame(vol, bg = "lightblue")
    answer = Text(frame3, height = 10, wrap = WORD)
    answer.grid(padx = 5, ipadx = 5, pady = 5, ipady =5)
    home = Button(frame3, font=("arial", 15), text="Home", bg="yellow", command=home)
    home.grid(row=0, column=2)
    frame3.place(x=350, y=300)
    vol.mainloop()
