# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myworldnews.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(650, 400)
        Dialog.setMinimumSize(QtCore.QSize(0, 341))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(39, 40, 61);"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(150, 150, 112);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.title = QtGui.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(0, 140, 251, 171))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(36, 0))
        self.title.setSizeIncrement(QtCore.QSize(10, 10))
        self.title.setBaseSize(QtCore.QSize(241, 0))
        self.title.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);"))
        self.title.setFrameShape(QtGui.QFrame.NoFrame)
        self.title.setFrameShadow(QtGui.QFrame.Raised)
        self.title.setTextFormat(QtCore.Qt.LogText)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.title.setWordWrap(False)
        self.title.setObjectName(_fromUtf8("title"))
        self.body = QtGui.QLabel(self.frame)
        self.body.setGeometry(QtCore.QRect(300, 130, 310, 220))
        self.body.setMinimumSize(QtCore.QSize(36, 0))
        self.body.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);"))
        self.body.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.body.setObjectName(_fromUtf8("body"))
        self.apptitle = QtGui.QLabel(self.frame)
        self.apptitle.setGeometry(QtCore.QRect(10, 10, 561, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apptitle.sizePolicy().hasHeightForWidth())
        self.apptitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.apptitle.setFont(font)
        self.apptitle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.apptitle.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 152, 174);"))
        self.apptitle.setFrameShape(QtGui.QFrame.WinPanel)
        self.apptitle.setFrameShadow(QtGui.QFrame.Raised)
        self.apptitle.setLineWidth(1)
        self.apptitle.setTextFormat(QtCore.Qt.AutoText)
        self.apptitle.setScaledContents(False)
        self.apptitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.apptitle.setWordWrap(True)
        self.apptitle.setIndent(-1)
        self.apptitle.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.apptitle.setObjectName(_fromUtf8("apptitle"))
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 60, 251, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sky = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sky.sizePolicy().hasHeightForWidth())
        self.sky.setSizePolicy(sizePolicy)
        self.sky.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sky.setMouseTracking(False)
        self.sky.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sky.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.sky.setToolTip(_fromUtf8(""))
        self.sky.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sky.setAutoFillBackground(False)
        self.sky.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"font: 75 16pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);"))
        self.sky.setObjectName(_fromUtf8("sky"))
        self.horizontalLayout.addWidget(self.sky)
        self.afriquemedia = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afriquemedia.sizePolicy().hasHeightForWidth())
        self.afriquemedia.setSizePolicy(sizePolicy)
        self.afriquemedia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.afriquemedia.setFocusPolicy(QtCore.Qt.NoFocus)
        self.afriquemedia.setStyleSheet(_fromUtf8("background-color: rgb(64, 99, 255);\n"
"font: 75 16pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);"))
        self.afriquemedia.setObjectName(_fromUtf8("afriquemedia"))
        self.horizontalLayout.addWidget(self.afriquemedia)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        QtCore.QObject.connect(self.sky, QtCore.SIGNAL('clicked()'), self.skyNews)
        QtCore.QObject.connect(self.afriquemedia, QtCore.SIGNAL('clicked()'), self.afrmediaNews)

        self.stopThread = False
        self.lock = threading.Lock()
        self.numThread = 0

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "WorldNews", None))
        self.title.setText(_translate("Dialog", "title of the site ", None))
        self.body.setText(_translate("Dialog", "body", None))
        self.apptitle.setText(_translate("Dialog", "                                International News", None))
        self.sky.setText(_translate("Dialog", "sky", None))
        self.afriquemedia.setText(_translate("Dialog", "afriquemedia", None))

    def display(self, website='sky'):
        db = database.Scraperdatabase()

        stop = False
        while True:

            res = db.retreivePerWebsiteData(website)
            if res:
                for content in res:
                    self.title.setText(_fromUtf8(str(self.formater(content[0]))))
                    self.body.setText(_fromUtf8(self.formater(content[1])))
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


    def formater(self,string):
        string = str(string).strip('\n').replace('\t',"")
        res = []
        i = 0
        k = 0
        for c in str(string):

            if i == 25:
                if c != ' ':
                    j = k - 1
                    while j > 0:
                        if res[j] == ' ':
                            res[j] = '\n'
                            break
                        j -= 1
                    res.append(c)
                else:
                    res.append('\n')
                i = 0
            else:
                res.append(c)
                i += 1
            k += 1
        f = ''
        for c in res:
            f += c
        return f


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

