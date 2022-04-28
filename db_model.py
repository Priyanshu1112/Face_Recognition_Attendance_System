import cx_Oracle
import traceback
import detail_controller
import datetime
import time

class Db_model:
    def __init__(self):
        self.conn=None
        self.cur=None
        self.db_status=True
        self.date = datetime.date.today()
        self.date = str(self.date)
        self.date = datetime.datetime.strptime(self.date, '%Y-%m-%d')
        self.date = self.date.strftime('%d-%b-%Y')
        self.date = self.date.upper()
        self.student_dict = {}
        try:
            self.conn=cx_Oracle.connect('facerecognition/facerecognition@127.0.0.1/xe')
            print('Connected successfully to the DB')
            self.cur=self.conn.cursor()
        except:
            self.db_status=False
            print('DB Error:', traceback.format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.conn.close()
        if self.conn.close():
            self.conn.close()
        print("Disconnected from db")

    def load_students_from_db(self):
        self.cur.execute("select * from students where e_no not like 'HOLIDAY_%' order by e_no")
        students_present = False
        self.student_dict = {}
        for e_no, name, section in self.cur:
            self.student_dict[e_no] = (name, section)
            students_present = True
        if students_present:
            return 'Students populated from db'
        else:
            return 'No students present'

    def add_student_to_db(self, de_obj):
        self.de_obj=de_obj
        try:
            self.cur.execute('insert into students values(:1, :2, :3)',(self.de_obj.get_eno(), self.de_obj.get_name(), self.de_obj.get_section()))
            self.conn.commit()
            return 'Student added succesfully'
        except cx_Oracle.IntegrityError:
            return 'Student already present'

    def add_image(self,image_name, image):
        '''print('add image called of db model')
        print('from db model ',image)'''
        with open(image, 'rb') as file:
            blob_image=file.read()
        self.cur.execute('insert into student_images values(:1, :2)',(image_name, blob_image))
        self.conn.commit()
        return 'Image added to db'

    def get_all_eno(self):
        return self.student_dict.keys()

    def get_name(self, eno):
        return self.student_dict[eno][0]

    def get_section(self, eno):
        return self.student_dict[eno][1]

    def get_path(self):
        self.cur.execute('select path from infos')
        return self.cur.fetchone()[0]

    def set_path(self, path):
        self.cur.execute(f"insert into infos (path) values('{path}')")
        self.conn.commit()
        return 'Path set succesfully'

    def get_start_time(self):
        self.cur.execute(f"select to_char(start_time, 'HH24:MI:SS') from infos")
        return self.cur.fetchone()[0]

    def get_end_time(self):
        self.cur.execute(f"select to_char(end_time, 'HH24:MI:SS') from infos")
        return self.cur.fetchone()[0]

    def check_attendance(self, eno):

        self.cur.execute(f"select present from attendance where date_ = '{self.date}' and e_no = '{eno}'")
        try:
            res = self.cur.fetchone()[0]
            return res
        except:
            return 'None'

    def mark_student_present(self, eno):
        self.cur.execute(f"insert into attendance values('{eno}', 'Y', '{self.date}', to_date('{time.strftime('%H:%M:%S')}', 'HH24:MI:SS'))")
        self.conn.commit()
        return 'Student marked present'

    def update_student(self, de_obj):
        try:
            #print(de_obj.get_eno(), de_obj.get_name(), de_obj.get_section())
            query = f"update students set name = '{de_obj.get_name()}', section = '{de_obj.get_section()}' where e_no='{de_obj.get_eno()}'"
            #print(query)
            self.cur.execute(query)
            self.conn.commit()
            self.student_dict[de_obj.get_eno()] = (de_obj.get_name(), de_obj.get_section())
            return 'Student updated successfully'
        except:
            print(traceback.format_exc())
            return 'Error Occured'

    def update_image(self, img_name, img):
        try:
            with open(img, 'rb') as file:
                blob_image = file.read()
            #query = f"update student_images set image = {blob_image} where e_no = {img_name}"
            self.cur.execute("update student_images set image = :1 where e_no = :2",{'1' : blob_image, '2' : img_name})
            self.conn.commit()
            return 'Image updated'
        except:
            print(traceback.format_exc())
            return 'Not updated'

    def change_eno(self, eno, alt_eno):
        try:
            name, section = self.student_dict[eno]
            self.cur.execute(f"insert into students values('{alt_eno}', '{name}', '{section}')")
            self.cur.execute(f"update attendance set e_no = '{alt_eno}' where e_no = '{eno}'")
            self.cur.execute(f"update student_images set e_no = '{alt_eno}' where e_no = '{eno}'")
            self.cur.execute(f"delete from students where e_no='{eno}'")
            self.conn.commit()
            self.load_students_from_db()
            return 'Successful'
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def change_eno_registered(self, eno, alt_eno1, alt_eno2):
        try:
            name, section = self.student_dict[eno]
            name1, section1 = self.student_dict[alt_eno1]
            self.cur.execute(f"insert into students values('{alt_eno2}', '{name1}', '{section1}')")
            self.cur.execute(f"update attendance set e_no = '{alt_eno2}' where e_no = '{alt_eno1}'")
            self.cur.execute(f"update student_images set e_no = '{alt_eno2}' where e_no = '{alt_eno1}'")
            self.cur.execute(f"delete from students where e_no='{alt_eno1}'")
            self.cur.execute(f"insert into students values('{alt_eno1}', '{name}', '{section}')")
            self.cur.execute(f"update attendance set e_no = '{alt_eno1}' where e_no = '{eno}'")
            self.cur.execute(f"update student_images set e_no = '{alt_eno1}' where e_no = '{eno}'")
            self.cur.execute(f"delete from students where e_no='{eno}'")
            self.conn.commit()
            self.load_students_from_db()
            return 'Successful'
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def remove_student(self, eno):
        try:
            self.cur.execute(f"delete from students where e_no = '{eno}'")
            self.conn.commit()
            self.load_students_from_db()
            return 'Successfull'
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def mark_holiday(self, holiday, date):
        holiday = 'HOLIDAY_'+holiday+'_'+date
        print(holiday)
        try:
            if self.check_holiday(holiday) != '':
                return 'Already'
            self.cur.execute(f"select e_no from attendance where e_no like '%{date}'")
            try:
                if self.cur.fetchone()[0] != None:
                    #print('here')
                    return 'Already marked'
            except:
                pass
            self.cur.execute(f"select e_no from attendance where date_ = '{date}'")
            try:
                if self.cur.fetchone()[0] != None:
                    return 'Student marked'
            except:
                pass
            #print(f"insert into students (e_no) values('{holiday}')")
            #print(holiday)
            #self.cur.execute(f"insert into students (e_no) values('{holiday}')")
            self.cur.execute(f"insert into attendance (e_no, date_) values('{holiday}', '{date}')")
            self.conn.commit()
            return 'Successful'
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def check_holiday(self, holiday):
        try:
            self.cur.execute(f"insert into students (e_no) values('{holiday}')")
            return ''
        except cx_Oracle.IntegrityError:
            print(traceback.format_exc())
            return 'Already'

    def update_holiday(self, holiday, date):
        try:
            holiday = 'HOLIDAY_' + holiday + '_' +date
            self.cur.execute(f"delete from students where e_no like '%{date}'")
            self.cur.execute(f"insert into students (e_no) values('{holiday}')")
            self.cur.execute(f"insert into attendance (e_no, date_) values('{holiday}', '{date}')")
            self.conn.commit()
            return 'Successful'
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def not_marked_students(self):
        try:
            self.absent_students = []
            self.cur.execute(f"select e_no from students where e_no not in (select e_no from attendance where date_ = '{self.date}' and e_no not like 'HOLIDAY%') and e_no not like 'HOLIDAY%' order by e_no")
            for f in self.cur:
                self.absent_students.append(f[0])
            return self.cur.rowcount
        except:
            print(traceback.format_exc())
            return 'Unsuccessful'

    def mark_rest_absent(self):
        for eno in self.absent_students:
            #print(eno)
            self.cur.execute(
                f"insert into attendance values('{eno}', 'N', '{self.date}', to_date('{time.strftime('%H:%M:%S')}', 'HH24:MI:SS'))")
        self.conn.commit()
        return 'Students marked absent'

    def update_time(self, start_time, end_time):
        self.cur.execute(f"update infos set start_time = to_date('{start_time}', 'HH24:MI:SS')")
        self.cur.execute(f"update infos set end_time = to_date('{end_time}', 'HH24:MI:SS')")
        self.conn.commit()
        return 'Success'

    def get_image_eno(self):
        self.cur.execute('select e_no from student_images')
        eno = []
        for x in self.cur:
            eno.append(x[0])
        return eno

    def restore_images(self, eno):
        #print('db model restore image called')
        eno = list(eno)
        for x in eno:
            self.cur.execute(f"select image from student_images where e_no = '{x}'")
            image = self.cur.fetchone()
            with open(self.get_path()+'/'+x+'.jpg', 'wb') as file:
                #print(self.get_path()+'/'+x+'.jpg')
                file.write(image[0].read())
        return True