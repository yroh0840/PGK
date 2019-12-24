import tkinter as tk
     
class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, height=200, width=200)
        self.master.title('Nested Frames')

        # First Frame
        f1 = tk.Frame(self, relief=tk.RIDGE, bd=2)
        
        f1.place(relx=0.2, rely=0.2)
        
##----------------
if __name__ == '__main__':
    root = tk.Tk()
    app = Frame(root)
    root.mainloop()