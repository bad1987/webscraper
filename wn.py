# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wn.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import time, threading, database


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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(486, 306)
        MainWindow.setMinimumSize(QtCore.QSize(471, 283))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/cto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:0.618182 rgba(128, 128, 128, 255), stop:0.968182 rgba(146, 146, 146, 255), stop:0.990909 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 7, 211, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sky = QtGui.QPushButton(self.layoutWidget)
        self.sky.setStyleSheet(_fromUtf8("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(170, 170, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));"))
        self.sky.setObjectName(_fromUtf8("sky"))
        self.horizontalLayout.addWidget(self.sky)
        self.afriquemedia = QtGui.QPushButton(self.layoutWidget)
        self.afriquemedia.setStyleSheet(_fromUtf8("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(170, 170, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));"))
        self.afriquemedia.setObjectName(_fromUtf8("afriquemedia"))
        self.horizontalLayout.addWidget(self.afriquemedia)
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(80, 90, 391, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setStyleSheet(_fromUtf8("background-color: rgb(238, 234, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 63 italic 14pt \"Ubuntu\";"))
        self.title.setWordWrap(True)
        self.title.setObjectName(_fromUtf8("title"))
        self.body = QtGui.QLabel(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(80, 170, 391, 101))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setMinimumSize(QtCore.QSize(391, 91))
        self.body.setStyleSheet(_fromUtf8("background-color: rgb(238, 234, 255);\n"
"font: 63 italic 14pt \"Ubuntu\";"))
        self.body.setFrameShadow(QtGui.QFrame.Plain)
        self.body.setText(_fromUtf8(""))
        self.body.setTextFormat(QtCore.Qt.RichText)
        self.body.setScaledContents(True)
        self.body.setWordWrap(True)
        self.body.setObjectName(_fromUtf8("body"))
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QObject.connect(self.sky, QtCore.SIGNAL('clicked()'), self.skyNews)
        QtCore.QObject.connect(self.afriquemedia, QtCore.SIGNAL('clicked()'), self.afrmediaNews)

        self.stopThread = False
        self.lock = threading.Lock()
        self.numThread = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "worldnews", None))
        self.sky.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sky</span></p></body></html>", None))
        self.sky.setText(_translate("MainWindow", "Sky", None))
        self.afriquemedia.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sky</span></p></body></html>", None))
        self.afriquemedia.setText(_translate("MainWindow", "AfriqueMedia", None))
        self.title.setText(_translate("MainWindow", "To start, push one of the buttons above", None))

    def display(self, website='sky'):
        db = database.Scraperdatabase()

        stop = False
        while True:

            res = db.retreivePerWebsiteData(website)
            if res:
                for content in res:
                    self.title.setText(_fromUtf8(str(content[0]).rstrip('\n').replace('\n', "")))
                    self.body.setText(_fromUtf8(content[1]))
                    # self.website.setText(_fromUtf8(content[2]))
                    # self.textBrowser.setText(_fromUtf8(content[0]))
                    time.sleep(10)

                    with self.lock:
                        if self.stopThread:
                            self.stopThread = False
                            self.numThread -= 1
                            if self.numThread < 0:
                                self.numThread = 0

                            stop = True

                    if stop:
                        break
                if stop:
                    break

            else:
                # print("the database is empty")
                self.title.setText(_fromUtf8('there are no news available for now'))
                self.body.setText(_fromUtf8('No content available, be patient'))

    def skyNews(self):
        # self.display('sky')

        with self.lock:
            if self.numThread != 0:
                self.stopThread = True
            self.numThread += 1

        thread = threading.Thread(target=self.display, args=('sky',), daemon=True)
        thread.start()

    def afrmediaNews(self):
        # self.display('afriquemedia')

        with self.lock:
            if self.numThread != 0:
                self.stopThread = True
            self.numThread += 1

        thread = threading.Thread(target=self.display, args=('afriquemedia',), daemon=True)
        thread.start()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

