import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):#初期値を設定する特殊メソッド　特殊メソッドはクラス内全体に反映すると考えてよい
        super().__init__(master) # スーパークラスであるFrameの呼び出し
        self.pack()#呼び出したスーパークラスであるFrameを表示
        self.create_widgets()#ここで下記のcreate_widgetsメソッドを呼び出し

    def create_widgets(self):#ウィジェットを作るメソッド
        self.curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得
        self.image = tk.PhotoImage(file = self.curdir+'/material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        #self.place(x=0,y=0)
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW) # 画像を配置

        self.label = tk.Label(self, text='ささっと外食先決めましょ！')
        self.label.place(x=20, y=20, width='500', height='30')



def run():
    root = tk.Tk()
    root.geometry('540x960')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()

