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


class UiChooseLevel(object):
    def setupUi(self, ChooseLevel):
        if not ChooseLevel.objectName():
            ChooseLevel.setObjectName(u"ChooseLevel")
        ChooseLevel.resize(804, 624)
        ChooseLevel.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(ChooseLevel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.level_screen = QVBoxLayout(self.centralwidget)
        self.level_screen.setObjectName(u"verticalLayout")
        self.horizontalLayout_level = QHBoxLayout()
        self.horizontalLayout_level.setSpacing(70)
        self.horizontalLayout_level.setObjectName(u"horizontalLayout")
        self.horizontalLayout_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_level.setContentsMargins(20, -1, 20, -1)

        self.buttons=[]
        for button in range(4):
                self.buttons.append(QPushButton(self.centralwidget))
                self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                                "background-color: rgb(236, 221, 11);\n"
                                                "border-radius:10px;")
                self.horizontalLayout_level.addWidget(self.buttons[button])


        self.level_screen.addLayout(self.horizontalLayout_level)

        self.horizontalLayout_2_level = QHBoxLayout()
        self.horizontalLayout_2_level.setSpacing(70)
        self.horizontalLayout_2_level.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2_level.setContentsMargins(20, -1, 20, -1)
        
        for button in range(4, 8):
                self.buttons.append(QPushButton(self.centralwidget))
                self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                                "background-color: rgb(236, 221, 11);\n"
                                                "border-radius:10px;")
                self.horizontalLayout_2_level.addWidget(self.buttons[button])

        self.level_screen.addLayout(self.horizontalLayout_2_level)

        ChooseLevel.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChooseLevel)

        QMetaObject.connectSlotsByName(ChooseLevel)
    # setupUi

    def retranslateUi(self, ChooseLevel):
        ChooseLevel.setWindowTitle(QCoreApplication.translate("ChooseLevel", u"Sokoban", None))
        for level, button in enumerate(self.buttons):
                button.setText(str(level + 1))
    # retranslateUi

