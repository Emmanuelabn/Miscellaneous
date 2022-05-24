from tkinter import *

window = Tk()
window.geometry("460x460")
window.title("Calculator")
window_label = Label(window, text="Calculator", bg='Orange', font=("Times", 30, 'bold'))
window_label.pack(side=TOP)
window.config(background='Orange')

txt = StringVar()
operator = ""


def click_button(num):
    global operator
    operator = operator + str(num)
    txt.set(operator)


def equal_button():
    global operator
    op = str(eval(operator))
    txt.set(op)
    operator = ''


def clear_button():
    txt.set("")


my_input = Entry(window, font=("Courier New", 12, 'bold'), textvar=txt, width=25, bd=5, bg='powder blue')
my_input.pack()

button_1 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(1), text="1", font=("Courier New", 16, "bold"))
button_1.place(x=100, y=100)

button_2 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(2), text="2", font=("Courier New", 16, "bold"))
button_2.place(x=165, y=100)

button_3 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(3), text="3", font=("Courier New", 16, "bold"))
button_3.place(x=230, y=100)

button_4 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(4), text="4", font=("Courier New", 16, "bold"))
button_4.place(x=100, y=170)

button_5 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(5), text="5", font=("Courier New", 16, "bold"))
button_5.place(x=165, y=170)

button_6 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(6), text="6", font=("Courier New", 16, "bold"))
button_6.place(x=230, y=170)

button_7 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(7), text="7", font=("Courier New", 16, "bold"))
button_7.place(x=100, y=240)

button_8 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(8), text="8", font=("Courier New", 16, "bold"))
button_8.place(x=165, y=240)

button_9 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(9), text="9", font=("Courier New", 16, "bold"))
button_9.place(x=230, y=240)

button_dot = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("."), text=".", font=("Courier New", 16, "bold"))
button_dot.place(x=165, y=310)

button_0 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(0), text="0", font=("Courier New", 16, "bold"))
button_0.place(x=100, y=310)

button_clear = Button(window, padx=4, pady=2, bd=4, bg='white', command=lambda: clear_button(), text="C", font=("Courier New", 16, "bold"))
button_clear.place(x=380, y=45)

button_add = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("+"), text="+", font=("Courier New", 16, "bold"))
button_add.place(x=300, y=100)

button_sub = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("-"), text="-", font=("Courier New", 16, "bold"))
button_sub.place(x=300, y=170)

button_mult = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("*"), text="*", font=("Courier New", 16, "bold"))
button_mult.place(x=300, y=240)

button_div = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("/"), text="/", font=("Courier New", 16, "bold"))
button_div.place(x=300, y=310)

button_equal = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: equal_button(), text="=", font=("Courier New", 16, "bold"))
button_equal.place(x=230, y=310)

window.mainloop()