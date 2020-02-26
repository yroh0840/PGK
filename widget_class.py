##################################    ウィジェットのモジュール    ####################################

import tkinter as tk
import os
import webbrowser
from is_gurunabi import *
class Widget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.counter = 0

    # ウィジェットの配置
    def create_widgets(self):
        self.canvass() # 背景画像表示
        self.first_buttons() # 最初のボタン表示
        self.talk_area() # トークエリア
        self.talk_area_stage_1() # トークエリア一段目
        self.talk_area_stage_2() # トークエリア二段目
        self.talk_area_stage_3() # トークエリア三段目
        self.svar = tk.StringVar()
        self.message = tk.Message(self, textvariable=self.svar, width='560', cursor='hand2')
        self.message.place(x=0, y=500)
        self.message.place_forget()

   # 背景画像表示
    def canvass(self):
        self.curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得
        self.image = tk.PhotoImage(file = self.curdir+'/./material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW)

    @staticmethod
    def frame(source, width, height, bg='#fcf3e7', x=0, y=None):
        obj = tk.Frame(source, width=width, height=height, bg=bg)
        obj.place(x = x, y = y)
        return obj

    # 最初のボタン表示   >>>>>>>>>>>>>>>>>>>>>>> 1 ########
    def first_buttons(self):
        self.sticky = tk.W+tk.E+tk.N+tk.S
        for n, l in enumerate(["distance", "budget", "genre"], 1):
            exec(f"self.first_button_image_{n} = tk.PhotoImage(file = self.curdir+'/./material/buttons&entrywindows/{l}_icon.png')")
        self.bottom_frame = self.frame(self, '560', '100', y=0)
        image_list = [self.first_button_image_1, self.first_button_image_2, self.first_button_image_3]
        first_button_list = []
        for n, image in enumerate(image_list, 1):
            self.first_button = tk.Button(self.bottom_frame, image=image, width='170', height='100', command=lambda:[self.parent_frame_1.place(x=0, y=0), self.bottom_frame.destroy()])
            self.first_button.pack(padx='2', side='left')
            first_button_list.append(self.first_button)
        for fbl, func in zip(first_button_list, [self.button_distance, self.button_yen, self.button_genre]):
            fbl.bind('<Button-1>', func)
        
    # トークエリアに入れるテキスト >>>>>>>>>>>>>>>>>>>>>>>>  2 ############
    def talk_area(self):
        for n, y in enumerate([0, 128, 256], 1):
            exec(f"self.parent_frame_{n} = self.frame(self, '560', '128', y={y})")
     
        # 一時的にparent_frameを消す  >>>>>>>>>>>>>>>>>>>>  3 ##############
        for n in range(1,4):
            exec(f"self.parent_frame_{n}.place_forget()")
            
    # トークエリア一段目             >>>>>>>>>>>>>>>>>>>>>>>>> 4
    def talk_area_stage_1(self):
        self.svar_question_1 = tk.StringVar() 
        self.image_girl1 = tk.PhotoImage(file = self.curdir+'/./material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', image=self.image_girl1)
        self.label_image1.place(x=0, y=0) 
        self.label_comment1 = tk.Label(self.parent_frame_1, bg='#fcf3e7', textvariable=self.svar_question_1, font='100')
        self.label_comment1.place(x=64, y=0, height=68)
        self.svar_state = tk.StringVar()
        self.svar_state.set('active')
        self.frame_button1 = self.frame(self.parent_frame_1, '280', '64', y=64)
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
        self.image_girl2 = tk.PhotoImage(file = self.curdir+'/./material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', image=self.image_girl2)
        self.label_image2.place(x=0, y=0)
        self.label_comment2 = tk.Label(self.parent_frame_2, bg='#fcf3e7', textvariable=self.svar_question_2, font='100')
        self.label_comment2.place(x=64, y=0, height=68, )
        self.frame_button2 = self.frame(self.parent_frame_2, '280', '64', y=64)
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
        self.image_girl3 = tk.PhotoImage(file = self.curdir+'/./material/buttons&entrywindows/girl_01_invi_circle.png')
        self.label_image3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', image=self.image_girl3)
        self.label_image3.place(x=0, y=0)
        self.label_comment3 = tk.Label(self.parent_frame_3, bg='#fcf3e7', textvariable=self.svar_question_3, font='100')
        self.label_comment3.place(x=64, y=0, height=68, )  
        self.frame_button3 = self.frame(self.parent_frame_3, '280', '64', y=64)
        text_color_list_3 = [('', 'magenta'), ('', 'yellow'), ('', 'SeaGreen'), ('', 'LightSkyBlue'), ('', 'pink'), ('', 'yellow')]
        self.button_list3 = []
        for cn, (text, color) in enumerate(text_color_list_3):
            self.button3 = tk.Button(self.frame_button3, text=text, bg=color, width=9, height=2, 
                                     command=self.button3_command)
            self.button_list3.append(self.button3)
            self.button_list3[cn].grid(row=0, column=cn, sticky=self.sticky, padx='1', ipadx='1', pady='10')

    # トークエリア１段目のボタンコマンド >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  5
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
    # トークエリア２段目のボタンコマンド   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  6
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
    # トークエリア３段目のボタンコマンド >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  7
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


    # トークを入れ替える関数 >>>>>>>>>>>>>>>>>>>>>>>>>>  7
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
    # 最初のボタン　範囲ボタンを押した後  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  9
    def button_distance(self, event):
        self.svar_question_1.set('どの範囲で探す？')
        self.svar_question_2.set('予算はいくら？')
        self.svar_question_3.set('どのジャンルがいいかな？')
        self.button_list1[0].config(text='300m')
        self.button_list1[1].config(text='500m')
        self.button_list1[2].config(text='1000m')
        self.button_list1[3].config(text='2000m')
        self.button_list1[4].config(text='3000m')
        self.button_list2[0].config(text='500円')
        self.button_list2[1].config(text='1000円')
        self.button_list2[2].config(text='1500円')
        self.button_list2[3].config(text='2000円')
        self.button_list2[4].config(text='3000円')
        self.button_list3[0].config(text='ラーメン')
        self.button_list3[1].config(text='カレーライス')
        self.button_list3[2].config(text='その他の料理')
        self.button_list3[3].config(text='')
        self.button_list3[4].config(text='')
        self.button_list3[5].config(text='')
        self.button_list1[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,300m'))
        self.button_list1[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,500m'))
        self.button_list1[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,1000m'))
        self.button_list1[3].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,2000m'))
        self.button_list1[4].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,3000m'))
        self.button_list2[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,500円'))
        self.button_list2[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,1000円'))
        self.button_list2[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,1500円'))
        self.button_list2[3].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,2000円'))
        self.button_list2[4].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,3000円'))
        self.button_list3[0].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',genre,ラーメン'), self.tmp()])
        self.button_list3[1].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',genre,カレーライス'), self.tmp()])
        self.button_list3[2].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',genre,その他の料理'), self.tmp()])
        self.button_list3[3].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+''))
        self.button_list3[4].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+''))
        self.button_list3[5].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+''))
    def button_yen(self, event): # 円ボタンを押した後
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
        self.button_list3[4].config(text='3000m')
        self.button_list2[0].config(text='ラーメン')
        self.button_list2[1].config(text='カレーライス')
        self.button_list2[2].config(text='その他の料理')
        self.button_list2[3].config(text='')
        self.button_list2[4].config(text='')
        self.button_list2[5].config(text='')
        self.button_list1[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,500円'))
        self.button_list1[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,1000円'))
        self.button_list1[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,1500円'))
        self.button_list1[3].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,2000円'))
        self.button_list1[4].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',yen,3000円'))
        self.button_list2[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,ラーメン'))
        self.button_list2[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,カレーライス'))
        self.button_list2[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,その他の料理'))
        self.button_list2[3].bind('<Button-1>', lambda event: self.svar.set(''))
        self.button_list2[4].bind('<Button-1>', lambda event: self.self.set(''))
        self.button_list2[5].bind('<Button-1>', lambda event: self.svar.set(''))
        self.button_list3[0].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',range,300m'), self.tmp()])
        self.button_list3[1].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',range,500m'), self.tmp()])
        self.button_list3[2].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',range,1000m'), self.tmp()])
        self.button_list3[3].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',range,2000m'), self.tmp()])
        self.button_list3[4].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',range,3000m'), self.tmp()])
        
    def button_genre(self, event): # ジャンルボタンを押した後
        self.svar_question_1.set('どのジャンルがいいかな？')
        self.svar_question_2.set('どの範囲で探す？')
        self.svar_question_3.set('予算はいくら？')
        self.button_list2[0].config(text='300m')
        self.button_list2[1].config(text='500m')
        self.button_list2[2].config(text='1000m')
        self.button_list2[3].config(text='2000m')
        self.button_list2[4].config(text='3000m')
        self.button_list3[0].config(text='500円')
        self.button_list3[1].config(text='1000円')
        self.button_list3[2].config(text='1500円')
        self.button_list3[3].config(text='2000円')
        self.button_list3[4].config(text='3000円')
        self.button_list1[0].config(text='ラーメン')
        self.button_list1[1].config(text='カレーライス')
        self.button_list1[2].config(text='その他の料理')
        self.button_list1[3].config(text='')
        self.button_list1[4].config(text='')
        self.button_list1[5].config(text='')
        self.button_list1[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,ラーメン'))
        self.button_list1[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,カレーライス'))
        self.button_list1[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',genre,その他の料理'))
        self.button_list1[3].bind('<Button-1>', lambda event: self.svar.set(''))
        self.button_list1[4].bind('<Button-1>', lambda event: self.self.set(''))
        self.button_list1[5].bind('<Button-1>', lambda event: self.svar.set(''))
        self.button_list2[0].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,300m'))
        self.button_list2[1].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,500m'))
        self.button_list2[2].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,1000m'))
        self.button_list2[3].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,2000m'))
        self.button_list2[4].bind('<Button-1>', lambda event: self.svar.set(self.svar.get()+',range,3000m'))
        self.button_list3[0].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',yen,500円'), self.tmp()])
        self.button_list3[1].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',yen,1000円'), self.tmp()])
        self.button_list3[2].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',yen,1500円'), self.tmp()])
        self.button_list3[3].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',yen,2000円'), self.tmp()])
        self.button_list3[4].bind('<Button-1>', lambda event: [self.svar.set(self.svar.get()+',yen,3000円'), self.tmp()])
        
    def link(self, event):
        if not self.result_shop_info == None:
            webbrowser.open_new(self.result_shop_info[0][2])

    def tmp(self):
        self.parent_frame_1.destroy(), self.parent_frame_2.destroy(), self.parent_frame_3.destroy()
        self.message.place(x=0, y=0)
        self.message.bind('<Button-1>', self.link)
        guru = GurunabiResponder()
        resultVar = tk.StringVar()
        l = self.svar.get().lstrip(',').split(',')
        d = {key:value for key, value in zip(l[0::2], l[1::2])}
        r = d['range']
        y = d['yen']
        g = d['genre']
        self.result_shop_info = guru.is_gurunabi(r,y,g)
        if self.result_shop_info == None:
            self.svar.set('すみません。\nその条件ではお店が見つかりませんでした。')
        else:
            result_message = 'お店情報だよ！\n\nお店の名前は\n'+str(self.result_shop_info[0][0])+'\n\n平均予算は\n'+str(self.result_shop_info[0][1])+'円'+'\n\nURLは\n'+str(self.result_shop_info[0][2])
            self.svar.set(result_message)