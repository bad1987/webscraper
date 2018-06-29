# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worldnews.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import database, time, threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(100, 240)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title = QtGui.QLabel(Form)
        self.title.setText(_fromUtf8(""))
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout.addWidget(self.title)
        self.body = QtGui.QLabel(Form)
        self.body.setText(_fromUtf8(""))
        self.body.setObjectName(_fromUtf8("body"))
        self.verticalLayout.addWidget(self.body)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.website = QtGui.QLabel(Form)
        self.website.setText(_fromUtf8(""))
        self.website.setObjectName(_fromUtf8("website"))
        self.horizontalLayout.addWidget(self.website)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        thread = threading.Thread(target=self.display, daemon=True)
        thread.start()

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def display(self):
        db = database.Scraperdatabase()

        while True:
            for content in db.retreivedata():
                self.title.setText(_fromUtf8(content[0]))
                self.body.setText(_fromUtf8(content[1]))
                self.website.setText(_fromUtf8(content[2]))

                time.sleep(20)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

