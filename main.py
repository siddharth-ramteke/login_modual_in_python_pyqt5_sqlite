from PyQt5.QtWidgets import QApplication
from Main_Form.clsMainForm import clsMainForm
from login.clsloginForm import clsloginForm
import sys

app = QApplication([])
# f = clsMainForm()
# f.show()
f=clsloginForm()
f.show()
sys.exit(app.exec_())