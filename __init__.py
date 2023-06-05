from views.main import Ui_initialWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initialWindow = QtWidgets.QMainWindow()
    ui = Ui_initialWindow()
    ui.setupUi(initialWindow)
    initialWindow.show()
    sys.exit(app.exec_())