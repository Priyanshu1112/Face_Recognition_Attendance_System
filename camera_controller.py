import cv2 as cv
from PIL import Image, ImageTk
import tkinter as tk
import time

class Camera:
    def __init__(self, root, root_splash, lbl_camera):
        self.register_view_root=root
        self.register_view_root.withdraw()
        self.cap = cv.VideoCapture(0)
        self.cap.set(3, 640)  # width
        self.cap.set(4, 480)  # height
        self.cap.set(10, 100)  # brightness
        self.splash_root = root_splash
        self.lbl_camera=lbl_camera
        self.run=True
        self.recognizer=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.x=0
        self.y=0
        self.w=0
        self.h=0
    #creating time label
        self.lbl_time = tk.Label(self.register_view_root)
        self.lbl_time.place(relx=0.660, rely=0.900, height=36, width=252)
        self.lbl_time.configure(background="#d3ebd7")
        self.lbl_time.configure(font="-family {Segoe UI} -size 9 -weight bold")

    def open_camera(self):
        run_time = 0
        while True:
            if run_time == 0:
                self.register_view_root.deiconify()
                self.splash_root.withdraw()
                run_time = 1
            self.update_time()
            img = self.cap.read()[1]
            if self.run:
                #print('Open Camera Called')
                img = cv.flip(img, 1)
                self.img = img
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                face=self.recognizer.detectMultiScale(img, 1.1, 15)
                for (x, y, w, h) in face:
                    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    self.x, self.y, self.w, self.h = x, y, w, h
                self.p_img = ImageTk.PhotoImage(Image.fromarray(img))
                self.lbl_camera['image'] = self.p_img
                self.register_view_root.update()

    def update_time(self):
        self.lbl_time.configure(text='Time:-'+time.strftime('%H:%M:%S'))

    def cap_release(self):
        self.cap.release()

    def stop_camera(self):
        self.run=False

    def capture(self):
        print('Capture Called')
        self.lbl_camera.pack_forget()
        return (self.x, self.y, self.w, self.h), self.img, self.p_img

    def capture_again(self):
        print('Capture again called')
        self.lbl_camera.pack()

    def root_destroy(self):
        self.root.destroy()