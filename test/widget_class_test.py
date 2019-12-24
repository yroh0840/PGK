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
        self.image = # 画像ファイル
        self.img 
        self.label_image = tk.Label(self, image=)
        self.label = tk.Label(self, text='飯いくぞ！')
        self.label.place(x=100, y=20, width='100', height='50')     
        self.frame = tk.Frame(self, bg='lightgreen')
        self.frame.place(x=250, y=60, width='250', height='50')
        self.sticky = tk.W+tk.E+tk.N+tk.S
        for cn, (text, color) in enumerate([('A', 'magenta'), ('B', 'yellow'), ('C', 'SeaGreen'), ('D', 'LightSkyBlue')]):
            self.button = tk.Button(self.frame, text=text, bg=color, width=4)
            self.button.grid(row=0, column=cn, sticky=self.sticky, padx='10', pady='10')
        



def run():
    root = tk.Tk()
    root.geometry('540x960')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()