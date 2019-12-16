import tkinter as tkinter

# グローバル変数の定義



# 画面を描画する関数

def run():
    # グローバル変数を使用するための記述

    # メインウインドウを作成
    root = tk.Tk()
    # 仮）ウィンドウサイズを設定
    root.geometry('560x880')
    # 仮）フォントの用意
    font=('Helevetica', 14)
    font_log=('Helevetica', 11)

    #キャンバスの作成
    canvas = tk.Canvas(
                root,              #親要素をメインウィンドウに設定
                width = 300,       #幅を設定
                height = 500,
                relief=tk.RIDGE,
                bd=2
            )
    canvas.place(x=370, y=0)