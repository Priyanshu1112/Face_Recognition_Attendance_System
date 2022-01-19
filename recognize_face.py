import face_recognition
import os
import cv2 as cv
import numpy as np
import traceback
from PIL import Image, ImageTk
import tkinter as tk
import time
import db_controller

class Recognize_face:
    def __init__(self, root, root_splash, lbl_camera, entry_name, pb):
        self.message=''
        self.splash_root = root_splash
        self.pb = pb
    #getting set folder
        try:
            self.default_path=''
            self.pb['value'] += 4
            self.splash_root.update()
            if self.get_folder()=='No folder set':
                self.message+= 'No folder set'
        except :
            print(traceback.format_exc())
            self.message+='Recognize face get_folder() error, '
    #loading images with eno
        self.known_images_encodings = []
        self.known_eno = []
        try:
            self.load_images()
            self.pb['value'] += 4
            self.splash_root.update()
        except:
            print(traceback.format_exc())
            #self.message+= 'Error in loading images, '
    #creating Db controller obj
        try:
            self.dbc_obj=db_controller.Db_controller()
            if self.dbc_obj.get_db_status():
                self.dbc_obj.load_students_from_db()
            else:
                self.message+='Cannot connect to db'
            self.pb['value'] += 4
            self.splash_root.update()
        except:
            print(traceback.format_exc())
            self.message+= 'Error in dbc_obj, '

    #setting camera and variables
        self.cap=cv.VideoCapture(0)
        self.cap.set(3, 640)  #width
        self.cap.set(4, 480)  #height
        self.cap.set(10, 100) #brightness
        self.attendance_view_root = root
        self.lbl_camera = lbl_camera
        self.entry_name=entry_name
        self.process_this_frame=True
    #creating time label
        self.lbl_time=tk.Label(self.attendance_view_root)
        self.lbl_time.place(relx=0.68, rely=0.92, height=36, width=252)
        self.lbl_time.configure(background='#d3ebd7')
        self.lbl_time.configure(font='-family {Segoe Ui} -size 9 -weight bold')
        self.pb['value'] += 4
        self.splash_root.update()

        self.run_loop = True

    def get_message(self):
        return self.message

    def get_folder(self):
        self.dbc_obj = db_controller.Db_controller()
        try:
            self.default_path = self.dbc_obj.get_path()
        except TypeError:
            return 'No folder set'

    def load_images(self):
        known_images = []
        image_paths = [os.path.join(self.default_path, f) for f in os.listdir(self.default_path)]
        if image_paths == []:
            return 'Set folder empty'
        for f in image_paths:
            known_images.append(face_recognition.load_image_file(f))
            self.known_eno.append(os.path.splitext(os.path.basename(f))[0])
        for f in known_images:
            self.known_images_encodings.append(face_recognition.face_encodings(f)[0])

    def open_camera(self):
        run_time = 0
        while self.run_loop:
            self.update_time()
            img = self.cap.read()[1]
            img = cv.flip(img, 1)

            if run_time == 0:
                self.attendance_view_root.deiconify()
                self.splash_root.withdraw()
                run_time = 1

            if self.process_this_frame:
                eno = 'UNKNOWN'
                face_locations = face_recognition.face_locations(img)
                face_encodings = face_recognition.face_encodings(img, face_locations)

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_images_encodings, face_encoding, tolerance=0.6)
                    face_distances = face_recognition.face_distance(self.known_images_encodings, face_encoding)
                    best_match_index=np.argmin(face_distances)
                    if matches[best_match_index]:
                        eno=self.known_eno[best_match_index]
                self.eno = eno
            self.process_this_frame = not self.process_this_frame

            for(top, right, bottom, left) in face_locations:
                cv.rectangle(img, (left, top + 10), (right, bottom + 10), (0, 255, 0), 2)
                cv.rectangle(img, (left, bottom + 10), (right, bottom + 40), (0, 255, 0), cv.FILLED)
                font = cv.FONT_HERSHEY_DUPLEX
                cv.putText(img, eno, (left + 6, bottom + 25), font, 0.6, (255, 255, 255), 1)
            try:
                if eno.isalnum():
                    name=self.dbc_obj.get_name(eno)
            except KeyError:
                name = ''
                print(traceback.format_exc())
            self.entry_name.configure(state='normal')
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_name.configure(state='disabled')
            print(eno+'-'+name)

            img=cv.cvtColor(img, cv.COLOR_RGB2BGR)
            img=ImageTk.PhotoImage(Image.fromarray(img))
            self.lbl_camera['image'] = img
            self.attendance_view_root.update()

    def close_camera(self):
        self.run_loop = False

    def release(self):
        self.cap.release()

    def get_eno(self):
        return self.eno

    def update_time(self):
        self.lbl_time.configure(text='Time:-'+time.strftime('%H:%M:%S'))