# tk_calclator2.py

import tkinter as tk

class CalcApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X, padx='10', pady='10')
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.sticky = tk.W+tk.E+tk.N+tk.S
        
        # row 1
        self.b_AC = tk.Button(self.frame, text='AC' ,width=4, bg='red')
        self.b_AC.grid(row=0, column=0, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())

        self.b_AC = tk.Button(self.frame, text='C' ,width=4)
        self.b_AC.grid(row=0, column=1, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())

        self.b_AC = tk.Button(self.frame, text='%' ,width=4)
        self.b_AC.grid(row=0, column=2, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())

        self.b_AC = tk.Button(self.frame, text='/' ,width=4)
        self.b_AC.grid(row=0, column=3, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())
        # row 2
        self.b_AC = tk.Button(self.frame, text='7' ,width=4)
        self.b_AC.grid(row=1, column=0, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 7))

        self.b_AC = tk.Button(self.frame, text='8' ,width=4)
        self.b_AC.grid(row=1, column=1, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 8))

        self.b_AC = tk.Button(self.frame, text='9' ,width=4)
        self.b_AC.grid(row=1, column=2, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 9))

        self.b_AC = tk.Button(self.frame, text='*' ,width=4)
        self.b_AC.grid(row=1, column=3, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())
        # row 3
        self.b_AC = tk.Button(self.frame, text='4' ,width=4)
        self.b_AC.grid(row=2, column=0, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 4))

        self.b_AC = tk.Button(self.frame, text='5' ,width=4)
        self.b_AC.grid(row=2, column=1, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 5))

        self.b_AC = tk.Button(self.frame, text='6' ,width=4)
        self.b_AC.grid(row=2, column=2, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 6))

        self.b_AC = tk.Button(self.frame, text='-' ,width=4)
        self.b_AC.grid(row=2, column=3, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())
        # row 4
        self.b_AC = tk.Button(self.frame, text='1' ,width=4)
        self.b_AC.grid(row=3, column=0, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 1))

        self.b_AC = tk.Button(self.frame, text='2' ,width=4)
        self.b_AC.grid(row=3, column=1, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 2))

        self.b_AC = tk.Button(self.frame, text='3' ,width=4)
        self.b_AC.grid(row=3, column=2, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 3))

        self.b_AC = tk.Button(self.frame, text='*' ,width=4)
        self.b_AC.grid(row=3, column=3, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())
        #row5
        self.b_AC = tk.Button(self.frame, text='0' ,width=4)
        self.b_AC.grid(row=4, column=0, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 0))

        self.b_AC = tk.Button(self.frame, text='.' ,width=4)
        self.b_AC.grid(row=4, column=2, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.insert(0, 0))

        self.b_AC = tk.Button(self.frame, text='=' ,width=4)
        self.b_AC.grid(row=4, column=3, sticky=self.sticky, padx='5',pady='3')
        self.b_AC.config(command=lambda:self.entry.clear())

        for i in range(4): self.frame.columnconfigure(i, weight=5)
        for i in range(5): self.frame.rowconfigure(i, weight=5)

        self.entry.get()

'''def reverse_string(event):
    input_value = var_entry.get()
    var_entry.set(input_value[::-1])'''


def main():
    root = tk.Tk()
    root.title('calclator')
    root.geometry('200x200+0+0')
    ca = CalcApp(root)
    root.mainloop()


if '__main__'==__name__:
    main()


    
#entry.bind('<Return>', reverse_string)
#var_entry = tk.StringVar()









'''
tk.Button(frame, text='AC',width=4, bg='red').grid(row=0, column=0, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='C', width=4).grid(row=0, column=1, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='%', width=4).grid(row=0, column=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='/', width=4).grid(row=0, column=3, sticky=sticky, padx='5',pady='3')

tk.Button(frame, text='7', width=4).grid(row=1, column=0, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='8', width=4).grid(row=1, column=1, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='9', width=4).grid(row=1, column=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='*', width=4).grid(row=1, column=3, sticky=sticky, padx='5',pady='3')

tk.Button(frame, text='4', width=4).grid(row=2, column=0, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='5', width=4).grid(row=2, column=1, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='6', width=4).grid(row=2, column=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='-', width=4).grid(row=2, column=3, sticky=sticky, padx='5',pady='3')

b_1 = tk.Button(frame, text='1', width=4)
b_1.grid(row=3, column=0, sticky=sticky, padx='5',pady='3')
b_1.config(command=lambda:entry.insert(0, 1))


tk.Button(frame, text='2', width=4).grid(row=3, column=1, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='3', width=4).grid(row=3, column=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='+', width=4).grid(row=3, column=3, sticky=sticky, padx='5',pady='3')

tk.Button(frame, text='0', width=10).grid(row=4, column=0, columnspan=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='.', width=4).grid(row=4, column=2, sticky=sticky, padx='5',pady='3')
tk.Button(frame, text='=', width=4).grid(row=4, column=3, sticky=sticky, padx='5',pady='3')
'''
