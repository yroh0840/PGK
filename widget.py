import tkinter as tk

# グローバル変数の定義



# 画面を描画する関数

def run():
    # グローバル変数を使用するための記述
    
    # メインウインドウを作成
    root = tk.Tk()
    # [確定]ウィンドウサイズを設定
    root.geometry('1080x1920') 
    # ウィンドウタイトルを設定
    root.title('ゴハンゴ')
    # 仮）フォントの用意
    font=('Helevetica', 14)
    font_log=('Helevetica', 11)

    #キャンバスの作成
    canvas = tk.Canvas(
                root,              # 親要素をメインウィンドウに設定
                width = 35,       # 幅を設定
                height = 30,      # 高さを設定
                relief=tk.RIDGE,   # 枠線を表示
                bd=2               # 枠線の幅を設定
            )
    canvas.place(x=370, y=0)       # メインウィンドウ上に配置

    img = tk.PhotoImage(file = r'C:\Users\pcuser\AppData\Local\Programs\Python\Python37\images.png')    # 表示するイメージを用意
    canvas.create_image(                      # キャンバス上にイメージを配置
        0,                                    # x座標
        0,                                    # y座標
        image = img,                          # 配置するイメージオブジェクトを指定
        anchor = tk.NW                        # 配置の起点となる位置を左上隅に指定
    )

    # 応答エリアを作成
    response_area = tk.Label(
                        root,                 # 親要素をメインウィンドウに設定
                        width=35,             # 幅を設定
                        height=30,            # 高さを設定
                        bg='yellow',           # 背景色を設定
                        font=font,            # フォントを設定
                        relief=tk.RIDGE,      # 枠線の種類を設定
                        bd=2                  # 枠線の幅を設定
                    )
    response_area.place(x=370, y=305)         # メインウィンドウ上に配置

    # フレームの作成
    frame = tk.Frame(
                root,                         # 親要素はメインウィンドウ
                relief=tk.RIDGE,              # ボーダーの種類
                borderwidth = 4               # ボーダーの幅を設定
            )

    # リストボックスを作成
    lb = tk.Listbox(
            root,                             # 親要素はメインウインドウ
            width=91,                         # 幅を設定
            height=30,                        # 高さを設定
            font=font_log                     # フォントを設定
    )
    # 縦のスクロールバーを生成
    sb1 = tk.Scrollbar(
            root,                             # 縦要素はメインウィンドウ
            orient = tk.VERTICAL,             # 縦方向のスクロールバーにする
            command = lb.yview                # スクロール時にListboxのyview()メソッドを呼ぶ
    )
    # リストボックスとスクロールバーを連動させる
    lb.configure(yscrollcommand = sb1.set)
    # grid()でリストボックス、スクロールバーを画面上に配置
    lb.grid(row = 0, column = 0)
    sb1.grid(row = 0, column = 1, sticky = tk.NS)

    # ボタンの作成
    button = tk.Button(
                frame,
                width=5,
                text ='開始',
                #bg='#f0e68c',
                #fg='#ff0000',
                #command=
        )
    button.pack(side = tk.LEFT)
    frame.place(x=700, y=1300)

    # メインループ
    root.mainloop()

# プログラムの起点
if __name__ == '__main__':
    run()

    

