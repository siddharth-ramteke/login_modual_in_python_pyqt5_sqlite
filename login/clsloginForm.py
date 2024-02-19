from PyQt5.QtWidgets import QMainWindow,QMessageBox

import DB
from login.loginForm import Ui_MainWindow
from Main_Form.clsMainForm import clsMainForm





class clsloginForm(QMainWindow):
    def __init__(self):
        super(clsloginForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Main=clsMainForm()
        self.ui.btnLogin.clicked.connect(self.logincheck)
        self.db=DB.DB()

        self.ui.ltxtUserName.setText("vinit")
        self.ui.ltxtPassword.setText("april")

    def logincheck(self):
        user=self.ui.ltxtUserName.text()
        password=self.ui.ltxtPassword.text()
        if self.db.check_duplicate("UserName",user,"AddUser","")!=0 and self.db.check_duplicate("Password",password,"AddUser","")!=0:
            self.Main.show()
            self.close()
        else:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("UserName or Password is ot correct")
            msg.setWindowTitle("Error")
            retval=msg.exec_()




