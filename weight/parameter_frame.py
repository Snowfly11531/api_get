import sys
from PyQt5 import *
from weight.parameter_frame_ui import *
class Parameter_Frame(QtWidgets.QFrame, Ui_Frame):
    def __init__(self,parent=None):
        super(QtWidgets.QFrame,self).__init__(parent)
        self.setupUi(self)

    def get_parameter(self):
        return None if self.lineEdit_2.text()=="" else{
            "key":self.lineEdit_2.text(),
            "value":self.lineEdit.text(),
            "isNowTime":self.radioButton.isChecked()
        }
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    test_frame=Parameter_Frame()
    test_frame.show()
    sys.exit(app.exec_())