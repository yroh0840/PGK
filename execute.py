from widget_class import *
#from is_gurunabi import *

#gurunabi = GurunabiResponder()

#print(gurunabi.is_gurunabi('3000m', '3000円', '中華'))
def run():
    root = tk.Tk()
    root.geometry('540x960+0+0')
    root.title('ゴハンゴ')
    app = Widget(root)
    root.mainloop()

if __name__ == '__main__':
    run()


