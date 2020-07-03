import os
import sys
import  PySide2.QtCore
from  PySide2.QtWidgets import QApplication, QWidget

# Prints PySide2 version
# e.g. 5.11.1a1
print(PySide2.__version__)

if __name__ == '__main__':

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 0)
    w.setWindowTitle('example 1')
    w.show()

    sys.exit(app.exec_())