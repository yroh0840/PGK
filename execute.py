from .tests.widget_tests.widget_class_test import *

def run():
    root = tk.Tk()
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Widget(root)
    root.mainloop()

if __name__ == '__main__':
    run()


