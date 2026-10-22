from tkinter import *

window = Tk()
window.geometry("328x500")
window.config(background="pink")
window.title("Калькулятор")


window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

for row_index in range(8):
    window.rowconfigure(row_index, weight=1)

expression = ""

def button_prs(num):
    global expression
    expression += str(num)
    result.set(expression)

def press_equal():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total 
    except:
        result.set("Ошибка! Деление на ноль невозможно.")
        expression = ""    

def press_reset():
    global expression
    total = ""
    result.set(total)
    expression = total

def press_backspace():
    global expression
    expression = expression[:-1]
    result.set(expression)

result = StringVar()
input_field = Entry(textvariable=result, font=("Arial", 20))
input_field.grid(row=0, column=1, columnspan=3, pady=10, padx=10, sticky="nsew")
input_field.config(background="PapayaWhip")


# 1 ряд кнопок
button1 = Button(text="1", command=lambda: button_prs(1), background="PaleVioletRed3", font=("Arial", 15))
button1.grid(row=2, column=1, pady=4, padx=4, sticky="nsew")

button2 = Button(text="2", command=lambda: button_prs(2), background="PaleVioletRed3", font=("Arial", 15))
button2.grid(row=2, column=2, pady=4, padx=4, sticky="nsew")

button3 = Button(text="3", command=lambda: button_prs(3), background="PaleVioletRed3", font=("Arial", 15))
button3.grid(row=2, column=3, pady=4, padx=4, sticky="nsew")

# 2 ряд кнопок
button4 = Button(text="4", command=lambda: button_prs(4), background="PaleVioletRed3", font=("Arial", 15))
button4.grid(row=3, column=1, pady=4, padx=4, sticky="nsew")

button5 = Button(text="5", command=lambda: button_prs(5), background="PaleVioletRed3", font=("Arial", 15))
button5.grid(row=3, column=2, pady=4, padx=4, sticky="nsew")

button6 = Button(text="6", command=lambda: button_prs(6), background="PaleVioletRed3", font=("Arial", 15))
button6.grid(row=3, column=3, pady=4, padx=4, sticky="nsew")

# 3 ряд кнопок
button7 = Button(text="7", command=lambda: button_prs(7), background="PaleVioletRed3", font=("Arial", 15))
button7.grid(row=4, column=1, pady=4, padx=4, sticky="nsew")

button8 = Button(text="8", command=lambda: button_prs(8), background="PaleVioletRed3", font=("Arial", 15))
button8.grid(row=4, column=2, pady=4, padx=4, sticky="nsew")

button9 = Button(text="9", command=lambda: button_prs(9), background="PaleVioletRed3", font=("Arial", 15))
button9.grid(row=4, column=3, pady=4, padx=4, sticky="nsew")

# 4 ряд кнопок
plus = Button(text="+", command=lambda: button_prs("+"), background="PaleVioletRed3", font=("Arial", 15))
plus.grid(row=5, column=1, pady=4, padx=4, sticky="nsew")

button10 = Button(text="0", command=lambda: button_prs(0), background="PaleVioletRed3", font=("Arial", 15))
button10.grid(row=5, column=2, pady=4, padx=4, sticky="nsew")

minus = Button(text="-", command=lambda: button_prs("-"), background="PaleVioletRed3", font=("Arial", 15))
minus.grid(row=5, column=3, pady=4, padx=4, sticky="nsew")

# 5 ряд кнопок
multiply = Button(text="*", command=lambda: button_prs("*"), background="PaleVioletRed3", font=("Arial", 15))
multiply.grid(row=6, column=1, pady=4, padx=4, sticky="nsew")

dot = Button(text=".", command=lambda: button_prs("."), background="PaleVioletRed3", font=("Arial", 15))
dot.grid(row=6, column=2, pady=4, padx=4, sticky="nsew")

divide = Button(text="/", command=lambda: button_prs("/"), background="PaleVioletRed3", font=("Arial", 15))
divide.grid(row=6, column=3, pady=4, padx=4, sticky="nsew")

# 6 ряд кнопок
backspace = Button(text="<-", command=press_backspace, background="PaleVioletRed3", font=("Arial", 15))
backspace.grid(row=7, column=1, pady=4, padx=4, sticky="nsew")

equal = Button(text="=", command=press_equal, background="PaleVioletRed3", font=("Arial", 15))
equal.grid(row=7, column=2, pady=4, padx=4, sticky="nsew")

reset = Button(text="AC", command=press_reset, background="PaleVioletRed3", font=("Arial", 15))
reset.grid(row=7, column=3, pady=4, padx=4, sticky="nsew")

window.mainloop()
