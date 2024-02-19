from PyQt5.QtWidgets import QMainWindow 
from BlockUser_.BlockUser import Ui_MainWindow
from DB import DB
class clsBlockUser(QMainWindow): 
	def __init__(self):
		super(clsBlockUser, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btnBlock.clicked.connect(self.blockbtnclick)
		self.db=DB()
		self.ui.cmbUser.clear()
		cur = self.db.runSelect("select * from AddUser where UserType='Local User'")
		rows = cur.fetchall()
		for row in rows:
			self.ui.cmbUser.addItem(str(row[1]))
	def blockbtnclick(self):
		userdelete=self.ui.cmbUser.currentText()
		username=self.ui.txtUserName.text()
		password=self.ui.ltxtPassword.text()


