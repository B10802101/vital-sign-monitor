search_string = ':/images/'
replace_string = 'images/'
directory = './Views/staff_main_window.py'
with open(directory, 'r', encoding='utf-8') as f:
    content = f.read()
if search_string in content:
    content = content.replace(search_string, replace_string)
    with open(directory, 'w', encoding='utf-8') as f:
        f.write(content)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
from Views.staff_main_window import *
from Views.staff_login_window_manual import *
import images_rc
import os
   
class PyQt_MVC_Main(QWidget):
    def __init__(self, parent=None):
        super(PyQt_MVC_Main, self).__init__(parent)
        self.ui = Ui_staff_main_window()
        self.ui.setupUi(self)
        self.setWindowTitle('staff_main_window')
        self.linkEvent()
        self.show()
    def linkEvent(self):
        self.ui.main_screen_button_manual.clicked.connect(self.show_staff_login_manual)
    
    @pyqtSlot()
    def show_staff_login_manual(self):
        self.main_window = QMainWindow()
        ui_staff_login = Ui_staff_login_window_manual()
        ui_staff_login.setupUi(self.main_window)
        self.main_window.setWindowTitle('staff_login_window_manual')
        self.main_window.show()
        self.main_window.showFullScreen()
        self.hide()
        

















def main():
    app = QtWidgets.QApplication(sys.argv)
    main = PyQt_MVC_Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()