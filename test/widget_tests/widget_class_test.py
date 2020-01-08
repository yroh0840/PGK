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
        self.image = tk.PhotoImage(file = self.curdir+'/../../material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW)

        # 一番下のボタンたち
        self.sticky = tk.W+tk.E+tk.N+tk.S
        self.bottom_frame = tk.Frame(self, bg='lightgreen')
        self.bottom_frame.place(x=0, y=0, width='560', height='100')
        for column, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen')],):
            self.button = tk.Button(self.bottom_frame, text=text, bg=color, width='15', height='5',
                                    command=lambda:[self.parent_frame_1.place(x=0, y=0), self.bottom_frame.destroy()])
            self.button.pack(padx=20, side='left')
        # トークエリア
        #ttk.Style().configure('TP.TFrame', background='white')
        self.parent_frame_1 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_1.place(x=0,y=0)
        #self.parent_frame_1.config(bg="systemTransparent")#あとで機能を調べる
        self.parent_frame_2 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_2.place(x=0,y=128)
        #self.parent_frame_2.config(bg="systemTransparent")#あとで機能を調べる
        self.parent_frame_3 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_3.place(x=0,y=256)
        #self.parent_frame_3.config(bg="systemTransparent")#あとで機能を調べる
        # 一時的にparent_frameを消す
        self.parent_frame_1.place_forget()
        self.parent_frame_2.place_forget()
        self.parent_frame_3.place_forget()

        self.svar1 = tk.StringVar() 
        self.svar1.set('おい！')
        self.svar2 = tk.StringVar()
        self.svar2.set('お前股間臭いで！')
        self.svar3 = tk.StringVar()
        self.svar3.set('そーだそーだ！')

        # トークエリア一段目
        self.image_girl1 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', image=self.image_girl1)
        self.label_image1.place(x=0, y=0) 
        self.label_comment1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', textvariable=self.svar1, font='100')
        self.label_comment1.place(x=64, y=0, height=68, )
        self.svar1 = tk.StringVar()
        self.svar1.set('active')
        self.frame_button1 = tk.Frame(self.parent_frame_1, width='280', height='64', bg='#fcf3e7')
        self.frame_button1.place(x=280, y=64)
        self.button_list1 = []
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button1 = tk.Button(self.frame_button1, text=text, bg=color, width=5, height=2, 
                                    command=lambda:[self.parent_frame_2.place(x=0,y=128), 
                                                    self.parent_frame_rotation_2(),
                                                    self.button_list1[0].config(state='disabled'),
                                                    self.button_list1[1].config(state='disabled'),
                                                    self.button_list1[2].config(state='disabled'),
                                                    self.button_list1[3].config(state='disabled'),
                                                    self.button_list2[0].config(state='active'),
                                                    self.button_list2[1].config(state='active'),
                                                    self.button_list2[2].config(state='active'),
                                                    self.button_list2[3].config(state='active')])
            self.button_list1.append(self.button1)
            self.button_list1[cn].grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
        # トークエリア二段目
        self.image_girl2 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', image=self.image_girl2)
        self.label_image2.place(x=0, y=0)
        self.label_comment2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', textvariable=self.svar2, font='100')
        self.label_comment2.place(x=64, y=0, height=68, )
        self.frame_button2 = tk.Frame(self.parent_frame_2, width='280', height='64', bg='#fcf3e7')
        self.frame_button2.place(x=280, y=64)
        self.button_list2 = []
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button2 = tk.Button(self.frame_button2, text=text, bg=color, width=5, height=2, 
                                     command=lambda:[self.parent_frame_3.place(x=0, y=256), self.parent_frame_rotation_3(),
                                                    self.button_list2[0].config(state='disabled'),
                                                    self.button_list2[1].config(state='disabled'),
                                                    self.button_list2[2].config(state='disabled'),
                                                    self.button_list2[3].config(state='disabled'),
                                                    self.button_list3[0].config(state='active'),
                                                    self.button_list3[1].config(state='active'),
                                                    self.button_list3[2].config(state='active'),
                                                    self.button_list3[3].config(state='active')])
            self.button_list2.append(self.button2)
            self.button_list2[cn].grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
            #self.button2.config(state='disabled')

        # トークエリア三段目
        self.image_girl3 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.image_girl4 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/洗濯おばさん.png')
        self.label_image3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', image=self.image_girl4)
        self.label_image3.place(x=0, y=0)
        self.label_comment3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', textvariable=self.svar3, font='100')
        self.label_comment3.place(x=64, y=0, height=68, )  
        self.frame_button3 = tk.Frame(self.parent_frame_3, width='280', height='64', bg='#fcf3e7')
        self.frame_button3.place(x=280, y=64)
        self.button_list3 = []
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button3 = tk.Button(self.frame_button3, text=text, bg=color, width=5, height=2, 
                                     command=lambda: [self.parent_frame_rotation_1(),
                                                      self.button_list3[0].config(state='disabled'),
                                                      self.button_list3[1].config(state='disabled'),
                                                      self.button_list3[2].config(state='disabled'),
                                                      self.button_list3[3].config(state='disabled'),
                                                      self.button_list1[0].config(state='active'),
                                                      self.button_list1[1].config(state='active'),
                                                      self.button_list1[2].config(state='active'),
                                                      self.button_list1[3].config(state='active')])
            self.button_list3.append(self.button3)
            self.button_list3[cn].grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
            #self.button3.config(state='disabled')
        
        self.bvar1 = tk.BooleanVar()
        self.bvar1.set(True)
        self.bvar2 = tk.BooleanVar()
        self.bvar3 = tk.BooleanVar()
    # トークを入れ替える関数
    def parent_frame_rotation_1(self):
        #self.butoon1.config(stat
        if self.bvar1.get() == True:
            self.parent_frame_3.place(x=0, y=128)
            self.parent_frame_1.place(x=0, y=256)
            self.parent_frame_2.place(x=0, y=0)
            self.bvar2.set(True)


    def parent_frame_rotation_2(self):
        if self.bvar2.get() == True:
            self.parent_frame_1.place(x=0, y=128)
            self.parent_frame_2.place(x=0, y=256)
            self.parent_frame_3.place(x=0, y=0)
            self.bvar3.set(True)

    def parent_frame_rotation_3(self):
        if self.bvar3.get() == True:
            self.parent_frame_2.place(x=0, y=128)
            self.parent_frame_3.place(x=0, y=256)
            self.parent_frame_1.place(x=0, y=0)

def run():
    root = tk.Tk()
    #root.wm_attributes("-topmost", True)
    #root.wm_attributes("-disabled", True)
    #root.wm_attributes("-transparent", True) #あとでどんな機能か調べる
    #root.wm_attributes('-transparentcolor', 'white')
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()