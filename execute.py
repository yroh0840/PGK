####################################    実行モジュール    ###############################################

from widget_class import *
from is_gurunabi import *

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Widget(root)
    app.mainloop()


