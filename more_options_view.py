import datetime
import tkinter as tk
import traceback
import tkcalendar
import db_controller
import detail_controller
from tkinter import messagebox, ttk
from threading import Thread
import time
import dir_controller


class More_options_view:
    def __init__(self, root):
        self.main_root = root
    #creating and desgining root window
        self.root = tk.Toplevel()
        self.root.title(''''More Options''')
        icon = tk.PhotoImage(file='icons/more_options.png')
        self.root.iconphoto(self.root, icon)
        self.root.geometry('900x700+200+70')
        self.root.configure(bg='#b7dfbd')
    #creating label frame Student
        self.lbl_frame_student = tk.LabelFrame(self.root)
        self.lbl_frame_student.configure(text='''Manage Students''')
        self.lbl_frame_student.configure(bg='#ceefba')
    #creating update student button
        self.btn_update = tk.Button(self.lbl_frame_student)
        self.btn_update.configure(background="#d3ebd7")
        self.btn_update.configure(foreground="#000000")
        self.btn_update.configure(command=self.update_student)
    #creating change eno button
        self.btn_change_eno = tk.Button(self.lbl_frame_student)
        self.btn_change_eno.configure(background="#d3ebd7")
        self.btn_change_eno.configure(foreground="#000000")
        self.btn_change_eno.configure(command=self.change_eno)
    #creating remove student button
        self.btn_remove_student = tk.Button(self.lbl_frame_student)
        self.btn_remove_student.configure(background="#d3ebd7")
        self.btn_remove_student.configure(foreground="#000000")
        self.btn_remove_student.configure(command=self.remove_student)
    #creating label frame attendance
        self.lbl_frame_attendance = tk.LabelFrame(self.root)
        self.lbl_frame_attendance.configure(text='''Manage Attendance''')
        self.lbl_frame_attendance.configure(bg='#ceefba')
    #creating show attendance button
        self.btn_show_attendance = tk.Button(self.lbl_frame_attendance)
        self.btn_show_attendance.configure(background="#d3ebd7")
        self.btn_show_attendance.configure(foreground="#000000")
        self.btn_show_attendance.configure(command=self.show_attendance)
    #creating mark holiday button
        self.btn_mark_holiday = tk.Button(self.lbl_frame_attendance)
        self.btn_mark_holiday.configure(background="#d3ebd7")
        self.btn_mark_holiday.configure(foreground="#000000")
        self.btn_mark_holiday.configure(command=self.mark_holiday)
    #creating mark rest absent
        self.btn_mark_rest_absent = tk.Button(self.lbl_frame_attendance)
        self.btn_mark_rest_absent.configure(background="#d3ebd7")
        self.btn_mark_rest_absent.configure(foreground="#000000")
        self.btn_mark_rest_absent.configure(command=self.mark_rest_absent)
    #creating label frame more options
        self.lbl_frame_more = tk.LabelFrame(self.root)
        self.lbl_frame_more.configure(text='''More Options''')
        self.lbl_frame_more.configure(bg='#ceefba')
    # creating start time button
        self.btn_time = tk.Button(self.lbl_frame_more)
        self.btn_time.configure(background="#d3ebd7")
        self.btn_time.configure(foreground="#000000")
        self.btn_time.configure(command=self.time)
    #creating open notepad button
        self.btn_open_notepad = tk.Button(self.lbl_frame_more)
        self.btn_open_notepad.configure(background="#d3ebd7")
        self.btn_open_notepad.configure(foreground="#000000")
        self.btn_open_notepad.configure(command=self.open_notepad)
    # creating open restore button
        self.btn_restore_images = tk.Button(self.lbl_frame_more)
        self.btn_restore_images.configure(background="#d3ebd7")
        self.btn_restore_images.configure(foreground="#000000")
        self.btn_restore_images.configure(command=self.restore_images)

    #creating time label
        self.lbl_time = tk.Label(self.root)
        self.lbl_time.configure(background="#ceefba")
        self.lbl_time.configure(font="-family {Segoe UI} -size 9 -weight bold")
    #creating back button
        self.back_icon = tk.PhotoImage(file='icons/back.png')
        self.btn_back = tk.Button(self.root, image=self.back_icon, command=self.back)
    #placing all the widgets
        self.place_widgets()

    #create detailc controller obj
        self.de_obj = detail_controller.Details()

    #creatin db controller obj
        self.dbc_obj = db_controller.Db_controller()

    # declaring forgeting widgets and side variables
        self.forget_widgets_dec()
        self.entry_eno2_placed = False
        self.load_eno()

    def update_student(self):
        if self.btn_update['text'] == 'Update':
            self.forget_widgets()
            self.place_widgets()
            self.btn_update['text'] = 'Done'
            self.btn_clicked = self.btn_update
            self.change_text = 'Update'
            self.lbl_frame_student.place(relx=0.03, rely=0.047, relheight=0.2, relwidth=0.94)
            self.btn_update.place(relx=0.03, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_change_eno.place(relx=0.45, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_remove_student.place(relx=0.84, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_cancel.place(relx=0.94, rely=0.65,  relheight=0.18)
            self.entry_section.place(relx=0.8, rely=0.65, relwidth=0.1)
            self.lbl_section.place(relx=0.73, rely=0.65)
            self.entry_name.place(relx=0.42, rely=0.65, relwidth=0.26)
            self.lbl_name.place(relx=0.35, rely=0.65)
            self.lbl_eno.place(relx=0.03, rely=0.65)
            self.cb_eno.place(relx=0.15, rely=0.65)
        elif self.btn_update['text'] == 'Done':
            if self.cb_eno.get() == '':
                messagebox.showerror('ERROR', 'Please select an Eno to proceed.')
                return
            if self.entry_name.get() == '' or self.entry_section.get() == '':
                messagebox.showerror('ERROR', 'None of the entries can be blank')
                return
            #self.btn_update['text'] = 'Update'
            #self.forget_widgets()
            #self.place_widgets()
            self.de_obj.set_eno(self.cb_eno.get())
            self.de_obj.set_name(self.entry_name.get())
            self.de_obj.set_section(self.entry_section.get())
            try:
                if self.dbc_obj.update_student(self.de_obj) in 'Student updated successfully':
                    messagebox.showinfo('SUCCESSFULL', 'Student updated successfully')
                    self.clear()
                else:
                    messagebox.showinfo('UNSUCCESSGUL', 'Cannot update student')
            except:
                print(traceback.format_exc())
                messagebox.showerror('ERROR', 'Error from db in updating student')

    def change_eno(self):
        if self.btn_change_eno['text'] == 'Change E_No':
            self.forget_widgets()
            self.place_widgets()
            self.btn_change_eno['text'] = 'Done'
            self.btn_clicked = self.btn_change_eno
            self.change_text = 'Change E_no'
            self.lbl_frame_student.place(relx=0.03, rely=0.047, relheight=0.2, relwidth=0.94)
            self.btn_cancel.place(relx=0.93, rely=0.6)
            self.btn_update.place(relx=0.03, rely=0.16, relheight=0.25, relwidth=0.15)
            self.btn_change_eno.place(relx=0.45, rely=0.16, relheight=0.25, relwidth=0.15)
            self.btn_remove_student.place(relx=0.84, rely=0.16, relheight=0.25, relwidth=0.15)
            self.entry_alt_eno1.place(relx=0.38, rely=0.56, relwidth=0.25)
            self.lbl_arrow.place(relx=0.33, rely=0.56)
            self.lbl_eno.place(relx=0.03, rely=0.56)
            self.cb_eno.place(relx=0.15, rely=0.56)
        else:
            if not self.entry_eno2_placed:
                 alt_eno1 = self.entry_alt_eno1.get().upper()
                 if self.validate_for_change_eno(alt_eno1) in 'Empty':
                     messagebox.showerror('ERROR', 'None of the entries can be blank')
                     return
                 elif self.validate_for_change_eno(alt_eno1) in 'Alternate found':
                    res = messagebox.askokcancel('Alternate Eno Found', f'{alt_eno1} is registered eno. You can continue by providing alternate for {alt_eno1} or by trying new alternative for selected eno. Do you wish to continue with {alt_eno1}?')
                    if res:
                        self.entry_eno2.insert(0, alt_eno1)
                        self.entry_eno2['state'] = 'disabled'
                        self.entry_eno2.delete(0, tk.END)
                        self.entry_alt_eno2.place(relx=0.38, rely=0.77, relwidth=0.24)
                        self.lbl_arrow2.place(relx=0.33, rely=0.77)
                        self.entry_eno2.place(relx=0.15, rely=0.77, relheight=0.14, relwidth=0.168)
                        self.entry_eno2_placed = True
                 else:
                     try:
                        msg = self.dbc_obj.change_eno(self.cb_eno.get() ,self.entry_alt_eno1.get().upper())
                        if msg in 'Successful':
                            messagebox.showinfo('Successful', 'Eno changed successfully')
                            self.load_students_from_db()
                            self.cb_eno.configure(values=self.e_no)
                            self.clear()
                        else:
                            messagebox.showerror('Unsuccessful', 'Cannot change eno')
                     except:
                        print(traceback.format_exc())
                        messagebox.showerror('ERROR', 'Error from db in changing eno')
            else:
                if self.entry_alt_eno2.get() == '' or self.cb_eno.get() == '' or self.entry_alt_eno1.get() == '':
                    messagebox.showerror('ERROR', 'None of the entries can be blank')
                    return
                if self.entry_alt_eno2.get().upper() in self.e_no:
                    messagebox.showerror('Alternate Eno Found', f'{self.entry_alt_eno2.get()} already registerd. Please try another alternate eno for {self.entry_eno2.get()} to continue')
                    return
                try:
                    msg = self.dbc_obj.change_eno_registered(self.cb_eno.get(), self.entry_alt_eno1.get().upper(), self.entry_alt_eno2.get().upper())
                    if msg in 'Successful':
                        messagebox.showinfo('Successful', 'Eno changed successfully')
                        self.load_students_from_db()
                        self.cb_eno.configure(values=self.e_no)
                        self.clear()
                        self.entry_eno2.place_forget()
                        self.entry_alt_eno2.place_forget()
                        self.lbl_arrow2.place_forget()
                        self.entry_eno2_placed = False
                    else:
                        messagebox.showerror('Unsuccessful', 'Cannot change eno')
                except:
                    print(traceback.format_exc())
                    messagebox.showerror('ERROR', 'Error from db in changing eno')

    def remove_student(self):
        if self.btn_remove_student['text'] == 'Remove':
            self.forget_widgets()
            self.place_widgets()
            self.btn_remove_student['text'] = 'Done'
            self.btn_clicked = self.btn_remove_student
            self.change_text = 'Remove'
            self.clear()
            self.lbl_frame_student.place(relx=0.03, rely=0.047, relheight=0.2, relwidth=0.94)
            self.btn_update.place(relx=0.03, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_change_eno.place(relx=0.45, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_remove_student.place(relx=0.84, rely=0.25, relheight=0.25, relwidth=0.15)
            self.btn_cancel.place(relx=0.94, rely=0.65,  relheight=0.18)
            self.entry_section_r.place(relx=0.8, rely=0.65, relwidth=0.1)
            self.lbl_section.place(relx=0.73, rely=0.65)
            self.entry_name_r.place(relx=0.42, rely=0.65, relwidth=0.26)
            self.lbl_name.place(relx=0.35, rely=0.65)
            self.lbl_eno.place(relx=0.03, rely=0.65)
            self.cb_eno.place(relx=0.15, rely=0.65)
        else:
            if self.cb_eno.get() == '':
                messagebox.showerror('ERROR', 'Please select an Eno to proceed')
                return
            try:
                res = self.dbc_obj.remove_student(self.cb_eno.get())
                if res == 'Successfull':
                    try:
                        self.di_obj = dir_controller.Dir_controller()
                        self.di_obj.delete_image(self.cb_eno.get())
                    except:
                        print(traceback.format_exc())
                        messagebox.showerror('ERROR', 'Cannot delete image')
                    messagebox.showinfo('Successfull', 'Removed student successfully')
                    self.load_students_from_db()
                    self.cb_eno.configure(values=self.e_no)
                    self.clear()
                    return
                if res == 'Unsuccessful':
                    messagebox.showinfo('Unsuccessfull', 'Cannot remove student')
                    return
            except:
                print(traceback.format_exc())
                messagebox.showerror('ERROR', 'Error from db in removing student')

    def show_attendance(self):
        def sel():
            print(tab.item(tab.focus())['values'][1])

        root = tk.Toplevel()

        values = {1: ['Ayush', 'a'], 2: ['Bikram', 'b'], 3: ['Chetan', 'C']}

        tab = tk.ttk.Treeview(root, columns=(1, 2, 3), show='headings')
        tab.heading(1, text='Enrollment NO', anchor='w')
        tab.heading(2, text='Name')
        tab.heading(3, text='Section')
        for i, j in values.items():
            tab.insert('', 'end', values=(i, j[0], j[1]))
        b = tk.Button(root, text='Get', command=sel)
        b.pack()
        tab.pack()
        root.mainloop()

    def mark_holiday(self):
        def ok():
            holiday = entry_holiday.get()
            if holiday == None:
                return
            if holiday == '':
                holiday = 'HOLIDAY'
            msg = self.dbc_obj.mark_holiday(holiday, entry_date.get())
            if msg == 'Successful':
                messagebox.showinfo('Success', 'Successfully marked holiday')
            elif msg == 'Student marked':
                messagebox.showinfo('Student Marked', 'Student(s) found marked.')
            elif msg == 'Already marked':
                if messagebox.askokcancel('Already Marked',
                                          'Current Day is marked as holiday with another name. Do you want to change?'):
                    msg = self.dbc_obj.update_holiday(holiday, entry_date.get())
                    if msg == 'Successful':
                        messagebox.showinfo('Success', 'Successfully updated holiday')
                    else:
                        messagebox.showerror('Unsuccessful', 'Cannot update holiday')
            elif msg == 'Already':
                messagebox.showerror('Unsuccessful', 'Day already marked with this name')
            else:
                messagebox.showerror('Unsuccessful', 'Cannot mark holiday')
        def select_date():
            def done():
                date = convert_date(cal.get_date())
                entry_date1.config(state='normal')
                entry_date1.delete(0, tk.END)
                entry_date1.insert(0, date)
                entry_date1['state'] = 'disabled'
                #print('here')
                root1.destroy()
            root1 = tk.Toplevel(root)
            root1.geometry('300x230+450+350')
            cal = tkcalendar.Calendar(root1)
            entry_date1 = entry_date
            btn_done = tk.Button(root1, text='Done',bg='#d3ebd7', command=done)
            root1.configure(bg='#ceefba')
            cal.pack(pady=5, padx=5)
            btn_done.pack()
            root1.mainloop()
        def cancel():
            pass
        def convert_date(c_date):
            date = datetime.date.today() 
            if c_date != 'today':
                date = c_date
            date = str(date)
            if isinstance(c_date, str) and c_date != 'today':
                date = datetime.datetime.strptime(date, '%m/%d/%y')
            else:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
            date = date.strftime('%d-%b-%Y')
            date = date.upper()
            return date

        root = tk.Toplevel(self.root)
        root.title('Mark Holiday')
        root.geometry('300x150+450+350')
        root.configure(bg='#ceefba')

        current_date = convert_date('today')

        lbl_holiday = tk.Label(root, text='Provide name for holiday:-', bg='#ceefba')
        lbl_date = tk.Label(root, text='Date:-', bg='#ceefba')
        entry_holiday = tk.Entry(root)
        entry_date = tk.Entry(root)
        btn_ok = tk.Button(root, text='Ok', bg='#d3ebd7', command=ok)
        btn_date = tk.Button(root, text='Select Date', bg='#d3ebd7', command=select_date)
        btn_cancel = tk.Button(root, text='Cancel', bg='#d3ebd7', command=cancel)
        lbl_holiday.grid(row=0, column=0, pady=5)
        entry_holiday.grid(row=0, column=1, pady=5, columnspan=2)
        entry_date.insert(0, current_date)
        tk.Label(root, bg='#ceefba').grid(row=1, column=0)
        lbl_date.grid(row=2, column=0, padx=5)
        entry_date.grid(row=2, column=1, padx=5, columnspan=2)
        btn_ok.grid(row=3, column=0, sticky='w', padx=20)
        btn_date.grid(row=3, column=1, sticky='w', pady=10)
        btn_cancel.grid(row=3, column=2, sticky='w')
        entry_date['state'] = 'disabled'
        root.mainloop()

    def mark_rest_absent(self):
        try:
            not_marked = self.dbc_obj.not_marked_students()
            res = messagebox.askokcancel('Mark Absent?', f'Mark {not_marked} student(s) absent?')
            if res:
                if self.dbc_obj.mark_rest_absent() == 'Students marked absent':
                    messagebox.showinfo('Successful', 'Successfully marked remaining students absent')
        except:
            print(traceback.format_exc())
            messagebox.showerror('ERROR', 'Cannot mark students absent')

    def time(self):
        def get_divisions(t):
            division = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
            for i in range(10,t):
                division.append(str(i))
            return division

        if self.btn_time['text'] == 'Time':
            self.forget_widgets()
            self.place_widgets()
            self.btn_time['text'] = 'Done'
            self.btn_clicked = self.btn_time
            self.change_text = 'Time'
            self.clear()

            self.lbl_start_time  = tk.Label(self.lbl_frame_more, text='Start time:-', bg='#ceefba')
            self.cb_start_hr = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.cb_start_min = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.cb_start_sec = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.lbl_colon1 =  tk.Label(self.lbl_frame_more, text=':', bg='#ceefba')
            self.lbl_colon2 = tk.Label(self.lbl_frame_more, text=':', bg='#ceefba')
            self.lbl_hour1 = tk.Label(self.lbl_frame_more, text='Hour', bg='#ceefba')
            self.cb_start_hr['values'] = get_divisions(24)
            self.cb_start_min['values'] = get_divisions(60)
            self.cb_start_sec['values'] = get_divisions(60)
            self.lbl_start_time.place(relx=0.03, rely=0.65)
            self.cb_start_hr.place(relx=0.11, rely=0.65)
            self.lbl_colon1.place(relx=0.175, rely=0.65)
            self.cb_start_min.place(relx=0.185, rely=0.65)
            self.lbl_colon2.place(relx=0.25, rely=0.65)
            self.cb_start_sec.place(relx=0.263, rely=0.65)
            self.lbl_hour1.place(relx=0.328, rely=0.65)

            self.lbl_end_time = tk.Label(self.lbl_frame_more, text='End time:-', bg='#ceefba')
            self.cb_end_hr = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.cb_end_min = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.cb_end_sec = ttk.Combobox(self.lbl_frame_more, width=5, state='readonly')
            self.lbl_colon3 = tk.Label(self.lbl_frame_more, text=':', bg='#ceefba')
            self.lbl_colon4 = tk.Label(self.lbl_frame_more, text=':', bg='#ceefba')
            self.lbl_hour2 = tk.Label(self.lbl_frame_more, text='Hour', bg='#ceefba')

            self.cb_end_hr['values'] = get_divisions(24)
            self.cb_end_min['values'] = get_divisions(60)
            self.cb_end_sec['values'] = get_divisions(60)

            self.lbl_end_time.place(relx=0.4, rely=0.65)
            self.cb_end_hr.place(relx=0.48, rely=0.65)
            self.lbl_colon3.place(relx=0.545, rely=0.65)
            self.cb_end_min.place(relx=0.556, rely=0.65)
            self.lbl_colon4.place(relx=0.62, rely=0.65)
            self.cb_end_sec.place(relx=0.631, rely=0.65)
            self.lbl_hour2.place(relx=0.696, rely=0.65)

            self.btn_cancel2 = tk.Button(self.lbl_frame_more, text='''Cancel''', bg="#d3ebd7", command=self.cancel)
            self.btn_cancel2.place(relx=0.933, rely=0.65)

            time = self.load_time()
            st_hr = time[0][:2]
            st_min = time[0][3:5]
            st_sec = time[0][6:]
            end_hr = time[1][:2]
            end_min = time[1][3:5]
            end_sec = time[1][6:]

            self.cb_start_hr.set(st_hr)
            self.cb_start_min.set(st_min)
            self.cb_start_sec.set(st_sec)
            self.cb_end_hr.set(end_hr)
            self.cb_end_min.set(end_min)
            self.cb_end_sec.set(end_sec)

        else:
            start_time = self.cb_start_hr.get()+':'+self.cb_start_min.get()+':'+self.cb_start_sec.get()
            end_time = self.cb_end_hr.get()+':'+self.cb_end_min.get()+':'+self.cb_end_sec.get()
            time = self.load_time()
            if time[0] != start_time or time[1] != end_time:
               try:
                msg = self.dbc_obj.update_time(start_time, end_time)
                if msg == 'Success':
                       messagebox.showinfo('SUCCESS', 'Time update successfully')
               except:
                   print(traceback.format_exc())
                   messagebox.showerror('UnsuccessfulS', 'Cannot update time')
            else:
                messagebox.showinfo('NO Change', 'No change in time detected')

    def open_notepad(self):
        pass

    def restore_images(self):
        pass

    def validate_for_change_eno(self, alt_eno):
        if alt_eno == '' or self.cb_eno.get() == '':
            return 'Empty'
        if alt_eno in self.e_no:
            return 'Alternate found'
        return 'True'

    def cancel(self):
        if tk.messagebox.askokcancel('Cancel', 'Do you want to cancel?'):
            self.forget_widgets()
            self.place_widgets()
            self.btn_clicked['text'] = self.change_text

    def load_time(self):
        return self.dbc_obj.get_start_time(), self.dbc_obj.get_end_time()

    def load_students_from_db(self):
        if self.dbc_obj.get_db_status():
            if self.dbc_obj.load_students_from_db() in 'Students populated from db':
                self.e_no = []
                for f in self.dbc_obj.get_all_eno():
                    self.e_no.append(f)
            else:
                tk.messagebox.showerror('ERROR', 'No Student present in DB')
        else:
            tk.messagebox.showerror('DB ERROR', 'Cannot connect to db')
    
    def load_eno(self):
        self.load_students_from_db()
        self.cb_eno = ttk.Combobox(self.lbl_frame_student, values=self.e_no)
        self.cb_eno.bind("<<ComboboxSelected>>", self.display_info)
        self.cb_eno.bind("<Return>", self.display_info)

    def display_info(self, event=None):
        eno = self.cb_eno.get()
        name = self.dbc_obj.get_name(eno)
        section = self.dbc_obj.get_section(eno)
        try:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_section.delete(0, tk.END)
            self.entry_section.insert(0, section)

            self.entry_name_r.config(state='normal')
            self.entry_section_r.config(state='normal')
            self.entry_name_r.delete(0, tk.END)
            self.entry_name_r.insert(0, name)
            self.entry_section_r.delete(0, tk.END)
            self.entry_section_r.insert(0, section)
            self.entry_name_r['state'] = 'disabled'
            self.entry_section_r['state'] = 'disabled'
        except:
            pass

    def place_widgets(self):
        self.lbl_frame_student.place(relx=0.03, rely=0.049, relheight=0.2, relwidth=0.94)
        self.btn_update.configure(text='Update')
        self.btn_update.place(relx=0.03, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_change_eno.configure(text='Change E_No')
        self.btn_change_eno.place(relx=0.45, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_remove_student.configure(text='Remove')
        self.btn_remove_student.place(relx=0.84, rely=0.25, relheight=0.3, relwidth=0.15)

        self.lbl_frame_attendance.place(relx=0.03, rely=0.37, relheight=0.2, relwidth=0.94)
        self.btn_show_attendance.configure(text='Show Attendance')
        self.btn_show_attendance.place(relx=0.03, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_mark_holiday.configure(text='Mark Holiday')
        self.btn_mark_holiday.place(relx=0.45, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_mark_rest_absent.configure(text='Mark Rest Absent')
        self.btn_mark_rest_absent.place(relx=0.84, rely=0.25, relheight=0.3, relwidth=0.15)

        self.lbl_frame_more.place(relx=0.03, rely=0.68, relheight=0.2, relwidth=0.94)
        self.btn_time.configure(text='Time')
        self.btn_time.place(relx=0.03, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_open_notepad.configure(text='Open Notepad')
        self.btn_open_notepad.place(relx=0.45, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_restore_images.configure(text='Restore Images')
        self.btn_restore_images.place(relx=0.84, rely=0.25, relheight=0.3, relwidth=0.15)
        self.btn_back.place(relx=0, rely=0)

        self.lbl_time.place(relx=0.71, rely=0.948, height=32, width=252)

    def forget_widgets_dec(self):
        self.lbl_eno = tk.Label(self.lbl_frame_student, text='Enrollment No:', bg="#ceefba")
        self.lbl_name = tk.Label(self.lbl_frame_student, text='Name', bg="#ceefba")
        self.entry_name = tk.Entry(self.lbl_frame_student)
        self.lbl_section = tk.Label(self.lbl_frame_student, text='Section', bg="#ceefba")
        self.entry_section = tk.Entry(self.lbl_frame_student)
        self.btn_cancel = tk.Button(self.lbl_frame_student, text='''Cancel''', bg="#d3ebd7", command=self.cancel)

        self.lbl_arrow = tk.Label(self.lbl_frame_student, text='-->', bg='#ceefba')
        self.entry_alt_eno1 = tk.Entry(self.lbl_frame_student)
        self.lbl_arrow2 = tk.Label(self.lbl_frame_student, text='-->', bg='#ceefba')
        self.entry_eno2 = tk.Entry(self.lbl_frame_student)
        self.entry_alt_eno2 = tk.Entry(self.lbl_frame_student)

        self.entry_name_r = tk.Entry(self.lbl_frame_student, state='disabled')
        self.entry_section_r = tk.Entry(self.lbl_frame_student, state='disabled')

    def clear(self):
        self.entry_name_r.config(state='normal')
        self.entry_section_r.config(state='normal')
        self.cb_eno.set('')
        self.entry_name.delete(0, tk.END)
        self.entry_section.delete(0, tk.END)
        self.entry_eno2.delete(0, tk.END)
        self.entry_alt_eno1.delete(0, tk.END)
        self.entry_alt_eno2.delete(0, tk.END)
        self.entry_name_r.delete(0, tk.END)
        self.entry_section_r.delete(0, tk.END)
        self.entry_name_r['state'] = 'disabled'
        self.entry_section_r['state'] = 'disabled'

    def forget_widgets(self):
        try:
            self.lbl_eno.place_forget()
            self.cb_eno.place_forget()

            self.lbl_arrow.place_forget()
            self.lbl_arrow2.place_forget()
            self.entry_alt_eno1.place_forget()
            self.entry_eno2.place_forget()
            self.entry_alt_eno2.place_forget()

            self.lbl_name.place_forget()
            self.entry_name.place_forget()
            self.lbl_section.place_forget()
            self.entry_section.place_forget()

            self.entry_name_r.place_forget()
            self.entry_section_r.place_forget()

            self.lbl_start_time.place_forget()
            self.cb_start_hr.place_forget()
            self.cb_start_min.place_forget()
            self.cb_start_sec.place_forget()
            self.lbl_colon1.place_forget()
            self.lbl_colon2.place_forget()
            self.lbl_hour1.place_forget()

            self.lbl_end_time.place_forget()
            self.cb_end_hr.place_forget()
            self.cb_end_min.place_forget()
            self.cb_end_sec.place_forget()
            self.lbl_colon3.place_forget()
            self.lbl_colon4.place_forget()
            self.lbl_hour2.place_forget()


            self.btn_cancel.place_forget()
            self.btn_cancel2.place_forget()
            self.clear()
        except:
            print(traceback.format_exc())

    def back(self):
        self.main_root.deiconify()
        self.root.destroy()

    def run(self):
        try:
            time_obj = cur_time(self.lbl_time)
            time_obj.start()
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
        try:
            while self.run_thread:
                self.lbl_time.configure(text='Time:-'+time.strftime('%H:%M:%S'))
                time.sleep(1)
        except:
            print(traceback.format_exc())

    def stop(self):
        self.run_thread = False

if __name__ == '__main__':
    obj = More_options_view()
    obj.run()