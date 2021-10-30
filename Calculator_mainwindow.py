"""Calculator PYQT5"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimpleCalculator(object):
    def setupUi(self, SimpleCalculator):
        SimpleCalculator.setObjectName("SimpleCalculator")
        SimpleCalculator.setFixedSize(301, 423)
        SimpleCalculator.setAutoFillBackground(False)
        # self.centralWidget = QtWidgets.QWidget(SimpleCalculator)
        # self.centralWidget.setObjectName("centralWidget")
        SimpleCalculator.setStyleSheet("background-color: rgb(135,206,234);")
        # self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.centralWidget = QtWidgets.QWidget(SimpleCalculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("background-color: white")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        

        self.pb7 = QtWidgets.QPushButton(self.centralWidget)
        self.pb7.setGeometry(QtCore.QRect(30, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb7.setFont(font)
        self.pb7.setObjectName("pb7")
        self.pb7.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb8 = QtWidgets.QPushButton(self.centralWidget)
        self.pb8.setGeometry(QtCore.QRect(90, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb8.setFont(font)
        self.pb8.setObjectName("pb8")
        self.pb8.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb9 = QtWidgets.QPushButton(self.centralWidget)
        self.pb9.setGeometry(QtCore.QRect(150, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb9.setFont(font)
        self.pb9.setObjectName("pb9")
        self.pb9.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_div = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_div.setGeometry(QtCore.QRect(220, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_div.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(220, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_mul.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(220, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_sub.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_add = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_add.setGeometry(QtCore.QRect(220, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_ac = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ac.setGeometry(QtCore.QRect(152, 330, 121, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_ac.setFont(font)
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.pushButton_ac.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb4 = QtWidgets.QPushButton(self.centralWidget)
        self.pb4.setGeometry(QtCore.QRect(30, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb4.setFont(font)
        self.pb4.setObjectName("pb4")
        self.pb4.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb5 = QtWidgets.QPushButton(self.centralWidget)
        self.pb5.setGeometry(QtCore.QRect(90, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb5.setFont(font)
        self.pb5.setObjectName("pb5")
        self.pb5.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb6 = QtWidgets.QPushButton(self.centralWidget)
        self.pb6.setGeometry(QtCore.QRect(150, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb6.setFont(font)
        self.pb6.setObjectName("pb6")
        self.pb6.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb2 = QtWidgets.QPushButton(self.centralWidget)
        self.pb2.setGeometry(QtCore.QRect(90, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb2.setFont(font)
        self.pb2.setObjectName("pb2")
        self.pb2.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb1 = QtWidgets.QPushButton(self.centralWidget)
        self.pb1.setGeometry(QtCore.QRect(30, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb1.setFont(font)
        self.pb1.setObjectName("pb1")
        self.pb1.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb3 = QtWidgets.QPushButton(self.centralWidget)
        self.pb3.setGeometry(QtCore.QRect(150, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb3.setFont(font)
        self.pb3.setObjectName("pb3")
        self.pb3.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb0 = QtWidgets.QPushButton(self.centralWidget)
        self.pb0.setGeometry(QtCore.QRect(90, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb0.setFont(font)
        self.pb0.setObjectName("pb0")
        self.pb0.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_eq = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_eq.setGeometry(QtCore.QRect(30, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.pushButton_eq.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pb10 = QtWidgets.QPushButton(self.centralWidget)
        self.pb10.setGeometry(QtCore.QRect(150, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pb10.setFont(font)
        self.pb10.setObjectName("pb10")
        self.pb10.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pushButton_ce = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ce.setGeometry(QtCore.QRect(30, 330, 111, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pushButton_ce.setFont(font)
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.pushButton_ce.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")

        self.pushButton_mr = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mr.setGeometry(QtCore.QRect(310, 380, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setKerning(True)
        self.pushButton_mr.setFont(font)
        self.pushButton_mr.setObjectName("pushButton_mr")
        self.pushButton_m = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_m.setGeometry(QtCore.QRect(310, 360, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setKerning(True)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setObjectName("pushButton_m")

        SimpleCalculator.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(SimpleCalculator)
        self.statusbar.setObjectName("statusbar")
        SimpleCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(SimpleCalculator)
        QtCore.QMetaObject.connectSlotsByName(SimpleCalculator)

    def retranslateUi(self, SimpleCalculator):
        _translate = QtCore.QCoreApplication.translate
        SimpleCalculator.setWindowTitle(_translate("SimpleCalculator", "Simple Calculator"))
        self.pb4.setText(_translate("MainWindow", "4"))
        self.pb4.setShortcut(_translate("MainWindow", "4"))
        self.pb1.setText(_translate("MainWindow", "1"))
        self.pb1.setShortcut(_translate("MainWindow", "1"))
        self.pb8.setText(_translate("MainWindow", "8"))
        self.pb8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_mul.setText(_translate("MainWindow", "*"))
        self.pushButton_mul.setShortcut(_translate("MainWindow", "*"))
        self.pb7.setText(_translate("MainWindow", "7"))
        self.pb7.setShortcut(_translate("MainWindow", "7"))
        self.pb6.setText(_translate("MainWindow", "6"))
        self.pb6.setShortcut(_translate("MainWindow", "6"))
        self.pb5.setText(_translate("MainWindow", "5"))
        self.pb5.setShortcut(_translate("MainWindow", "5"))
        self.pb0.setText(_translate("MainWindow", "0"))
        self.pb0.setShortcut(_translate("MainWindow", "0"))
        self.pb2.setText(_translate("MainWindow", "2"))
        self.pb2.setShortcut(_translate("MainWindow", "2"))
        self.pb9.setText(_translate("MainWindow", "9"))
        self.pb9.setShortcut(_translate("MainWindow", "9"))
        self.pb3.setText(_translate("MainWindow", "3"))
        self.pb3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_div.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_sub.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_add.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_eq.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_ac.setText(_translate("MainWindow", "C"))
        self.pushButton_ac.setShortcut(_translate("MainWindow", "Esc"))
        self.pb10.setText(_translate("SimpleCalculator", "."))
        self.pushButton_ce.setText(_translate("SimpleCalculator", "CE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimpleCalculator = QtWidgets.QMainWindow()
    ui = Ui_SimpleCalculator()
    ui.setupUi(SimpleCalculator)
    SimpleCalculator.show()
    sys.exit(app.exec_())
