"""Calculator PYQT5"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimpleCalculator(object):
    def setupUi(self, SimpleCalculator):
        SimpleCalculator.setObjectName("SimpleCalculator")
        SimpleCalculator.setFixedSize(301, 423)
        SimpleCalculator.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(SimpleCalculator)
        self.centralwidget.setObjectName("centralwidget")
        SimpleCalculator.setStyleSheet("background-color: rgb(135,206,234);")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(30, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setAutoFillBackground(False)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setLineWidth(1)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.outputLabel.setStyleSheet("background-color: white")
        self.p7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.p7.setGeometry(QtCore.QRect(30, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p7.setFont(font)
        self.p7.setObjectName("p7")
        self.p7.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.p8.setGeometry(QtCore.QRect(90, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p8.setFont(font)
        self.p8.setObjectName("p8")
        self.p8.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.p9.setGeometry(QtCore.QRect(150, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p9.setFont(font)
        self.p9.setObjectName("p9")
        self.p9.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pslash = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.pslash.setGeometry(QtCore.QRect(220, 90, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pslash.setFont(font)
        self.pslash.setObjectName("pslash")
        self.pslash.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pmul = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.pmul.setGeometry(QtCore.QRect(220, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pmul.setFont(font)
        self.pmul.setObjectName("pmul")
        self.pmul.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pminus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.pminus.setGeometry(QtCore.QRect(220, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pminus.setFont(font)
        self.pminus.setObjectName("pminus")
        self.pminus.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pplus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.pplus.setGeometry(QtCore.QRect(220, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pplus.setFont(font)
        self.pplus.setObjectName("pplus")
        self.pplus.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pclear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C"))
        self.pclear.setGeometry(QtCore.QRect(152, 330, 121, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pclear.setFont(font)
        self.pclear.setObjectName("pclear")
        self.pclear.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.p4.setGeometry(QtCore.QRect(30, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p4.setFont(font)
        self.p4.setObjectName("p4")
        self.p4.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.p5.setGeometry(QtCore.QRect(90, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p5.setFont(font)
        self.p5.setObjectName("p5")
        self.p5.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.p6.setGeometry(QtCore.QRect(150, 150, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p6.setFont(font)
        self.p6.setObjectName("p6")
        self.p6.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.p2.setGeometry(QtCore.QRect(90, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p2.setFont(font)
        self.p2.setObjectName("p2")
        self.p2.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.p1.setGeometry(QtCore.QRect(30, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p1.setFont(font)
        self.p1.setObjectName("p1")
        self.p1.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.p3.setGeometry(QtCore.QRect(150, 210, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p3.setFont(font)
        self.p3.setObjectName("p3")
        self.p3.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.p0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.p0.setGeometry(QtCore.QRect(90, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.p0.setFont(font)
        self.p0.setObjectName("p0")
        self.p0.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pequal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
        self.pequal.setGeometry(QtCore.QRect(30, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pequal.setFont(font)
        self.pequal.setObjectName("pequal")
        self.pequal.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pdot = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.pdot.setGeometry(QtCore.QRect(150, 270, 53, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pdot.setFont(font)
        self.pdot.setObjectName("pdot")
        self.pdot.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        self.pclearentry = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_ce())
        self.pclearentry.setGeometry(QtCore.QRect(30, 330, 111, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pclearentry.setFont(font)
        self.pclearentry.setObjectName("pclearentry")
        self.pclearentry.setStyleSheet("QPushButton"
                    "{"
                    "background-color : #e6e6e6;"
                    "}"
                    "QPushButton::hover"
                    "{"
                    "border :2px solid ;"
                    "border-color : #418abb; "
                    "}")
        SimpleCalculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SimpleCalculator)
        self.statusbar.setObjectName("statusbar")
        SimpleCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(SimpleCalculator)
        QtCore.QMetaObject.connectSlotsByName(SimpleCalculator)

    # operation
    def math_it(self):
        screen = self.outputLabel.text()
        try:    
            # math
            answer = eval(screen)
            # output answer
            if answer - int(answer) == 0:
                self.outputLabel.setText(str(answer))
            else:
                answer = round(answer, 10)
                self.outputLabel.setText(str(answer))
        except:
            # output ERROR
            self.outputLabel.setText("ERROR")

    # remove entry CE
    def remove_ce(self):
        screen = self.outputLabel.text()
        # remove the last set of number
        if "+" in screen or "-" in screen or "*" in screen or "/" in screen:
            while True:
                if screen[-1] in ("+", "-", "/", "*"):
                    if screen[-1] in ("+", "-"):
                        screen += "0"
                    elif screen[-1] in ("/", "*"):
                        screen += "1"
                    break
                screen = screen[:-1]
        self.outputLabel.setText(screen)

    # add decimal
    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed, operator=0):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # check if it start with 0, if so remove
            if self.outputLabel.text() == "0":
                 self.outputLabel.setText("")
            # add number after the one berfore
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, SimpleCalculator):
        _translate = QtCore.QCoreApplication.translate
        SimpleCalculator.setWindowTitle(_translate("SimpleCalculator", "Simple Calculator"))
        self.outputLabel.setText(_translate("SimpleCalculator", "0"))
        self.p7.setText(_translate("SimpleCalculator", "7"))
        self.p8.setText(_translate("SimpleCalculator", "8"))
        self.p9.setText(_translate("SimpleCalculator", "9"))
        self.pslash.setText(_translate("SimpleCalculator", "/"))
        self.pmul.setText(_translate("SimpleCalculator", "*"))
        self.pminus.setText(_translate("SimpleCalculator", "-"))
        self.pplus.setText(_translate("SimpleCalculator", "+"))
        self.pclear.setText(_translate("SimpleCalculator", "C"))
        self.p4.setText(_translate("SimpleCalculator", "4"))
        self.p5.setText(_translate("SimpleCalculator", "5"))
        self.p6.setText(_translate("SimpleCalculator", "6"))
        self.p2.setText(_translate("SimpleCalculator", "2"))
        self.p1.setText(_translate("SimpleCalculator", "1"))
        self.p3.setText(_translate("SimpleCalculator", "3"))
        self.p0.setText(_translate("SimpleCalculator", "0"))
        self.pequal.setText(_translate("SimpleCalculator", "="))
        self.pdot.setText(_translate("SimpleCalculator", "."))
        self.pclearentry.setText(_translate("SimpleCalculator", "CE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimpleCalculator = QtWidgets.QMainWindow()
    ui = Ui_SimpleCalculator()
    ui.setupUi(SimpleCalculator)
    SimpleCalculator.show()
    sys.exit(app.exec_())
