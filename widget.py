import tkinter as tk

# グローバル変数の定義
response_area = None              # 応答エリアのオブジェクトを保持
lb = None                         # ログ表示用リストボックスを保持
action = None                     # 'オプション'メニューの状態を保持

# 画面を描画する関数
def run():
    # グローバル変数を使用するための記述
    global response_area, lb, action
    # メインウインドウを作成
    root = tk.Tk()
    # ウィンドウサイズを設定
    root.geometry('1080x1920') 
    # ウィンドウタイトルを設定
    root.title('ゴハンゴ')
    # フォントの用意
    font=('Helevetica', 14)
    font_log=('Helevetica', 11)
    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    # ファイルメニュー
    filemenu = tk.Menu(root)
    menubar.add_cascade(label='ファイル', menu=filemenu)
    filemenu.add_command(label='閉じる', command=root.destroy)
    # メニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='メニュー', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='和食',                     # アイテム名
        #variable = action,                           # 選択時の値を格納するオブジェクト
        #value = 0                                    # actionの値を0にする
    )
    optionmenu.add_radiobutton(
        label='洋食',                # アイテム名
        #variable = action,                           # 選択時の値を格納するオブジェクト
        #value = 0                                    # actionの値を0にする
    )
    optionmenu.add_radiobutton(
        label='中華',                # アイテム名
        #variable = action,                           # 選択時の値を格納するオブジェクト
        #value = 0                                    # actionの値を0にする
    )
    optionmenu.add_radiobutton(
        label='ファーストフード',                # アイテム名
        #variable = action,                           # 選択時の値を格納するオブジェクト
        #value = 0                                    # actionの値を0にする
    )


    #キャンバスの作成
    canvas = tk.Canvas(
                root,              # 親要素をメインウィンドウに設定
                width = 35,       # 幅を設定
                height = 30,      # 高さを設定
                relief=tk.RIDGE,   # 枠線を表示
                bd=2               # 枠線の幅を設定
            )
    canvas.place(x=370, y=0)       # メインウィンドウ上に配置

    img = tk.PhotoImage(file = r'C:\Users\pcuser\Documents\GitHub\PGK\material\boys&girls\boy_01_invi.png')    # 表示するイメージを用意
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
                        #bg='yellow',           # 背景色を設定
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
    # ボタンの作成
    button = tk.Button(
                frame,                        # 親要素はフレーム
                width=5,                      # 幅を設定
                text ='開始',                  # ボタンに表示するテキスト
                #bg='#f0e68c',
                #fg='#ff0000',
                #command=
        )
    button.pack(side = tk.LEFT)               # フレームに左詰で配置する
    frame.place(x=700, y=1300)                # フレームを画面上に配置


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
    # 横のスクロールバーを生成
    sb2 = tk.Scrollbar(
            root,                             # 親要素はメインウインドウ
            orient = tk.HORIZONTAL,            # 横方向のスクロールバーにする
            command = lb.xview                # スクロール時にListboxのxview()メソッドを呼ぶ
    )
    # リストボックスとスクロールバーを連動させる
    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)
    # grid()でリストボックス、スクロールバーを画面上に配置
    lb.grid(row = 0, column = 0)
    sb1.grid(row = 0, column = 1, sticky = tk.NS)
    sb2.grid(row = 1, column = 0, sticky = tk.EW)

    # メインループ
    root.mainloop()

# プログラムの起点
if __name__ == '__main__':
    run()

    

