from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from Main_Form.MainForm import Ui_MainWindow
from UserOptions.clsAddUser import  clsAddUser
from userlist_.clsuserlist import clsuserlist
from BlockUser_.clsBlockUser import clsBlockUser


class clsMainForm(QMainWindow):
    def __init__(self):
        super(clsMainForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setCentralWidget(self.ui.mdiArea)
        self.ui.actionAdd_New_User.triggered.connect(self.actAddUser)
        self.ui.actionList_All_User.triggered.connect(self.actList)
        self.ui.actionBlock_User.triggered.connect(self.actblock)

    def actAddUser(self):
        self.Add=clsAddUser()
        self.ui.mdiArea.addSubWindow(self.Add)
        self.Add.show()
    def actList(self):
        self.List=clsuserlist()
        self.ui.mdiArea.addSubWindow(self.List)
        self.List.show()
    def actblock(self):
        self.block=clsBlockUser()
        self.ui.mdiArea.addSubWindow(self.block)
        self.block.show()

