from _ast import Lambda
from tkinter import *
from tkinter import font as f


class Calculator:
    def __init__(self, master):
        self.master = master

        DisplayFont = f.Font(font=("Garamond", 40, "bold"))
        CurrentFont = f.Font(font=("Garamond", 25))
        NumbersFont = f.Font(font=("Garamond", 30, "bold"))

        MainFrame = Frame(master, bd=5, relief=RIDGE)
        MainFrame.pack(fill=BOTH)

        DisplayFrame = Frame(MainFrame, bd=3, relief=RIDGE)
        DisplayFrame.pack(side=TOP, fill=X)
        ButtonsFrame = Frame(MainFrame, bd=3, relief=RIDGE)
        ButtonsFrame.pack(side=TOP)
        NumbersFrame = Frame(ButtonsFrame, bd=3, relief=RIDGE)
        NumbersFrame.pack(side=LEFT)
        OperationsFrame = Frame(ButtonsFrame, bd=3, relief=RIDGE)
        OperationsFrame.pack(side=RIGHT)

        Lbl1 = Label(DisplayFrame, bg="ivory", bd=2, relief=RIDGE, padx=10, pady=10)
        Lbl1.pack(fill=X)

        Txt2 = Entry(Lbl1, bg="white", bd=2, relief=RIDGE, font=CurrentFont, justify=RIGHT)
        Txt2.pack(side=TOP, padx=5, pady=5, fill=BOTH)

        Txt1 = Entry(Lbl1, bg="white", bd=2, relief=RIDGE, font=DisplayFont, justify=RIGHT)
        Txt1.pack(side=TOP, padx=5, pady=5, fill=BOTH)

        a = BooleanVar()
        b = BooleanVar()
        c = StringVar()
        d = StringVar()

        def clear_e():
            Txt1.delete(0, END)

        BtnCE = Button(NumbersFrame, text="CE", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                       width=3, command=clear_e)
        BtnCE.grid(row=0, column=0)

        def clear():
            Txt1.delete(0, END)
            Txt2.delete(0, END)
            c.set("")
            d.set("")

        BtnC = Button(NumbersFrame, text="C ", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=clear)
        BtnC.grid(row=0, column=1)

        def erase():
            cl1 = Txt1.get()
            Txt1.delete(len(cl1)-1)

        BtnErase = Button(NumbersFrame, text="<¬", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                          width=3, command=erase)
        BtnErase.grid(row=0, column=2)

        def button_click(number):
            cl1 = Txt1.get()
            cl2 = Txt2.get()
            state = 0
            for numbers in range(len(cl1)):
                if number == "." and cl1[numbers] == ".":
                    state = 1
                    print("THERE'S ALREADY A DOT.")
            if cl1 == cl2[-len(cl1)-1:-1] and a.get() is False:
                Txt1.delete(0, END)
                Txt1.insert(INSERT, number)
                a.set(TRUE)
            elif a.get() is True and state != 1:
                Txt1.insert(INSERT, number)
            elif state != 1:
                a.set(TRUE)
                Txt1.delete(0, END)
                Txt1.insert(INSERT, number)

        Btn7 = Button(NumbersFrame, text="7", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("7"))
        Btn7.grid(row=1, column=0)

        Btn8 = Button(NumbersFrame, text="8", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("8"))
        Btn8.grid(row=1, column=1)

        Btn9 = Button(NumbersFrame, text="9", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("9"))
        Btn9.grid(row=1, column=2)

        Btn4 = Button(NumbersFrame, text="4", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("4"))
        Btn4.grid(row=2, column=0)

        Btn5 = Button(NumbersFrame, text="5", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("5"))
        Btn5.grid(row=2, column=1)

        Btn6 = Button(NumbersFrame, text="6", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("6"))
        Btn6.grid(row=2, column=2)

        Btn1 = Button(NumbersFrame, text="1", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("1"))
        Btn1.grid(row=3, column=0)

        Btn2 = Button(NumbersFrame, text="2", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("2"))
        Btn2.grid(row=3, column=1)

        Btn3 = Button(NumbersFrame, text="3", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("3"))
        Btn3.grid(row=3, column=2)

        def minus():
            cl1 = Txt1.get()
            Txt1.delete(0, END)
            Txt1.insert(INSERT, int(cl1) * -1)

        BtnMinus = Button(NumbersFrame, text="_", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                          width=3, command=minus)
        BtnMinus.grid(row=4, column=0)

        Btn0 = Button(NumbersFrame, text="0", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                      width=3, command=lambda: button_click("0"))
        Btn0.grid(row=4, column=1)

        BtnDot = Button(NumbersFrame, text=".", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                        width=3, command=lambda: button_click("."))
        BtnDot.grid(row=4, column=2)

        def div():
            if d.get() == "" or d.get() == "div":
                cl1 = Txt1.get()
                cl2 = Txt2.get()
                a.set(FALSE)
                Txt2.insert(INSERT, cl1)
                Txt2.insert(END, "/")
                d.set("div")
                if cl2 == "":
                    c.set(cl1)
                elif b.get() is True:
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, float(c.get()) / float(cl1))
                    c.set(Txt1.get())
                elif cl2 != "" and b.get() is False:
                    b.set(TRUE)
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, float(cl2[-len(cl2):-1]) / float(cl1))
                    c.set(Txt1.get())
            else:
                if d.get() == "add":
                    add()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "/")
                    d.set("div")
                elif d.get() == "sub":
                    sub()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "/")
                    d.set("div")
                elif d.get() == "mul":
                    mul()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "/")
                    d.set("div")

        BtnDiv = Button(OperationsFrame, text="/", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                        width=3, command=div)
        BtnDiv.grid(row=0, column=0)

        def mul():
            if d.get() == "" or d.get() == "mul":
                cl1 = Txt1.get()
                cl2 = Txt2.get()
                a.set(FALSE)
                Txt2.insert(INSERT, cl1)
                Txt2.insert(END, "*")
                d.set("mul")
                if cl2 == "":
                    c.set(cl1)
                elif b.get() is True:
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(c.get()) * int(cl1))
                    c.set(Txt1.get())
                elif cl2 != "" and b.get() is False:
                    b.set(TRUE)
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(cl2[-len(cl2):-1]) * int(cl1))
                    c.set(Txt1.get())
            else:
                if d.get() == "add":
                    add()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "*")
                    d.set("mul")
                elif d.get() == "sub":
                    sub()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "*")
                    d.set("mul")
                elif d.get() == "div":
                    div()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "*")
                    d.set("mul")

        BtnMul = Button(OperationsFrame, text="*", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                        width=3, command=mul)
        BtnMul.grid(row=1, column=0)

        def sub():
            if d.get() == "" or d.get() == "sub":
                cl1 = Txt1.get()
                cl2 = Txt2.get()
                a.set(FALSE)
                Txt2.insert(INSERT, cl1)
                Txt2.insert(END, "-")
                d.set("sub")
                if cl2 == "":
                    c.set(cl1)
                elif b.get() is True:
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(c.get()) - int(cl1))
                    c.set(Txt1.get())
                elif cl2 != "" and b.get() is False:
                    b.set(TRUE)
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(cl2[-len(cl2):-1]) - int(cl1))
                    c.set(Txt1.get())
            else:
                if d.get() == "add":
                    add()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "-")
                    d.set("sub")
                elif d.get() == "mul":
                    mul()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "-")
                    d.set("sub")
                elif d.get() == "div":
                    div()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "-")
                    d.set("sub")

        BtnSub = Button(OperationsFrame, text="-", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                        width=3, command=sub)
        BtnSub.grid(row=2, column=0)

        def add():
            global math
            if d.get() == "" or d.get() == "add":
                cl1 = Txt1.get()
                cl2 = Txt2.get()
                a.set(FALSE)
                Txt2.insert(INSERT, cl1)
                Txt2.insert(END, "+")
                d.set("add")
                if cl2 == "":
                    c.set(cl1)
                elif b.get() is True:
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(c.get()) + int(cl1))
                    c.set(Txt1.get())
                elif cl2 != "" and b.get() is False:
                    b.set(TRUE)
                    Txt1.delete(0, END)
                    Txt1.insert(INSERT, int(cl2[-len(cl2):-1]) + int(cl1))
                    c.set(Txt1.get())
            else:
                if d.get() == "sub":
                    sub()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "+")
                    d.set("add")
                elif d.get() == "mul":
                    mul()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "+")
                    d.set("add")
                elif d.get() == "div":
                    div()
                    a.set(FALSE)
                    cl2 = Txt2.get()
                    Txt2.delete(0, END)
                    Txt2.insert(INSERT, cl2[:-1])
                    Txt2.insert(END, "+")
                    d.set("add")

        BtnAdd = Button(OperationsFrame, text="+", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                        width=3, command=add)
        BtnAdd.grid(row=3, column=0)

        def equals():
            second_number = Txt1.get()
            Txt1.delete(0, END)

            if d.get() == "add":
                Txt1.insert(INSERT, int(c.get()) + int(second_number))
                Txt2.delete(0, END)
            if d.get() == "sub":
                Txt1.insert(INSERT, int(c.get()) - int(second_number))
                Txt2.delete(0, END)
            if d.get() == "mul":
                Txt1.insert(INSERT, int(c.get()) * int(second_number))
                Txt2.delete(0, END)
            if d.get() == "div":
                Txt1.insert(INSERT, float(c.get()) / float(second_number))
                Txt2.delete(0, END)

        BtnEquals = Button(OperationsFrame, text="=", bg="beige", bd=5, relief=GROOVE, font=NumbersFont,
                           width=3, command=equals)
        BtnEquals.grid(row=4, column=0)


root = Tk()
app = Calculator(root)
root.title("CALCULATOR by Felipe Díaz")
root.resizable(False, False)
root.geometry("380x586+500+70")
root.mainloop()
