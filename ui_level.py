# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChooseLevel(object):
    def setupUi(self, ChooseLevel):
        if not ChooseLevel.objectName():
            ChooseLevel.setObjectName(u"ChooseLevel")
        ChooseLevel.resize(804, 624)
        ChooseLevel.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(ChooseLevel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(70)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_2")
        self.pushButton_1.setStyleSheet(u"font-size: 80px;\n"
"background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_4")
        self.pushButton_2.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton")
        self.pushButton_4.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(70)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_6")
        self.pushButton_5.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_7")
        self.pushButton_6.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_8")
        self.pushButton_7.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_5")
        self.pushButton_8.setStyleSheet(u"font-size: 80px;background-color: rgb(236, 221, 11);\n"
"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ChooseLevel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ChooseLevel)
        self.statusbar.setObjectName(u"statusbar")
        ChooseLevel.setStatusBar(self.statusbar)

        self.retranslateUi(ChooseLevel)

        QMetaObject.connectSlotsByName(ChooseLevel)
    # setupUi

    def retranslateUi(self, ChooseLevel):
        ChooseLevel.setWindowTitle(QCoreApplication.translate("ChooseLevel", u"Sokoban", None))
        self.pushButton_1.setText(QCoreApplication.translate("ChooseLevel", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("ChooseLevel", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("ChooseLevel", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("ChooseLevel", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("ChooseLevel", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("ChooseLevel", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("ChooseLevel", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("ChooseLevel", u"8", None))
    # retranslateUi

