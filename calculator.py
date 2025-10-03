from tkinter import *

#calculations--------------------------------------------------------------------------
exp = ""
exp_shown = ""

def button_press_number(key):
    global exp
    global exp_shown
    exp_shown += str(key)
    exp += str(key)
    display.set(exp_shown)

def button_press_func(key, val):
    global exp
    global exp_shown
    exp += str(val)
    exp_shown += str(key)
    display.set(exp_shown)


def equal():
    global exp
    global exp_shown
    try:
        evaluation = eval(exp)
        display.set(str(evaluation))
        exp = ""
        exp_shown = ""
    except:
        display.set("Error")
        exp = ""
        exp_shown = ""

def clear():
    global exp
    global exp_shown
    exp_shown = ""
    exp = ""
    display.set(exp_shown)

#gui----------------------------------------------------------------------------------

if __name__ == "__main__":
    calculator = Tk()
    calculator.title("Calculator")
    # calculator.geometry("400x240")
    calculator.configure(bg="black")

    display = StringVar()
    entry = Entry(calculator, textvariable=display, font=("Arial", 20))
    entry.grid(columnspan=5, sticky="EW")
    entry.config(bg="black", fg="white")
    #buttons number-----------------------------------
    b1 = Button(calculator, text="1", command=lambda:button_press_number(1) , fg="black", bg="white", height=2, width=13)
    b1.grid(row=1, column=0)

    b2 = Button(calculator, text="2", command=lambda:button_press_number(2) , fg="black", bg="white", height=2, width=13)
    b2.grid(row=2, column=0)

    b3 = Button(calculator, text="3", command=lambda:button_press_number(3) , fg="black", bg="white", height=2, width=13)
    b3.grid(row=3, column=0)

    b4 = Button(calculator, text="4", command=lambda:button_press_number(4) , fg="black", bg="white", height=2, width=13)
    b4.grid(row=4, column=0)

    b5 = Button(calculator, text="5", command=lambda:button_press_number(5) , fg="black", bg="white", height=2, width=13)
    b5.grid(row=5, column=0)

    b6 = Button(calculator, text="6", command=lambda:button_press_number(6) , fg="black", bg="white", height=2, width=13)
    b6.grid(row=1, column=1)

    b7 = Button(calculator, text="7", command=lambda:button_press_number(7) , fg="black", bg="white", height=2, width=13)
    b7.grid(row=2, column=1)

    b8 = Button(calculator, text="8", command=lambda:button_press_number(8) , fg="black", bg="white", height=2, width=13)
    b8.grid(row=3, column=1)

    b9 = Button(calculator, text="9", command=lambda:button_press_number(9) , fg="black", bg="white", height=2, width=13)
    b9.grid(row=4, column=1)

    b0 = Button(calculator, text="0", command=lambda:button_press_number(0) , fg="black", bg="white", height=2, width=13)
    b0.grid(row=5, column=1)

    #buttons functions-------------------------------

    bequal = Button(calculator, text="=", command=lambda:equal() , fg="black", bg="white", height=2, width=13)
    bequal.grid(row=1, column=2)

    badd = Button(calculator, text="+", command=lambda:button_press_func('+', '+') , fg="black", bg="white", height=2, width=13)
    badd.grid(row=2, column=2)

    bsubtract = Button(calculator, text="-", command=lambda:button_press_func('-', '-') , fg="black", bg="white", height=2, width=13)
    bsubtract.grid(row=3, column=2)

    bmultipy = Button(calculator, text="×", command=lambda:button_press_func('×' , '*') , fg="black", bg="white", height=2, width=13)
    bmultipy.grid(row=4, column=2)

    bdivide = Button(calculator, text="÷", command=lambda:button_press_func('÷', '/') , fg="black", bg="white", height=2, width=13)
    bdivide.grid(row=5, column=2)

    bclear = Button(calculator, text="clear", command=lambda: clear(), fg="black", bg="white", height=2, width=13)
    bclear.grid(row=1, column=3)

    bsquare = Button(calculator, text="x\u00b2", command=lambda: button_press_func('\u00b2', '**2'), fg="black", bg="white",
                     height=2, width=13)
    bsquare.grid(row=2, column=3)

    bsquareroot = Button(calculator, text="√x", command=lambda: button_press_func('^1/2', '**(1/2)'), fg="black", bg="white",
                     height=2, width=13)
    bsquareroot.grid(row=3, column=3)

    bpower = Button(calculator, text="x\u02B8", command=lambda: button_press_func('^', '**'), fg="black",
                     bg="white",
                     height=2, width=13)
    bpower.grid(row=4, column=3)

    bcube = Button(calculator, text="x\u00B3", command=lambda: button_press_func('x\u00B3', '**3'), fg="black",
                     bg="white",
                     height=2, width=13)
    bcube.grid(row=2, column=4)

    bremainder = Button(calculator, text="rem", command=lambda: button_press_func('/', '%'), fg="black",
                     bg="white",
                     height=2, width=13)
    bremainder.grid(row=1, column=4)

    bcuberoot = Button(calculator, text="\u00B3√x", command=lambda: button_press_func('^(1/3)', '**(1/3)'), fg="black",
                     bg="white",
                     height=2, width=13)
    bcuberoot.grid(row=3, column=4)

    #button paranthesis and point--------------------------------------------------------------

    bleft = Button(calculator, text="(", command=lambda: button_press_number("("), fg="black", bg="white", height=2,
                width=13)
    bleft.grid(row=5, column=3)

    bright = Button(calculator, text=")", command=lambda: button_press_number(")"), fg="black", bg="white", height=2,
                width=13)
    bright.grid(row=5, column=4)

    bpoint = Button(calculator, text=".", command=lambda: button_press_func('.', '.'), fg="black",
                     bg="white",
                     height=2, width=13)
    bpoint.grid(row=4, column=4)

    calculator.mainloop()