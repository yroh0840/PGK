from widget_class import *
from guru_test import *

class Execute(Widget, GurunabiResponder):
    def __init__(self):
        super(Execute, self).__init__()
        super(GurunabiResponder, self).__init__()
    
    @staticmethod
    def run():
        root = tk.Tk()
        root.geometry('540x960+0+0')
        root.title('ゴハンゴ')
        app = Widget(root)
        root.mainloop()

if __name__ == '__main__':
    ex = Execute()
    ex.run()


