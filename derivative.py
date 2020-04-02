from tkinter import *
import mathlab


def page():
    class Derivative:
        def _polyn():
            a = length.get()
            l = list(a)
            print(l)
            s = ['-', '+', '^', ' ']
            c = []
            p = []
            f = ' '
            h = ' '
            for i in range(len(l)):
                if l[i] == 'x':
                    t = i
                    while ((l[t - 1] in s) == False) and (t != 0):
                        f = l[t - 1] + f
                        t = t - 1
                    if (t != 0):
                        f = l[t - 1] + f
                    c.append(float(f))
                    f = ' '
                if l[i] == '^':
                    k = i
                    while (k + 1) < len(l) and ((l[k + 1] in s) == False):
                        h = h + l[k + 1]
                        k = k + 1
                    p.append(float(h))
                    h = ''
            valueframe2 = Frame(der)
            value = Label(valueframe2, text="Enter the powers of expression:")
            value.grid(row=1, column=0)
            answer.insert(INSERT, "\nThe derivative of the expression ")
            answer.insert(INSERT, length.get())
            answer.insert(INSERT, " is\n")
            for i in range(len(c)):
                if (c[i]>0 and p[i]>0) or (c[i]<0 and p[i]<0):
                    answer.insert(INSERT, " + ")
                    answer.insert(INSERT,c[i]*p[i])
                    answer.insert(INSERT, " x ^ ")
                    answer.insert(INSERT, p[i] - 1)
                else:
                    answer.insert(INSERT, c[i] * p[i])
                    answer.insert(INSERT, " x ^ ")
                    answer.insert(INSERT, p[i] - 1)
            if len(c)== 0:
                answer.insert(INSERT, 0)





        def polyn():
            global length
            valueframe1 = Frame(der)
            value = Label(valueframe1, text="Enter the expression without the spaces between")
            value.grid(row=0, column=0)
            length = Entry(valueframe1)
            length.grid(row=0, column=1, ipadx=5)
            valueframe1.pack(side=TOP, pady=5, ipadx=5)
            result = Button(valueframe1, text="Get answer", bg="red", command = Derivative._polyn)
            result.grid(row=0, column=2, padx=5)
            polynomial.config(state=DISABLED)


    der = Tk()
    der.title("Derivative")
    der.geometry("1400x1000")
    der.configure(background="orchid3")
    frame1 = Frame (der,background="orchid3")
    title = Label(frame1, text = "Calculate the derivative of function", font =("arial",20, "bold"), fg = "black",background="orchid3")
    title.grid(row = 0, column = 0)
    choice = Label(frame1, text = "What is your function?",font =("arial",20), fg= "blue",background="orchid3")
    choice.grid(row = 1, column = 0)
    frame1.pack(side = TOP, pady =10, padx = 5, ipadx = 5)



    frame2 = Frame (der)
    polynomial = Button(frame2, font =("arial", 15), text = "Polynomial", bg = "azure2", command = Derivative.polyn)
    polynomial.grid(row = 0, column = 0)
    frame2.pack(side = TOP)

    def home():
        der.destroy()
        mathlab.page()

    frame3 = Frame(der, bg = "lightblue")
    answer = Text(frame3, height = 10, wrap = WORD)
    answer.grid(padx = 5, ipadx = 5, pady = 5, ipady =5)
    home = Button(frame3, font=("arial", 15), text="Home", bg="yellow", command=home)
    home.grid(row=0, column=2)
    frame3.place(x=350, y=300)
    der.mainloop()
