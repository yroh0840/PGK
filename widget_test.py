import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X)
        
        
def run():
    root = tk.Tk()
    root.geometry('1080x1920')
    root.title('ゴハンゴ')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    run()

