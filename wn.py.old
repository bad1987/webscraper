# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wn.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import time, threading, database
from PyQt4 import QtCore, QtGui


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
        MainWindow.resize(471, 283)
        MainWindow.setMinimumSize(QtCore.QSize(471, 283))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/cto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(170, 85, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 70, 211, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setStyleSheet(_fromUtf8("background-color: rgb(238, 234, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);\n"
"font: 63 italic 14pt \"Ubuntu\";"))
        self.title.setText(_fromUtf8("To start, push one of the buttons above"))
        self.title.setWordWrap(True)
        self.title.setObjectName(_fromUtf8("title"))
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
        self.body = QtGui.QLabel(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(20, 140, 391, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet(_fromUtf8("background-color: rgb(238, 234, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);\n"
"font: 63 italic 14pt \"Ubuntu\";"))
        self.body.setText(_fromUtf8(""))
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


    def display(self, website='sky'):
        db = database.Scraperdatabase()

        stop = False
        while True:

            res = db.retreivePerWebsiteData(website)
            if res:
                for content in res:
                    self.title.setText(_fromUtf8(str(content[0]).rstrip('\n').replace('\n',"")))
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

