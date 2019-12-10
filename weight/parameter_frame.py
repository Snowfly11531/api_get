import sys
from PyQt5 import *
from weight.parameter_frame_ui import *
class Test_Frame(QtWidgets.QFrame,Ui_Frame):
    def __init__(self,parent=None):
        super(QtWidgets.QFrame,self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    test_frame=Test_Frame()
    test_frame.show()
    sys.exit(app.exec_())