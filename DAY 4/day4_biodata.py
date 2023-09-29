from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry('500x670')
root.title('Biodata')
root.configure(bg='lightblue')

namelbl = Label(root, text="NAME:", font="Arial 12", bg='lightblue')
namelbl.grid(row=0, column=0, padx=3, pady=5)

name = Entry(root, width=35, font='Arial 12')
name.grid(row=0, column=1, padx=3, pady=1)


agelbl = Label(root, text="AGE:", font="Arial 12", bg='lightblue')
agelbl.grid(row=1, column=0, padx=3, pady=1)

agelist = list(range(12,99))

age_selector = IntVar()
agecombo = ttk.Combobox(root, values=agelist, textvariable=age_selector, width=50)
agecombo.grid(row=1, column=1, padx=3, pady=1) 

genderlbl = Label(root, text="GENDER:", font="Arial 12", bg='lightblue')
genderlbl.grid(row=2, column=0, padx=8, pady=1)

genderSelect = StringVar(root)

gender1 = Radiobutton(root, text="Male", variable=genderSelect, value="Male")
gender1.place(x=200, y=65)

gender2 = Radiobutton(root, text="Female", variable=genderSelect, value="Female")
gender2.place(x=300, y=65)


addresslbl = Label(root, text="ADDRESS:", font="Arial 12", bg='lightblue')
addresslbl.grid(row=3, column=0, padx=3, pady=5)

address = Entry(root, width=35, font='Arial 12')
address.grid(row=3, column=1, padx=3, pady=1)

skillslbl = Label(root, text="SKILLS:", font="Arial 12", bg='lightblue')
skillslbl.grid(row=4, column=0, padx=3, pady=5)

skills = Entry(root, width=35, font='Arial 12')
skills.grid(row=4, column=1, padx=3, pady=1)

phonelbl = Label(root, text="PHONE:", font="Arial 12", bg='lightblue')
phonelbl.grid(row=5, column=0, padx=3, pady=5)

phone = Entry(root, width=35, font='Arial 12')
phone.grid(row=5, column=1, padx=3, pady=1)

educationlbl = Label(root, text="EDUCATION:", font="Arial 12", bg="lightblue")
educationlbl.grid(row=6, column=0, padx=3, pady=5)

educationList = ['Elementary', 'Bachelor\'s Degree', 'Masteral', 'PhD']

education_selector = StringVar()
educationCombo = ttk.Combobox(root, width=50, values=educationList, textvariable=education_selector)
educationCombo.grid(row=6, column=1,  padx=3, pady=5)

hobbies = Label(root, text="HOBBIES:", font="Arial 12", bg='lightblue')
hobbies.grid(row=7, column=0, padx=3, pady=4)

hobby1_sel = IntVar()
hobby1 = Checkbutton(root, text="Programming", variable=hobby1_sel)
hobby1.grid(row=8, column=1, padx=3, pady=3)

hobby2_sel = IntVar()
hobby2 = Checkbutton(root, text="Reading Books", variable=hobby2_sel)
hobby2.grid(row=9, column=1, padx=3, pady=3)

hobby3_sel = IntVar()
hobby3= Checkbutton(root, text="Volleyball", variable=hobby3_sel)
hobby3.grid(row=10, column=1, padx=3, pady=3)


desclbl = Label(root, text="DESCRIPTION:", font="Arial 12", bg='lightblue')
desclbl.grid(row=11, column=0, padx=3, pady=1)

description = Text(root, width=45, height=3)
description.grid(row=11, column=1, padx=3, pady=1)

submit = Button(root, text="SUBMIT", font="Arial 12", width=7, height=1, command=lambda:compile_data())
submit.grid(row=12, column=0, columnspan=3, padx=4, pady=1)

def compile_data():
    nametxt = name.get()
    agetxt = age_selector.get()
    gendertxt = genderSelect.get()
    desctxt = description.get("1.0", "end-1c")
    hobbiestxt = ''
    if hobby1_sel.get() == 1:
        hobbiestxt += "Programming "
    if hobby2_sel.get() == 1:
        hobbiestxt += 'Reading Books '
    if hobby3_sel.get() == 1:
        hobbiestxt += 'Volleyball '
    msg = f'Hi, {nametxt}, {agetxt} years old - {gendertxt} - {desctxt}\n {hobbiestxt}'
    print(msg)
    messagebox.showinfo("Success", msg)

root.mainloop()