import tkinter as tk
import tkinter.ttk as ttk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得
        self.image = tk.PhotoImage(file = self.curdir+'/../material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW)

        # 一番下のボタンたち
        self.sticky = tk.W+tk.E+tk.N+tk.S
        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=0, y=860, width='560', height='100')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue'), ('E', 'Red')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width='5', height='3', command=lambda: [self.frame.place_forget(), self.add_widget()])
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='20', pady='17', ipadx='10')
  
        # talk_area
        self.image_girl = tk.PhotoImage(file = self.curdir+'/../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=20)
        self.label = tk.Label(self, text='飯いくぞ！')
        self.label.place(x=100, y=20, width='100', height='50')  
        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=80, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
        self.label_image.place_forget(), self.label.place_forget(), self.button.grid_forget(), self.button.grid_forget()

        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=120)
        self.label = tk.Label(self, text='何が食いたいんや？')
        self.label.place(x=100, y=120, width='100', height='50')
        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=160, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
 
        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=220)
        self.label = tk.Label(self, text='何が食いたいんや？')
        self.label.place(x=100, y=220, width='100', height='50')
        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=240, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')

        '''
    def add_widget(self):
        self.image_girl = tk.PhotoImage(file = self.curdir+'/../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=20)

        self.label = tk.Label(self, text='飯いくぞ！')
        self.label.place(x=100, y=20, width='100', height='50')     

        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=80, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4, command=self.add_widget2)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')

    def add_widget2(self):
        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=120)
        self.label = tk.Label(self, text='何が食いたいんや？')
        self.label.place(x=100, y=120, width='100', height='50')

        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=160, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4, command=self.add_widget3)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
 
    def add_widget3(self):
        self.label_image = tk.Label(self, width=50, height=50, image=self.image_girl)
        self.label_image.place(x=20, y=220)
        self.label = tk.Label(self, text='何が食いたいんや？')
        self.label.place(x=100, y=220, width='100', height='50')

        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=240, width='250', height='50')
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4, command=self.add_widget3)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')

    '''
def run():
    root = tk.Tk()
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()