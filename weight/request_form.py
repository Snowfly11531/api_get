import sys
from PyQt5 import *
from weight.request_form_ui import *
from weight.main_window import Main_Window
class Request_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(QtWidgets.QWidget,self).__init__()
        self.setupUi(self)
        self.main_window = Main_Window()
    def request(self):
        self.main_window.show()
        #self.close()
    def get_url_parameters(self):
        pass
    def get_headers_parameters(self):
        pass
    def get_body_parameters(self):
        pass
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    request_form = Request_Form()
    request_form.show()
    sys.exit(app.exec_())
