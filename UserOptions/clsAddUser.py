from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UserOptions.AddUser import Ui_MainWindow
from DB import DB


class clsAddUser(QMainWindow):
    def __init__(self):
        super(clsAddUser, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=DB()

        self.ui.btnSave.clicked.connect(self.savebtnclick)

    def savebtnclick(self):
        username=self.ui.ltxtName.text()
        usertype=self.ui.comboBox.currentText()
        password=self.ui.ltxtPassword.text()
        if self.db.check_duplicate("UserName",username,"AddUser","")==0:
            if self.ui.ltxtPassword.text()==self.ui.ltxtPassword2.text():
                sql = "insert into AddUser values(null,'" + username + "','" + usertype + "','" + password + "')"
                self.db.Execute_Sql(sql)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("User Created Successfully")
                msg.setWindowTitle("Success")
                retval = msg.exec_()
            else:
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Confirmation of password is not the same as password")
                msg.setWindowTitle("Error")
                retval=msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("User Already Exists")
            msg.setWindowTitle("Error")
            retval = msg.exec_()




