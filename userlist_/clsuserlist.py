from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from userlist_.userlist import Ui_MainWindow
from DB import DB

class clsuserlist(QMainWindow): 
	def __init__(self):
		super(clsuserlist, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.db=DB()
		self.ui.tableWidget.setColumnCount(2)
		self.ui.tableWidget.setHorizontalHeaderLabels(["User Name","User Type"])
		self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(150)
		self.loadd()

	def loadd(self):
		cur=self.db.runSelect("select * from AddUser")
		rows=cur.fetchall()
		for row in rows:
			self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)
			rw=self.ui.tableWidget.rowCount()
			self.ui.tableWidget.setItem(rw - 1 ,0, QTableWidgetItem(str(row[1])))
			self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[2])))




