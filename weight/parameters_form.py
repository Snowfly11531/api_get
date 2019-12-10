import sys
from PyQt5 import *
from weight.parameters_form_ui import Ui_Form
from weight.parameter_frame import *
class Parameters_Window(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(QtWidgets.QWidget,self).__init__()
        self.frameHeight=0
        self.frameCount=1
        self.setupUi(self)
    def addframe(self):
        test_frame = Test_Frame(self)
        print(self.verticalLayout_3.count())
        self.verticalLayout_3.addWidget(test_frame)
        self.frameHeight = test_frame.geometry().height()+self.verticalLayout_3.spacing()
        top=self.frameHeight*self.frameCount
        self.scrollAreaWidgetContents.setMaximumHeight(top+20)
        self.scrollAreaWidgetContents.setMinimumHeight(top+20)
        test_frame.show()
        self.frameCount += 1
    def ensure(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Parameters_Window()
    main_window.show()
    sys.exit(app.exec_())