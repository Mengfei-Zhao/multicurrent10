import sys
from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import uic
from Ui_subWin_infoOfConnection import Ui_infoOfConnection


class SubWin_InfoOfConnection(QWidget, Ui_infoOfConnection):
    def __init__(self):
        super().__init__()
        # uic.loadUi('subWin_infoOfConnection.ui', self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SubWin_InfoOfConnection()
    demo.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
