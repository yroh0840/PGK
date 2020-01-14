import tkinter as tk
import os

class Widget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.counter = 0
        self.params_list = []

    # ウィジェットの配置
    def create_widgets(self):
        self.canvass() # 背景画像表示
        self.first_buttons() # 最初のボタン表示
        self.talk_area() # トークエリア
        self.talk_area_stage_1() # トークエリア一段目
        self.talk_area_stage_2() # トークエリア二段目
        self.talk_area_stage_3() # トークエリア三段目

   # 背景画像表示
    def canvass(self):
        self.curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得
        self.image = tk.PhotoImage(file = self.curdir+'/../../material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW)

    # 最初のボタン表示
    def first_buttons(self):
        self.sticky = tk.W+tk.E+tk.N+tk.S
        self.first_button_image_1 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/distance_icon.png')
        self.first_button_image_2 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/budget_icon.png')
        self.first_button_image_3 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/genre_icon.png')
        self.bottom_frame = tk.Frame(self, bg='#fcf3e7')
        self.bottom_frame.place(x=0, y=0, width='560', height='100')
        image_list = [self.first_button_image_1, self.first_button_image_2, self.first_button_image_3]
        button_list = []
        for image in image_list:
            self.button = tk.Button(self.bottom_frame, image=image, width='170', height='100',
                                    command=lambda:[self.parent_frame_1.place(x=0, y=0), 
                                                    self.bottom_frame.destroy()])
            self.button.pack(padx='2', side='left')
            button_list.append(self.button)
        button_list[0].bind('<Button-1>', self.button_distance)
        button_list[1].bind('<Button-1>', self.button_yen)
        button_list[2].bind('<Button-1>', self.button_genre)
        
    # トークエリアに入れるテキスト
    def talk_area(self):
        self.parent_frame_1 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_1.place(x=0,y=0)
        self.parent_frame_2 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_2.place(x=0,y=128)
        self.parent_frame_3 = tk.Frame(self, bg='#fcf3e7', width='560', height='128')
        self.parent_frame_3.place(x=0,y=256)
        # 一時的にparent_frameを消す
        self.parent_frame_1.place_forget()
        self.parent_frame_2.place_forget()
        self.parent_frame_3.place_forget()

    # トークエリア一段目
    def talk_area_stage_1(self):
        self.svar_question_1 = tk.StringVar() 
        self.image_girl1 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', image=self.image_girl1)
        self.label_image1.place(x=0, y=0) 
        self.label_comment1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', textvariable=self.svar_question_1, font='100')
        self.label_comment1.place(x=64, y=0, height=68)
        self.svar_state = tk.StringVar()
        self.svar_state.set('active')
        self.frame_button1 = tk.Frame(self.parent_frame_1, width='280', height='64', bg='#fcf3e7')
        self.frame_button1.place(x=0, y=64)
        text_color_list_1 = [('', 'magenta'), ('', 'pink'), ('', 'SeaGreen'), ('', 'LightSkyBlue'), ('', 'pink'), ('', 'yellow')]
        self.button_list1 = []
        for cn, (text, color) in enumerate(text_color_list_1):
            self.button1 = tk.Button(self.frame_button1, text=text, bg=color, width=9, height=2, 
                                     command=self.button1_command)
            self.button_list1.append(self.button1)
            self.button_list1[cn].grid(row=0, column=cn, sticky=self.sticky, padx='1', ipadx='1', pady='10')

    # トークエリア二段目
    def talk_area_stage_2(self):
        self.svar_question_2 = tk.StringVar()
        self.image_girl2 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', image=self.image_girl2)
        self.label_image2.place(x=0, y=0)
        self.label_comment2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', textvariable=self.svar_question_2, font='100')
        self.label_comment2.place(x=64, y=0, height=68, )
        self.frame_button2 = tk.Frame(self.parent_frame_2, width='280', height='64', bg='#fcf3e7')
        self.frame_button2.place(x=0, y=64)
        text_color_list_2 = [('', 'magenta'), ('', 'yellow'), ('', 'SeaGreen'), ('', 'LightSkyBlue'), ('', 'pink'), ('', 'yellow')]
        self.button_list2 = []
        for cn, (text, color) in enumerate(text_color_list_2):
            self.button2 = tk.Button(self.frame_button2, text=text, bg=color, width=9, height=2, 
                                     command=self.button2_command)
            self.button_list2.append(self.button2)
            self.button_list2[cn].grid(row=0, column=cn, sticky=self.sticky, padx='1', ipadx='1', pady='10')

    # トークエリア三段目
    def talk_area_stage_3(self):
        self.svar_question_3 = tk.StringVar()
        self.image_girl3 = tk.PhotoImage(file = self.curdir+'/../../material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', image=self.image_girl3)
        self.label_image3.place(x=0, y=0)
        self.label_comment3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', textvariable=self.svar_question_3, font='100')
        self.label_comment3.place(x=64, y=0, height=68, )  
        self.frame_button3 = tk.Frame(self.parent_frame_3, width='280', height='64', bg='#fcf3e7')
        self.frame_button3.place(x=0, y=64)
        text_color_list_3 = [('', 'magenta'), ('', 'yellow'), ('', 'SeaGreen'), ('', 'LightSkyBlue'), ('', 'pink'), ('', 'yellow')]
        self.button_list3 = []
        for cn, (text, color) in enumerate(text_color_list_3):
            self.button3 = tk.Button(self.frame_button3, text=text, bg=color, width=9, height=2, 
                                     command=self.button3_command)
            self.button_list3.append(self.button3)
            self.button_list3[cn].grid(row=0, column=cn, sticky=self.sticky, padx='1', ipadx='1', pady='10')

    # トークエリア１段目のボタンコマンド
    def button1_command(self):    
        self.parent_frame_2.place(x=0,y=128)
        self.parent_frame_rotation_2()
        self.button_list1[0].config(state='disabled')
        self.button_list1[1].config(state='disabled')
        self.button_list1[2].config(state='disabled')
        self.button_list1[3].config(state='disabled')
        self.button_list1[4].config(state='disabled')
        self.button_list1[5].config(state='disabled')

        self.button_list2[0].config(state='active')
        self.button_list2[1].config(state='active')
        self.button_list2[2].config(state='active')
        self.button_list2[3].config(state='active')
        self.button_list2[4].config(state='active')
        self.button_list2[5].config(state='active')
    # トークエリア２段目のボタンコマンド
    def button2_command(self):
        self.parent_frame_3.place(x=0, y=256)
        self.parent_frame_rotation_3()
        self.button_list2[0].config(state='disabled')
        self.button_list2[1].config(state='disabled')
        self.button_list2[2].config(state='disabled')
        self.button_list2[3].config(state='disabled')
        self.button_list2[4].config(state='disabled')
        self.button_list2[5].config(state='disabled')
        self.button_list3[0].config(state='active')
        self.button_list3[1].config(state='active')
        self.button_list3[2].config(state='active')
        self.button_list3[3].config(state='active')
        self.button_list3[4].config(state='active')
        self.button_list3[5].config(state='active')
    # トークエリア３段目のボタンコマンド
    def button3_command(self): 
        self.parent_frame_rotation_1()
        self.button_list3[0].config(state='disabled')
        self.button_list3[1].config(state='disabled')
        self.button_list3[2].config(state='disabled')
        self.button_list3[3].config(state='disabled')
        self.button_list3[4].config(state='disabled')
        self.button_list3[5].config(state='disabled')
        self.button_list1[0].config(state='active')
        self.button_list1[1].config(state='active')
        self.button_list1[2].config(state='active')
        self.button_list1[3].config(state='active')
        self.button_list1[4].config(state='active')
        self.button_list1[5].config(state='active')


    # トークを入れ替える関数
    def parent_frame_rotation_1(self):
        if self.counter % 3 == 0 :
            self.parent_frame_3.place(x=0, y=128)
            self.parent_frame_1.place(x=0, y=256)
            self.parent_frame_2.place(x=0, y=0)
            self.counter += 1

    def parent_frame_rotation_2(self):
        if self.counter % 3 == 1 :
            self.parent_frame_1.place(x=0, y=128)
            self.parent_frame_2.place(x=0, y=256)
            self.parent_frame_3.place(x=0, y=0)

    def parent_frame_rotation_3(self):
        if self.counter % 3 == 1 :
            self.parent_frame_2.place(x=0, y=128)
            self.parent_frame_3.place(x=0, y=256)
            self.parent_frame_1.place(x=0, y=0)
            self.counter -= 1

    def button_distance(self, event):
        self.data_list = []
        self.svar_question_1.set('どの範囲で探す？')
        self.svar_question_2.set('予算はいくら？')
        self.svar_question_3.set('どのジャンルがいいかな？')
        self.button_list1[0].config(text='300m')
        self.button_list1[1].config(text='500m')
        self.button_list1[2].config(text='1000m')
        self.button_list1[3].config(text='2000m')
        self.button_list1[4].config(text='5000m')
        self.button_list2[0].config(text='500円')
        self.button_list2[1].config(text='1000円')
        self.button_list2[2].config(text='1500円')
        self.button_list2[3].config(text='2000円')
        self.button_list2[4].config(text='3000円')
        self.button_list3[0].config(text='中華')
        self.button_list3[1].config(text='和食')
        self.button_list3[2].config(text='洋食')
        self.button_list3[3].config(text='ラーメン')
        self.button_list3[4].config(text='カレーライス')
        self.button_list3[5].config(text='その他の料理')
        self.button_list1[0].bind('<Button>', lambda event: self.params_list.append('300m'))
        self.button_list1[1].bind('<Button>', lambda event: self.params_list.append('500m'))
        self.button_list1[2].bind('<Button>', lambda event: self.params_list.append('1000m'))
        self.button_list1[3].bind('<Button>', lambda event: self.params_list.append('2000m'))
        self.button_list1[4].bind('<Button>', lambda event: self.params_list.append('5000m'))
        self.button_list2[0].bind('<Button>', lambda event: self.params_list.append('500円'))
        self.button_list2[1].bind('<Button>', lambda event: self.params_list.append('1000円'))
        self.button_list2[2].bind('<Button>', lambda event: self.params_list.append('1500円'))
        self.button_list2[3].bind('<Button>', lambda event: self.params_list.append('2000円'))
        self.button_list2[4].bind('<Button>', lambda event: self.params_list.append('3000円'))
        self.button_list3[0].bind('<Button>', lambda event: self.params_list.append('中華'))
        self.button_list3[1].bind('<Button>', lambda event: self.params_list.append('和食'))
        self.button_list3[2].bind('<Button>', lambda event: self.params_list.append('洋食'))
        self.button_list3[3].bind('<Button>', lambda event: self.params_list.append('ラーメン'))
        self.button_list3[4].bind('<Button>', lambda event: self.params_list.append('カレーライス'))
        self.button_list3[5].bind('<Button>', lambda event: self.params_list.append('その他の料理'))
    def button_yen(self, event):
        self.svar_question_1.set('予算はいくら？')
        self.svar_question_2.set('どのジャンルがいいかな？')
        self.svar_question_3.set('どの範囲で探す？')
        self.button_list1[0].config(text='500円')
        self.button_list1[1].config(text='1000円')
        self.button_list1[2].config(text='1500円')
        self.button_list1[3].config(text='2000円')
        self.button_list1[4].config(text='3000円')
        self.button_list3[0].config(text='300m')
        self.button_list3[1].config(text='500m')
        self.button_list3[2].config(text='1000m')
        self.button_list3[3].config(text='2000m')
        self.button_list3[4].config(text='5000m')
        self.button_list2[0].config(text='中華')
        self.button_list2[1].config(text='和食')
        self.button_list2[2].config(text='洋食')
        self.button_list2[3].config(text='ラーメン')
        self.button_list2[4].config(text='カレーライス')
        self.button_list2[5].config(text='その他の料理')
        self.button_list1[0].bind('<Button>', lambda event: self.params_list.append('500円'))
        self.button_list1[1].bind('<Button>', lambda event: self.params_list.append('1000円'))
        self.button_list1[2].bind('<Button>', lambda event: self.params_list.append('1500円'))
        self.button_list1[3].bind('<Button>', lambda event: self.params_list.append('2000円'))
        self.button_list1[4].bind('<Button>', lambda event: self.params_list.append('3000円'))
        self.button_list3[0].bind('<Button>', lambda event: self.params_list.append('300m'))
        self.button_list3[1].bind('<Button>', lambda event: self.params_list.append('500m'))
        self.button_list3[2].bind('<Button>', lambda event: self.params_list.append('1000m'))
        self.button_list3[3].bind('<Button>', lambda event: self.params_list.append('2000m'))
        self.button_list3[4].bind('<Button>', lambda event: self.params_list.append('5000m'))
        self.button_list2[0].bind('<Button>', lambda event: self.params_list.append('中華'))
        self.button_list2[1].bind('<Button>', lambda event: self.params_list.append('和食'))
        self.button_list2[2].bind('<Button>', lambda event: self.params_list.append('洋食'))
        self.button_list2[3].bind('<Button>', lambda event: self.params_list.append('ラーメン'))
        self.button_list2[4].bind('<Button>', lambda event: self.params_list.append('カレーライス'))
        self.button_list2[5].bind('<Button>', lambda event: self.params_list.append('その他の料理'))
    def button_genre(self, event):
        self.svar_question_1.set('どのジャンルがいいかな？')
        self.svar_question_2.set('どの範囲で探す？')
        self.svar_question_3.set('予算はいくら？')
        self.button_list2[0].config(text='300m')
        self.button_list2[1].config(text='500m')
        self.button_list2[2].config(text='1000m')
        self.button_list2[3].config(text='2000m')
        self.button_list2[4].config(text='5000m')
        self.button_list3[0].config(text='500円')
        self.button_list3[1].config(text='1000円')
        self.button_list3[2].config(text='1500円')
        self.button_list3[3].config(text='2000円')
        self.button_list3[4].config(text='3000円')
        self.button_list1[0].config(text='中華')
        self.button_list1[1].config(text='和食')
        self.button_list1[2].config(text='洋食')
        self.button_list1[3].config(text='ラーメン')
        self.button_list1[4].config(text='カレーライス')
        self.button_list1[5].config(text='その他の料理')
        self.button_list2[0].bind('<Button>', lambda event: self.params_list.append('300m'))
        self.button_list2[1].bind('<Button>', lambda event: self.params_list.append('500m'))
        self.button_list2[2].bind('<Button>', lambda event: self.params_list.append('1000m'))
        self.button_list2[3].bind('<Button>', lambda event: self.params_list.append('2000m'))
        self.button_list2[4].bind('<Button>', lambda event: self.params_list.append('5000m'))
        self.button_list3[0].bind('<Button>', lambda event: self.params_list.append('500円'))
        self.button_list3[1].bind('<Button>', lambda event: self.params_list.append('1000円'))
        self.button_list3[2].bind('<Button>', lambda event: self.params_list.append('1500円'))
        self.button_list3[3].bind('<Button>', lambda event: self.params_list.append('2000円'))
        self.button_list3[4].bind('<Button>', lambda event: self.params_list.append('3000円'))
        self.button_list1[0].bind('<Button>', lambda event: self.params_list.append('中華'))
        self.button_list1[1].bind('<Button>', lambda event: self.params_list.append('和食'))
        self.button_list1[2].bind('<Button>', lambda event: self.params_list.append('洋食'))
        self.button_list1[3].bind('<Button>', lambda event: self.params_list.append('ラーメン'))
        self.button_list1[4].bind('<Button>', lambda event: self.params_list.append('カレーライス'))
        self.button_list1[5].bind('<Button>', lambda event: self.params_list.append('その他の料理'))



def run():
    root = tk.Tk()
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Widget(root)
    root.mainloop()
if __name__ == '__main__':
    run()