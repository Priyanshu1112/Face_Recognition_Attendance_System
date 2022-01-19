import sys
import tkinter as tk
import time
from tkinter import messagebox
import traceback
import recognize_face
import db_controller

class Attendance_view:
    def __init__(self,main_root, root_splash, pb, lbl_status):
        self.main_root = main_root
        self.root_splash = root_splash
        self.pb = pb
        self.lbl_status = lbl_status
    #creating and designing root window
        self.lbl_status['text'] = 'Status: Loading widgets...'
        self.root_splash.update()
        self.root=tk.Toplevel()
        self.root.title('''Attendance''')
        icon=tk.PhotoImage(file='icons/attendance_icon.png')
        self.root.iconphoto(self.root, icon)
        self.root.geometry("900x700+280+70")
        self.root.configure(bg="#b7dfbd")
        self.pb['value'] += 5
        self.root_splash.update()
    #creating label frame
        self.lbl_frame_camera = tk.LabelFrame(self.root)
        self.lbl_frame_camera.configure(text='Camera')
        self.lbl_frame_camera.place(relx=0.043, rely=0.085, relheight=0.592
                                    , relwidth=0.651)
        self.lbl_frame_camera.configure(relief='groove')
        self.lbl_frame_camera.configure(foreground="black")
        self.lbl_frame_camera.configure(text='''Camera''')
        self.lbl_frame_camera.configure(background="#d9d9d9")
        self.pb['value'] += 5
        self.root_splash.update()
    #creating label
        self.lbl_camera = tk.Label(self.lbl_frame_camera)
        #self.lbl_camera.configure(text='Check')
        self.lbl_camera.pack()
    #creating back button
        self.btn_back = tk.Button(self.root)
        self.icon = tk.PhotoImage(file='icons/back.png')
        self.btn_back.configure(image=self.icon)
        self.btn_back.configure(background="#d3ebd7")
        self.btn_back.configure(foreground="#000000")
        self.btn_back.configure(command=self.back)
        self.btn_back.place(relx=0.00, rely=0.0, relheight=0.044, relwidth=0.07)
        self.pb['value'] += 5
        self.root_splash.update()
    #creating label name
        self.lbl_name = tk.Label(self.root)
        self.lbl_name.place(relx=0.043, rely=0.77, height=25, width=167)
        self.lbl_name.configure(background="#d3ebd7")
        self.lbl_name.configure(disabledforeground="#a3a3a3")
        self.lbl_name.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(text='''Name:-''')
        self.pb['value'] += 5
        self.root_splash.update()
    #creating entry name
        self.entry_name = tk.Entry(self.root)
        self.entry_name.place(relx=0.26, rely=0.77, height=25, relwidth=0.43)
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#a3a3a3")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(insertbackground="black")
        self.pb['value'] += 5
        self.root_splash.update()
    #creating button mark present
        self.btn_mark_present = tk.Button(self.root)
        self.btn_mark_present.place(relx=0.734, rely=0.177, height=73, width=216)
        self.btn_mark_present.configure(background="#d3ebd7")
        self.btn_mark_present.configure(foreground="#000000")
        self.btn_mark_present.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.btn_mark_present.configure(takefocus="")
        self.btn_mark_present.configure(text='''Mark Present''')
        self.btn_mark_present.configure(command=self.mark_present)
        self.pb['value'] += 5
        self.root_splash.update()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.root.withdraw()

    #creating recognize face obj
        self.lbl_status['text'] = 'Status: Creating rf obj ...'
        self.root_splash.update()
        try:
            self.rf_obj = recognize_face.Recognize_face(self.root, self.root_splash, self.lbl_camera, self.entry_name, self.pb)
            self.status=self.rf_obj.get_message()
            if self.status!='':
                messagebox.showerror('ERROR', 'Error in rf_obj:-'+self.status)
            else:
                self.pb['value'] += 4
                self.root.update()
        except:
            messagebox.showerror('Recognize face Error', 'Error in rf_obj')
            print(traceback.format_exc())
            sys.exit(1)

    #creating dbc_obj
        self.lbl_status['text'] = 'Status: Crating Dbc obj ...'
        self.root_splash.update()
        try:
            self.dbc_obj = db_controller.Db_controller()
            self.pb['value'] += 10
        except:
            messagebox.showerror('Recognize face Error', 'Error in rf_obj')
            print(traceback.format_exc())
            sys.exit(1)

    def open_camera(self):
        self.lbl_status['text'] = 'Status: Opening camera ...'
        self.root_splash.update()
        try:
            self.rf_obj.open_camera()
        except:
            print(traceback.format_exc())
            #sys.exit(1)

    def back(self):
        self.rf_obj.release()
        self.rf_obj.close_camera()
        self.main_root.deiconify()
        self.root.destroy()

    def mark_present(self):
        print('Mark present clicked')
        res = self.check_attendance()
        if res == 'None':
            if self.dbc_obj.get_start_time()<=str(time.strftime('%H:%M:%S'))<=self.dbc_obj.get_end_time():
                self.mark_student_present()
                eno=self.rf_obj.get_eno()
                print(eno)
                messagebox.showinfo('Successful', f'{eno} marked present')
            else:
                messagebox.showerror('ERROR', f'Mark attendance between {self.dbc_obj.get_start_time()} hour and {self.dbc_obj.get_end_time()} hour')
        elif res != 'NO ENO':
            if res == 'N':
                status='Absent'
            elif res == 'Y':
                status = 'Present'
            messagebox.showinfo('Already marked', f'Student already marked {status}')

    def check_attendance(self):
        try:
            eno = self.rf_obj.get_eno()
            if eno in ['UNKNOWN','']:
                messagebox.showerror('Enrollment number Error', 'Got no enrollment number')
                return "NO ENO"
            res = self.dbc_obj.check_attendance(eno)
            return res
        except:
            messagebox.showerror('ERROR', 'Error occured in checking attendance')
            print(traceback.format_exc())

    def mark_student_present(self):
        eno = self.rf_obj.get_eno()
        self.dbc_obj.mark_student_present(eno)

    def exit(self):
        self.root.destroy()
        self.root_splash.destroy()

    def run(self):
        self.open_camera()
        self.root.mainloop()

if __name__ == '__main__':
    obj=Attendance_view()
    obj.run()