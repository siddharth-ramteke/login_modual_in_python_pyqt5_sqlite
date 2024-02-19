from PyQt5.QtWidgets import QMainWindow 
from admissionForm import Ui_MainWindow 
class clsadmissionForm(QMainWindow): 
	def __init__(self):
		super(clsadmissionForm, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
