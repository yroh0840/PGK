import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.curdir = os.path.dirname(__file__) # 現在のフォルダのパス取得
        self.image = tk.PhotoImage(file = self.curdir+'/material/backgrounds_02/background_girl02.png') # 画像のｲﾝｽﾀﾝｽ変数
        self.canvas = tk.Canvas(self, width=540, height=960, bg="white")
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.image, anchor=tk.NW)

        self.label = tk.Label(self, text='ささっと外食先決めましょ！')
        self.label.place(x=20, y=20, width='500', height='30')
        self.frame = tk.Frame(self, relief=tk.ridge, bd=2)
            for text, color in [('はい', 'gray'), ('いいえ', 'gray1'), ('どちらでもない', 'gray2')]:
                self.frame = tk.Label(self.frame, text=text, bg=color, font=('', '16'))             self.frame.pack(side=tk.Right)
        self.frame.place(x=40, y=0)



def run():
    root = tk.Tk()
    root.geometry('540x960')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()