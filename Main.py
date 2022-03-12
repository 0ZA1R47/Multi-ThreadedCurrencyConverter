import tkinter as tk
from threading import *

# Options for Main Currency
OptionList1 = [
    "USD",

]
# Options for Converting Currency
OptionList2 = [
    "PKR",
    "Pound",
    "Both",
]


# Function to convert USD to PKR $ Pound
def ok1():
    fr = variable.get()
    to = variable1.get()

    amount = float(e1.get())

    if fr == "USD" and to == "PKR":

        tot = amount * 155

    else:

        tot = amount * 220

    nsalText.set(tot)


# Function to convert USD to PKR $ Pound Both simultaneously
# Result of both the converted amounts will be displayed
def ok2():
    fr = variable.get()
    to = variable1.get()

    amount = float(e1.get())

    if fr == "USD" and to == "Both":
        tot1 = amount * 155
        tot2 = amount * 220
        result = ["PKR=", str(tot1), "&", "Pound=", str(tot2)]

    nsalText.set(result)


# Performing two tasks via Multi-Threading
def threading():
    if variable1.get() == "Both":  # if user chooses 'both' then thread 1 will be executed
        t1 = Thread(target=ok2())  # thread t1 will call function ok2()
        t1.start()  # Currency will be converted into both PKR & Pound,
        t1.join()

    else:
        t2 = Thread(target=ok1())  # thread t2 will call function ok1()
        t2.start()
        t2.join()


# GUI interface Design using Tkinter
root = tk.Tk()
root.geometry('350x350')
root.title(" Multi threaded Currency Converter ")
root['background'] = 'sky blue'

variable = tk.StringVar(root)
variable.set(OptionList1[0])

opt = tk.OptionMenu(root, variable, *OptionList1)
opt.config(width=10, background='white', font=('Helvetica', 12))
opt.pack(side="top")

variable1 = tk.StringVar(root)
variable1.set(OptionList2[0])

opt = tk.OptionMenu(root, variable1, *OptionList2)
opt.config(width=10, background='white', font=('Times New Roman', 12))
opt.pack(side="top")

global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

tk.Label(root, text="From", background='sky blue', font=('Times New Roman', 14)).place(x=10, y=10)
tk.Label(root, text="To", background='sky blue', font=('Times New Roman', 14)).place(x=10, y=40)
tk.Label(root, text="Amount", background='sky blue', font=('Times New Roman', 14)).place(x=10, y=80)

tk.Label(root, text="Total", background='sky blue', font=('Times New Roman', 14)).place(x=10, y=150)
tk.Label(root, text="", bd='3px', font=('Helvetica', 13), fg='red', textvariable=nsalText).place(x=80, y=150)
tk.Button(root, text="Calculate", fg='white', activebackground='white', bg='blue', command=threading,
                                                              height=1, width=8).place(x=110, y=110)

tk.Label(root, text="Developed by Group 08 \n190774\n190798\n190826\n190828"
         , font=('Times New Roman', 12), background='wheat', fg='red', ).place(x=90, y=220)

e1 = tk.Entry(root)
e1.place(x=110, y=80)

root.mainloop()
