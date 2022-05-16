from tkinter import *
import checker
from tkinter import messagebox
from codeconverter import CodeConverter

code = CodeConverter()

checker = checker.Checker()


def number_type_for_convert():
    type_of_number = ("{}".format(clicked.get()))
    type_of_number2 = ("{}".format(clicked2.get()))

    if type_of_number == "Select Number System" or type_of_number2 == "Select Number System":
        messagebox.showerror(title="Electronic Code Calculator", message="Please Select valid number types for "
                                                                         "conversion")

    else:
        check_number(type_of_number, type_of_number2)


def check_number(type_of_number, type_of_number2):
    number = entry1.get()
    if type_of_number == "Decimal":
        if not number.isnumeric():
            messagebox.showerror(title="Electronic Code Calculator", message="Please Select valid Decimal number")

        else:
            answer = code.from_decimal(type_of_number, type_of_number2, number)
            canvas1.itemconfig(text1, text=answer)

    elif type_of_number == "Octal":
        if not checker.is_octal(number):
            messagebox.showerror(title="Electronic Code Calculator", message="Please Select valid Octal number")

        else:
            answer = code.from_octal(type_of_number, type_of_number2, number)
            canvas1.itemconfig(text1, text=answer)

    elif (type_of_number == "Binary") or (type_of_number == "Excess 3") or (type_of_number == "Gray"):
        if not checker.is_binary(number):
            messagebox.showerror(title="Electronic Code Calculator",
                                 message=f"Please Select valid {type_of_number} code")

        else:
            if type_of_number == "Binary":
                answer = code.from_binary(type_of_number, type_of_number2, number)
                canvas1.itemconfig(text1, text=answer)

            elif type_of_number == "Excess 3":
                answer = code.from_excess(type_of_number, type_of_number2, number)
                canvas1.itemconfig(text1, text=answer)

            elif type_of_number == "Gray":
                answer = code.from_gray(type_of_number, type_of_number2, number)
                canvas1.itemconfig(text1, text=answer)

            elif type_of_number == "BCD":
                answer = code.from_bcd(type_of_number, type_of_number2, number)
                canvas1.itemconfig(text1, text=answer)

    elif type_of_number == "Hexadecimal":
        if not checker.is_hexadecimal(number):
            messagebox.showerror(title="Electronic Code Calculator", message=f"Please Select valid Hexadecimal code")

        else:
            answer = code.from_hexadecimal(type_of_number, type_of_number2, number)
            canvas1.itemconfig(text1, text=answer)

    elif type_of_number == "BCD":
        if not checker.is_bcd(number):
            messagebox.showerror(title="Electronic Code Calculator", message=f"Please Select valid BCD code")

        else:
            answer = code.from_bcd(type_of_number, type_of_number2, number)
            canvas1.itemconfig(text1, text=answer)


tk = Tk()
tk.title("Electronic Code Calculator")
tk.config(bg="#43C6DB")
tk.geometry('1500x700')
title = Label(text='Electronic Code Calculator', font=('Arial', 40, 'bold'), bg="#43C6DB")
title.place(x=400, y=50)

options = [
    "Decimal",
    "Binary",
    "Octal",
    "Hexadecimal",
    "Excess 3",
    "Gray",
    "BCD"
]

# datatype of menu text
clicked = StringVar()
clicked2 = StringVar()

# initial menu text
clicked.set("Select Number System")
clicked2.set("Select Number System")

# Create Dropdown menu
drop = OptionMenu(tk, clicked, *options)
drop.config(width=30, height=1, font=("Arial", 20, "bold"), bg="#B3B3B3")
drop.place(x=200, y=180)

drop2 = OptionMenu(tk, clicked2, *options)
drop2.config(width=30, height=1, font=("Arial", 20, "bold"), bg="#B3B3B3")
drop2.place(x=800, y=180)

entry1 = Entry(width=32, font=("Arial", 20, "bold"))
entry1.place(x=200, y=350)
entry1.focus()

canvas1 = Canvas(width=490, height=35)
text1 = canvas1.create_text(250, 20, text="Answer", font=("Arial", 20, "bold"))
canvas1.place(x=800, y=350)

canvas2 = Canvas(width=50, height=50, bg="#43C6DB", highlightthickness=0)

img = PhotoImage(file="arrow (1).png")

canvas2.create_image(27, 27, image=img)
canvas2.config(background="#43C6DB")
canvas2.place(x=715, y=342)

button = Button(text="Convert", font=("Arial", 20, "bold"), command=number_type_for_convert, activebackground="#B3B3B3",
                activeforeground="green")
button.place(x=683, y=500)

name = Label(text="Made by Achyut Jadhav", background="#43C6DB")
name.place(x=1300, y=650)

tk.mainloop()
