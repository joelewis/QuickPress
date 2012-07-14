# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'post.ui'
#
# Created: Sat Jul 14 17:19:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtNetwork
from PyQt4 import QtSvg, QtXml
from PyKDE4 import kdecore
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(530, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BodyEdit = QtGui.QTextEdit(self.centralwidget)
        self.BodyEdit.setGeometry(QtCore.QRect(10, 20, 511, 301))
        self.BodyEdit.setMinimumSize(QtCore.QSize(0, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.BodyEdit.setFont(font)
        self.BodyEdit.setAutoFillBackground(False)
        self.BodyEdit.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.BodyEdit.setFrameShape(QtGui.QFrame.StyledPanel)
        self.BodyEdit.setFrameShadow(QtGui.QFrame.Raised)
        self.BodyEdit.setLineWidth(1)
        self.BodyEdit.setTabChangesFocus(True)
        self.BodyEdit.setObjectName(_fromUtf8("BodyEdit"))
        self.TitleEdit = QtGui.QLineEdit(self.centralwidget)
        self.TitleEdit.setGeometry(QtCore.QRect(12, 330, 411, 27))
        self.TitleEdit.setAccessibleName(_fromUtf8(""))
        self.TitleEdit.setObjectName(_fromUtf8("TitleEdit"))
        self.postbutton = KPushButton(self.centralwidget)
        self.postbutton.setGeometry(QtCore.QRect(430, 330, 91, 31))
        self.postbutton.setObjectName(_fromUtf8("postbutton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 360, 501, 17))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Wordpress Quick Post", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Content...", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyEdit.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Enter the Content of your post", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Title...", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Title...", None, QtGui.QApplication.UnicodeUTF8))
        self.postbutton.setText(QtGui.QApplication.translate("MainWindow", "Post", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "status...", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KPushButton
