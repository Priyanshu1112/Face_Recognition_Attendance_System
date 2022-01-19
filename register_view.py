import tkinter as tk
import camera_controller as cc
from tkinter import messagebox, simpledialog
import sys
import traceback
from PyQt5 import QtWidgets
import db_controller
import opening_view_tk
import detail_controller
import dir_controller

class Register_view:

    def __init__(self,main_root, root_splash, pb, lbl_status):
        self.main_root = main_root
        self.root_splash = root_splash
        self.pb = pb
        self.lbl_status = lbl_status
    #creating and designing root window
        self.lbl_status['text'] = 'Status: Loading widgets...'
        self.root_splash.update()
        self.root=tk.Toplevel()
        self.root.title('''Register Student''')
        icon=tk.PhotoImage(file='icons/register_icon .png')
        self.root.iconphoto(self.root, icon)
        self.root.geometry('900x700+280+70')
        self.root.configure(bg="#b7dfbd")
        self.pb['value'] += 5
        self.root_splash.update()
    #creating label frame
        self.lbl_frame_camera=tk.LabelFrame(self.root)
        self.lbl_frame_camera.place(relx=0.03, rely=0.047, relheight=0.651, relwidth=0.6)
        self.lbl_frame_camera.configure(text='Camera')
        self.lbl_frame_camera.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.pb['value'] += 5
        self.root_splash.update()
    #creating label
        self.lbl_camera=tk.Label(self.lbl_frame_camera)
        #self.lbl_camera.configure(text='Check')
        self.lbl_camera.pack()
    #creating label captured
        self.lbl_captured=tk.Label(self.lbl_frame_camera)
        self.pb['value'] += 5
        self.root_splash.update()
    #creating back button
        self.btn_back = tk.Button(self.root)
        self.icon = tk.PhotoImage(file='icons/back.png')
        self.btn_back.configure(image=self.icon)
        self.btn_back.configure(background="#d3ebd7")
        self.btn_back.configure(foreground="#000000")
        self.btn_back.configure(command=self.back)
        self.btn_back.place(relx=0.00, rely=0.0, relheight=0.044, relwidth=0.05)
        self.pb['value'] += 5
        self.root_splash.update()
    #creating capture button
        self.btn_capture = tk.Button(self.root)
        self.btn_capture.place(relx=0.769, rely=0.1, height=50, width=178)
        self.btn_capture.configure(background="#d3ebd7")
        self.btn_capture.configure(foreground="#000000")
        self.btn_capture.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.btn_capture.configure(takefocus="")
        self.btn_txt_variable=tk.StringVar()
        self.btn_txt_variable.set('''Capture''')
        self.btn_capture.configure(textvariable=self.btn_txt_variable)
        self.btn_capture.configure(command=self.capture)
        self.pb['value'] += 5
        self.root_splash.update()
    # creating eno label
        self.lbl_eno = tk.Label(self.root)
        self.lbl_eno.place(relx=0.03, rely=0.715, height=26, width=182)
        self.lbl_eno.configure(background="#d3ebd7")
        self.lbl_eno.configure(disabledforeground="#a3a3a3")
        self.lbl_eno.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_eno.configure(foreground="#000000")
        self.lbl_eno.configure(text='''Enrollment No:-''')
        self.pb['value'] += 5
        self.root_splash.update()
    # creating eno entry
        self.entry_eno = tk.Entry(self.root)
        self.entry_eno.place(relx=0.277, rely=0.715, height=24, relwidth=0.350)
        self.entry_eno.configure(background="white")
        self.entry_eno.configure(disabledforeground="#a3a3a3")
        self.entry_eno.configure(font="TkFixedFont")
        self.entry_eno.configure(foreground="#000000")
        self.entry_eno.configure(insertbackground="black")
        self.pb['value'] += 5
        self.root_splash.update()
    # creating name label
        self.lbl_name = tk.Label(self.root)
        self.lbl_name.place(relx=0.03, rely=0.795, height=26, width=182)
        self.lbl_name.configure(background="#d3ebd7")
        self.lbl_name.configure(disabledforeground="#a3a3a3")
        self.lbl_name.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_name.configure(foreground="#000000")
        self.lbl_name.configure(text='''Name:-''')
    # creating name entry
        self.entry_name = tk.Entry(self.root)
        self.entry_name.place(relx=0.277, rely=0.795, height=24, relwidth=0.350)
        self.entry_name.configure(background="white")
        self.entry_name.configure(disabledforeground="#a3a3a3")
        self.entry_name.configure(font="TkFixedFont")
        self.entry_name.configure(foreground="#000000")
        self.entry_name.configure(insertbackground="black")
        self.pb['value'] += 5
        self.root_splash.update()
    # creating section label
        self.lbl_section = tk.Label(self.root)
        self.lbl_section.place(relx=0.03, rely=0.875, height=26, width=183)
        self.lbl_section.configure(background="#d3ebd7")
        self.lbl_section.configure(disabledforeground="#a3a3a3")
        self.lbl_section.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.lbl_section.configure(foreground="#000000")
        self.lbl_section.configure(text='''Section:-''')
        self.pb['value'] += 5
        self.root_splash.update()
    # creating section entry
        self.entry_section = tk.Entry(self.root)
        self.entry_section.place(relx=0.277, rely=0.875, height=24, relwidth=0.350)
        self.entry_section.configure(background="white")
        self.entry_section.configure(disabledforeground="#a3a3a3")
        self.entry_section.configure(font="TkFixedFont")
        self.entry_section.configure(foreground="#000000")
        self.entry_section.configure(insertbackground="black")
        self.pb['value'] += 5
        self.root_splash.update()
    # creating register button
        self.btn_register = tk.Button(self.root)
        self.btn_register.place(relx=0.769, rely=0.25, height=50, width=178)
        self.btn_register.configure(background="#d3ebd7")
        self.btn_register.configure(foreground="#000000")
        self.btn_register.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.btn_register.configure(takefocus="")
        self.btn_register.configure(text='''Register''')
        self.btn_register.configure(command=self.register)
        self.pb['value'] += 5
        self.root_splash.update()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)

    #calling creating camera_controller object
        self.lbl_status['text'] = 'Status: Creating Cc obj ...'
        self.root_splash.update()
        try:
            #self.root.withdraw()
            self.cc_obj=cc.Camera(self.root, self.root_splash, self.lbl_camera)
            self.pb['value'] += 20
            self.root_splash.update()
        except:
            messagebox.showerror('Camera Controller Error', 'Error in cc_obj')
            print(traceback.format_exc())
            sys.exit(1)

    def open_camera(self):
        try:
            self.lbl_status['text'] = 'Status: Opening camera ...'
            self.root_splash.update()
            self.cc_obj.open_camera()
        except:
            print(traceback.format_exc())
            #sys.exit(1)

    def register(self):
        print('Register clicked')
        try:
            if self.captured():
                if self.validate():
                    self.de_obj=detail_controller.Details(self.entry_eno.get().strip(), self.entry_name.get().strip(), self.entry_section.get().strip(), self.img[self.y:self.y+self.h, self.x:self.x+self.w])
                    self.dbc_obj=db_controller.Db_controller()
                    if not self.dbc_obj.get_db_status():
                        messagebox.showerror('DB Error', 'Cannot connect to db')
                        return
                    self.di_obj = dir_controller.Dir_controller()
                    res = self.di_obj.save_img(self.x, self.y, self.w, self.h, self.img,
                                               self.entry_eno.get().strip())
                    if not res:
                        messagebox.showerror('ERROR', 'Image was not saved')
                        return
                    message = self.dbc_obj.add_student_to_db(self.de_obj)
                    if message in 'Student added succesfully':
                        res_db = self.dbc_obj.add_image(self.entry_eno.get().strip().upper(),
                                                        self.di_obj.get_img_path())
                        if res_db != 'Image added to db':
                            messagebox.showerror('ERROR', 'Could not save image in database')
                        messagebox.showinfo('SUCCESFULL',
                                            f'Student registered with E_No.:-{self.entry_eno.get().strip().upper()}')
                    elif message in 'Student already present':
                        res_up = messagebox.askyesno('Already Present',
                                             f'Student with E_No:-{self.entry_eno.get().strip().upper()} already present. Do you want to update?')
                        if res_up:
                            self.update_student()
                    self.clear()
                    self.capture()
                else:
                    messagebox.showerror('Cannot proceed', 'Fill all the fields to proceed')
            else:
                messagebox.showerror('Cannot proceed', 'Capture the image first to proceed')
        except:
            messagebox.showerror('ERROR', 'An unexpected error occured')
            print(traceback.format_exc())


    def update_student(self):
        res = self.di_obj.save_img(self.x, self.y, self.w, self.h, self.img,
                                   self.entry_eno.get().strip())
        if not res:
            messagebox.showerror('ERROR', 'Image was not saved')
            return
        message = self.dbc_obj.update_student(self.de_obj)
        if message in 'Student updated successfully':
            res_db = self.dbc_obj.update_image(self.entry_eno.get().strip().upper(),
                                               self.di_obj.get_img_path())
            if res_db != 'Image updated':
                messagebox.showerror('ERROR', 'Could not save image in database')
            messagebox.showinfo('SUCCESFULL',
                                f'Student with E_No.:-{self.entry_eno.get().strip().upper()} updated successfully')
        else:
            messagebox.showerror('UNSUCCESFULL', 'Cannot update student')

    def captured(self):
        if self.btn_txt_variable.get()=='Capture Again':
            return True
        return False

    def validate(self):
        if self.entry_eno.get().strip()=='' or self.entry_name.get().strip()=='' or self.entry_section.get().strip()=='':
            return False
        return True

    def clear(self):
        self.entry_eno.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_section.delete(0, tk.END)


    def back(self):
        self.main_root.deiconify()
        self.root.destroy()

    def capture(self):
        print('Capture clicked')
        try:
            text_variable=self.btn_txt_variable.get()
            if text_variable in 'Capture':
                self.btn_txt_variable.set('''Capture Again''')
                face, self.img, self.p_img=self.cc_obj.capture()
                self.x, self.y, self.w, self.h = face
                '''print('x='+str(self.x)+', y='+str(self.y)+', w='+str(self.w)+', h='+str(self.h))
                print(type(self.x))'''
                self.lbl_captured['image']=self.p_img
                self.lbl_captured.pack()

            elif text_variable in '''Capture Again''':
                self.btn_txt_variable.set('''Capture''')
                self.lbl_captured.pack_forget()
                self.cc_obj.capture_again()
        except:
            messagebox.showerror('ERROR', 'Unexpected error occured')
            print(traceback.format_exc())
            sys.exit(1)

    def exit(self):
        self.root.destroy()
        self.root_splash.destroy()

    def run(self):
        self.open_camera()
        self.root.mainloop()

if __name__ == '__main__':

    obj=Register_view()
    obj.run()
