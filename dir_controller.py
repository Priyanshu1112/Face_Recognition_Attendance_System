import db_controller
from tkinter import filedialog, messagebox
import cv2 as cv
import os

class Dir_controller:
    def __init__(self):
        self.defaulth_path=''
        self.get_set_path()
        self.img_path=self.default_path

    def get_set_path(self):
        self.dbc_obj=db_controller.Db_controller()
        try:
            self.default_path=self.dbc_obj.get_path()
        except TypeError:
                path=filedialog.askdirectory(title='Select folder')
                self.dbc_obj.set_path(path)
                self.default_path=path

    def get_path(self):
        return self.default_path

    def save_img(self, x, y, w, h, img, img_name):
        self.img_path=self.default_path+'/'+img_name.upper()+'.jpg'
        res=cv.imwrite(self.img_path, img[y:y+h+30, x:x+w+30])
        return res

    def get_img_path(self):
        return self.img_path

    def delete_image(self, img_name):
        os.remove(self.default_path+'/'.img_name.upper()+'.jpg')
        return 'Removed'
