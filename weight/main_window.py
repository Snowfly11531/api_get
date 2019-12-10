import sys
from PyQt5 import *
from weight.main_window_ui import *
from weight.parameter_frame import *
class Main_Window(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(QtWidgets.QWidget,self).__init__()
        self.frameHeight=0
        self.frameCount=0
        self.setupUi(self)
    def addframe(self):
        test_frame = Parameter_Frame(self.scrollAreaWidgetContents)
        self.frameHeight = test_frame.geometry().height()
        top=self.frameHeight*self.frameCount
        test_frame.setGeometry(QtCore.QRect(0, top, test_frame.geometry().width(), test_frame.geometry().height()))
        self.scrollAreaWidgetContents.setMinimumHeight(top+self.frameHeight+10)
        test_frame.show()
        self.frameCount += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())