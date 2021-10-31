from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from caldesign import Ui_SimpleCalculator

READY = 0
INPUT = 1

class SimpleCalculator(QMainWindow, Ui_SimpleCalculator):
    def __init__(self, *args, **kwargs):
        super(SimpleCalculator, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pb%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        # Setup operations.
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))

        self.pb10.pressed.connect(self.decimal)

        self.pushButton_eq.pressed.connect(self.equals)

        # Setup actions
        self.pushButton_ce.pressed.connect(self.resetce)
        self.pushButton_ac.pressed.connect(self.reset)

        self.pushButton_m.pressed.connect(self.memory_store)
        self.pushButton_mr.pressed.connect(self.memory_recall)

        self.memory = 0
        self.memory_before = 0
        self.reset()

        self.show()

# cannot do the decimal yet
    def decimal(self):
        # self.stack[-1] = f'{self.stack[-1]}{"."}'
        # self.state = INPUT
        # self.display()
        pass

    def display(self):
        self.lcdNumber.display(self.stack[-1])

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()
    
    def resetce(self):
        # CE: clear entry - restore the number before press equal
        self.state = INPUT
        self.stack = [0]
        self.stack[-1] = self.memory_before
        self.display()

    def memory_store(self):
        self.memory = self.lcdNumber.value()

    def memory_recall(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def operation(self, op):
        if self.current_op:
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op
        self.memory_before = self.lcdNumber.value()

    def equals(self):
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            self.stack = [self.current_op(*self.stack)]
            self.current_op = None
            self.state = READY
            self.display()

        self.memory_before = self.lcdNumber.value()

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("PyQt Calculator")

    window = SimpleCalculator()
    app.exec_()
