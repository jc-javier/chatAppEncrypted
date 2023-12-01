from PySide6.QtWidgets import QApplication
from client import ChatApp
import sys

app = QApplication(sys.argv)

window = ChatApp(app)
window.show()

app.exec()
