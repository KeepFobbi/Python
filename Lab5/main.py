from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyCalculator import Ui_Dialog

# Create application 
app = QtWidgets.QApplication(sys.argv)
    
# Create form and init UI
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook logic
def bp(key):
    calcEntry = ui.textEdit.toPlainText()
    ui.textEdit.setText(calcEntry + key)
    if key == "=":
        try:
            result = eval(calcEntry.replace("=", ""))
            ui.textEdit.setText(str(result))
        except:
            ui.textEdit.setText("Error!")
    elif key == "C":
        ui.textEdit.clear()

ui.pushButton_3.clicked.connect(lambda: bp("0"))
ui.pushButton_8.clicked.connect(lambda: bp("1"))
ui.pushButton_7.clicked.connect(lambda: bp("2"))
ui.pushButton_6.clicked.connect(lambda: bp("3"))
ui.pushButton_12.clicked.connect(lambda: bp("4"))
ui.pushButton_11.clicked.connect(lambda: bp("5"))
ui.pushButton_10.clicked.connect(lambda: bp("6"))
ui.pushButton_16.clicked.connect(lambda: bp("7"))
ui.pushButton_15.clicked.connect(lambda: bp("8"))
ui.pushButton_14.clicked.connect(lambda: bp("9"))
ui.pushButton_9.clicked.connect(lambda: bp("+"))
ui.pushButton_13.clicked.connect(lambda: bp("-"))
ui.pushButton_23.clicked.connect(lambda: bp("*"))
ui.pushButton_24.clicked.connect(lambda: bp("/"))
ui.pushButton_2.clicked.connect(lambda: bp("="))
ui.pushButton_34.clicked.connect(lambda: bp("C"))
ui.pushButton_21.clicked.connect(lambda: bp("("))
ui.pushButton_22.clicked.connect(lambda: bp(")"))
# Run main loop
sys.exit(app.exec_())