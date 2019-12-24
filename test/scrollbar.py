import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

# Canvas Widget を生成
canvas = tk.Canvas(root)

# Top Widget上に Scrollbar を生成して配置
bar = tk.Scrollbar(root, orient=tk.VERTICAL)
bar.pack(side=tk.RIGHT, fill=tk.Y)
bar.config(command=canvas.yview) # ScrollbarでCanvasを制御

# Canvas Widget をTopWidget上に配置
canvas.config(yscrollcommand=bar.set) # Canvasのサイズ変更をScrollbarに通知
canvas.config(scrollregion=(0,0,500,2000)) #スクロール範囲

canvas.bind_all("<MouseWheel>", lambda eve:canvas.yview_scroll(int(-eve.delta/120), 'units'))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame Widgetを 生成
frame = tk.Frame(canvas)

# Frame Widgetを Canvas Widget上に配置（）
canvas.create_window((0,0), window=frame, anchor=tk.NW, width=500, height=500)

# Frame Widget上に各種ラベルを表示
aaa = tk.Label(frame, text='aaa')
aaa.place(x=20, y=20)

bbb = tk.Label(frame, text='bbb')
bbb.place(x=20, y=40)

ccc = tk.Label(frame, text='ccc')
ccc.place(x=20, y=450)

ddd = tk.Label(frame, text='ddd')
ddd.place(x=450, y=450)

root.mainloop()
