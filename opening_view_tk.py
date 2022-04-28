import time
import tkinter as tk
import traceback
from threading import Thread
import more_options_view
import splash_attendance
import splash_register

class Opening_view():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('''''')
        icon = tk.PhotoImage(file='icons/attendance_icon.png')
        self.root.iconphoto(self.root, icon)
        self.root.geometry("900x700+280+70")
        self.root.configure(bg="#b7dfbd")

        self.load_icon()       
        self.lbl_background = tk.Label(self.root, text='Label', image=self.background_icon)
        self.lbl_background.place(relx=0, rely=0, relheight=1, relwidth=1)
        

        self.btn_mic = tk.Button(self.lbl_background, bg='#ceefd8', image=self.mic_icon, command=self.mic)
        self.btn_register = tk.Button(self.lbl_background, bg='#cbeed8', text='  Register Student', image=self.register_icon, compound='left', command=self.register)
        self.btn_attendance = tk.Button(self.lbl_background, bg='#cbeed8', text='  Attendance', image=self.attendance_icon, compound='left', command=self.attendance)
        self.btn_more_options = tk.Button(self.lbl_background, bg='#ceefd8', text='  More Options', image=self.more_optoin_icon, compound='left', command=self.more_options)

        self.btn_register.place(relx=0.3, rely=0.32, relheight=0.05, relwidth=0.4)
        self.btn_attendance.place(relx=0.3, rely=0.43, relheight=0.05, relwidth=0.4)
        self.btn_more_options.place(relx=0.3, rely=0.54, relheight=0.05, relwidth=0.4)

        self.btn_mic.place(relx=0.965, rely=-0.001)

        self.lbl_time = tk.Label(self.lbl_background, bg='#c2956b')
        self.lbl_time.place(relx=0.89, rely=0.947)

    def load_icon(self):
        self.background_icon = tk.PhotoImage(file='icons/root_background.png')

        self.register_icon = tk.PhotoImage(file='icons/register_icon .png')
        self.attendance_icon = tk.PhotoImage(file='icons/attendance_icon.png')
        self.more_optoin_icon = tk.PhotoImage(file='icons/more_options.png')
        self.mic_icon = tk.PhotoImage(file='icons/microphone.png')

    def register(self):
        self.root.withdraw()
        self.sr_obj = splash_register.Splash_Register(self.root)
        self.sr_obj.run()

    def attendance(self):
        self.root.withdraw()
        self.sa_obj = splash_attendance.Splash_Attendance(self.root)
        self.sa_obj.run()

    def more_options(self):
        self.root.withdraw()
        self.mo_obj = more_options_view.More_options_view(self.root)
        self.mo_obj.run()

    def mic(self):
        pass

    def run(self):
        print('run')
        try:
            time_obj = cur_time(self.lbl_time)
            #time_obj.start()
            self.root.mainloop()
            time_obj.stop()
        except:
            print(traceback.format_exc())

class cur_time(Thread):
    def __init__(self, lbl_time):
        super().__init__()
        self.lbl_time = lbl_time
        self.run_thread = True

    def run(self):
        while self.run_thread:
            self.lbl_time.configure(text='Time:-'+time.strftime('%H:%M:%S'))
            time.sleep(1)

    def stop(self): #hello
        self.run_thread = False

if __name__ == '__main__':
    obj = Opening_view()
    obj.run()
