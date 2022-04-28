import db_model

class Db_controller:
    def __init__(self):
        self.dbm_obj=db_model.Db_model()

    def get_db_status(self):
        return self.dbm_obj.get_db_status()

    def add_student_to_db(self, de_obj):
        return self.dbm_obj.add_student_to_db(de_obj)

    def add_image(self, img_name, img):
        return self.dbm_obj.add_image(img_name, img)

    def get_name(self, eno):
        return self.dbm_obj.get_name(eno)

    def get_section(self, eno):
        return self.dbm_obj.get_section(eno)

    def get_path(self):
        return self.dbm_obj.get_path()

    def set_path(self, path):
        return self.dbm_obj.set_path(path)

    def get_start_time(self):
        return self.dbm_obj.get_start_time()

    def get_end_time(self):
        return self.dbm_obj.get_end_time()

    def check_attendance(self, eno):
        return self.dbm_obj.check_attendance(eno)

    def mark_student_present(self, eno):
        return self.dbm_obj.mark_student_present(eno)

    def update_student(self, de_obj):
        return self.dbm_obj.update_student(de_obj)

    def update_image(self, img_name, img):
        return self.dbm_obj.update_image(img_name, img)

    def load_students_from_db(self):
        return self.dbm_obj.load_students_from_db()

    def get_all_eno(self):
        return self.dbm_obj.get_all_eno()

    def change_eno(self, eno, alt_eno):
        return self.dbm_obj.change_eno(eno, alt_eno)

    def change_eno_registered(self, eno, alt_eno1, alt_eno2):
        return self.dbm_obj.change_eno_registered(eno, alt_eno1, alt_eno2)

    def remove_student(self, eno):
        return self.dbm_obj.remove_student(eno)

    def mark_holiday(self, holiday, date):
        return self.dbm_obj.mark_holiday(holiday, date)

    def update_holiday(self, holiday, date):
        return self.dbm_obj.update_holiday(holiday, date)

    def not_marked_students(self):
        return self.dbm_obj.not_marked_students()

    def mark_rest_absent(self):
        return self.dbm_obj.mark_rest_absent()

    def update_time(self, start_time, end_time):
        return self.dbm_obj.update_time(start_time, end_time)

    def get_image_eno(self):
        return self.dbm_obj.get_image_eno()

    def restore_images(self, eno):
        return self.dbm_obj.restore_images(eno)