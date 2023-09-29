from tkinter import *

tk = Tk()

tk.geometry("355x400")
tk.title("Gem Rey Calculator")
tk.configure(bg='lightblue')

MyEntry = Entry(tk, font="Arial 20", width=22,justify=RIGHT)
# MyEntry.place(x=50,y=20)
MyEntry.grid(row=1, column=0, padx=10, pady=30, columnspan=4)

num1 = Button(tk, text='1', font='Arial 20', width=3, height=1, command=lambda:num_display('1'))
num1.grid(row=2,column=0, pady=5)

num2 = Button(tk, text='2', font='Arial 20', width=3, height=1, command=lambda:num_display('2'))
num2.grid(row=2,column=1)

num3 = Button(tk, text='3', font='Arial 20', width=3, height=1, command=lambda:num_display('3'))
num3.grid(row=2,column=2)

plus = Button(tk, text='+', font='Arial 20', width=3, height=1, command=lambda:operator_select('+'))
plus.grid(row=2,column=3)

num4 = Button(tk, text='4', font='Arial 20', width=3, height=1, command=lambda:num_display('4'))
num4.grid(row=3,column=0, pady=5)

num5 = Button(tk, text='5', font='Arial 20', width=3, height=1, command=lambda:num_display('5'))
num5.grid(row=3,column=1)

num6 = Button(tk, text='6', font='Arial 20', width=3, height=1, command=lambda:num_display('6'))
num6.grid(row=3,column=2)

minus = Button(tk, text='-', font='Arial 20', width=3, height=1, command=lambda:operator_select('-'))
minus.grid(row=3,column=3)

num7 = Button(tk, text='7', font='Arial 20', width=3, height=1, command=lambda:num_display('7'))
num7.grid(row=4,column=0, pady=5)

num8 = Button(tk, text='8', font='Arial 20', width=3, height=1, command=lambda:num_display('8'))
num8.grid(row=4,column=1)

num9 = Button(tk, text='9', font='Arial 20', width=3, height=1, command=lambda:num_display('9'))
num9.grid(row=4,column=2)

times = Button(tk, text='x', font='Arial 20', width=3, height=1, command=lambda:operator_select('*'))
times.grid(row=4,column=3)

dot = Button(tk, text='.', font='Arial 20', width=3, height=1, command=lambda:num_display('.'))
dot.grid(row=5,column=0, pady=5)

zero = Button(tk, text='0', font='Arial 20', width=3, height=1, command=lambda:num_display('0'))
zero.grid(row=5,column=1)

equal = Button(tk, text='=', font='Arial 20', width=3, height=1, command=lambda:calculate())
equal.grid(row=5,column=2)

divide = Button(tk, text='÷', font='Arial 20', width=3, height=1, command=lambda:operator_select('/'))
divide.grid(row=5,column=3)


def num_display(num):
    value = MyEntry.get()
    MyEntry.delete(0, END)
    new_value = value + num
    MyEntry.insert(0, new_value)

def operator_select(opr):
    global operator
    operator = opr
    global firstnum
    firstnum = int(MyEntry.get())
    MyEntry.delete(0, END)

def calculate():
    secondnum = int(MyEntry.get())
    MyEntry.delete(0, END)
    if operator == '+':
        answer = firstnum + secondnum
    elif operator == '-':
        answer = firstnum - secondnum
    elif operator == '*':
        answer = firstnum * secondnum
    elif operator == '/':
        answer = firstnum / secondnum
    MyEntry.insert(0, answer)

tk.mainloop()