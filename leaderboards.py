from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sq
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Leaderboards")
        Dialog.resize(340, 452)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 301, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.Close_btn = QtWidgets.QPushButton(Dialog)
        self.Close_btn.setGeometry(QtCore.QRect(130, 410, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Close_btn.sizePolicy().hasHeightForWidth())
        self.Close_btn.setSizePolicy(sizePolicy)
        self.Close_btn.setObjectName("Close_btn")
        i = 1
        with sq.connect('users.sqlite3') as ldb:
            command = 'SELECT * FROM users ORDER BY highscore DESC'
            cursor = ldb.execute(command)
            for x in cursor:
                row = str(i) +'\t'+ str(x[0]) +'\t'+ str(x[1])
                self.listWidget.addItem(row)
                i += 1 


        self.retranslateUi(Dialog)
        self.Close_btn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Leaderboard"))
        self.Close_btn.setText(_translate("Dialog", "Close"))
