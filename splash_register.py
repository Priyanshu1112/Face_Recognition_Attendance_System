import tkinter as tk
from tkinter import ttk
import register_view

class Splash_Register:
    def __init__(self, root):
        self.main_root = root
        self.root = tk.Toplevel()
        self.root.geometry('500x300+450+200')
        self.root.overrideredirect(True)
        self.root.config(bg='#ceefba')
        self.lbl = tk.Label(self.root, text='Loading Register Screen', anchor='center', font=('Arial', 15), bg='#ceefba')
        self.pb = ttk.Progressbar(self.root, orient='horizontal', mode='determinate', length=460)
        self.lbl_status = tk.Label(self.root, bg='#ceefba', text= 'Status: Loading widgets')

        self.lbl.place(relx=0.22, rely=0.25, relheight=0.3, relwidth=0.6)
        self.pb.place(relx=0.05, rely=0.7)
        self.lbl_status.place(relx=0.3, rely=0.8)

    def rgv(self):
        self.rgv_obj = register_view.Register_view(self.main_root, self.root, self.pb, self.lbl_status)
        #print('back')
        self.rgv_obj.run()

    def run(self):
        self.root.after(1000, self.rgv)
        self.root.mainloop()

if __name__ == '__main__':
    obj = Splash_Register()
    obj.run()


