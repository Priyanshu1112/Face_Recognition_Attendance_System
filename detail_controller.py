import traceback


class Details:
    def __init__(self, s_no=None, s_name=None, s_section=None, img=None):
        try:
            self.s_eno=s_no.upper()
            self.s_name=s_name.title()
            self.s_section=s_section.upper()
            self.img=img
        except AttributeError:
            print('from detail controller:',traceback.format_exc())

    def set_eno(self, eno):
        self.s_eno = eno.upper()

    def set_name(self, s_name):
        self.s_name = s_name.title()

    def set_section(self, section):
        self.s_section = section.upper()

    def get_eno(self):
        return self.s_eno

    def get_name(self):
        return self.s_name

    def get_section(self):
        return self.s_section

    def get_image(self):
        return self.img

