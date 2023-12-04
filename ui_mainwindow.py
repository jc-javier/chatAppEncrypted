# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(3, 71, 103);")
        self.actionQQuit = QAction(MainWindow)
        self.actionQQuit.setObjectName(u"actionQQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username_lineedit = QLineEdit(self.centralwidget)
        self.username_lineedit.setObjectName(u"username_lineedit")
        self.username_lineedit.setMinimumSize(QSize(120, 30))
        self.username_lineedit.setMaximumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(11)
        self.username_lineedit.setFont(font)
        self.username_lineedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.username_lineedit)

        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setEnabled(True)
        self.connect_button.setMinimumSize(QSize(110, 30))
        self.connect_button.setMaximumSize(QSize(110, 16777215))
        self.connect_button.setFont(font)
        self.connect_button.setStyleSheet(u"background-color: rgb(137, 204, 255);")
        self.connect_button.setFlat(False)

        self.horizontalLayout_2.addWidget(self.connect_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.chat_listwidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.chat_listwidget)
        self.chat_listwidget.setObjectName(u"chat_listwidget")
        self.chat_listwidget.setMinimumSize(QSize(480, 382))
        self.chat_listwidget.setMaximumSize(QSize(480, 382))
        font1 = QFont()
        font1.setPointSize(12)
        self.chat_listwidget.setFont(font1)
        self.chat_listwidget.setFocusPolicy(Qt.NoFocus)
        self.chat_listwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.chat_listwidget.setFrameShape(QFrame.NoFrame)
        self.chat_listwidget.setFrameShadow(QFrame.Raised)
        self.chat_listwidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.chat_listwidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chat_listwidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.chat_listwidget.setAutoScroll(True)
        self.chat_listwidget.setAutoScrollMargin(20)
        self.chat_listwidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chat_listwidget.setAlternatingRowColors(True)
        self.chat_listwidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.chat_listwidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.chat_listwidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chat_listwidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chat_listwidget.setMovement(QListView.Static)
        self.chat_listwidget.setProperty("isWrapping", False)
        self.chat_listwidget.setResizeMode(QListView.Adjust)
        self.chat_listwidget.setUniformItemSizes(False)
        self.chat_listwidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.chat_listwidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.message_lineedit = QLineEdit(self.centralwidget)
        self.message_lineedit.setObjectName(u"message_lineedit")
        self.message_lineedit.setEnabled(True)
        self.message_lineedit.setMinimumSize(QSize(0, 30))
        self.message_lineedit.setFont(font)
        self.message_lineedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.message_lineedit.setMaxLength(240)

        self.horizontalLayout.addWidget(self.message_lineedit)

        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMinimumSize(QSize(0, 30))
        self.send_button.setFont(font)
        self.send_button.setStyleSheet(u"background-color: rgb(137, 204, 255);")

        self.horizontalLayout.addWidget(self.send_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        self.menubar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(229, 229, 229);\n"
"selection-color: rgb(0, 0, 0);")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionQQuit)

        self.retranslateUi(MainWindow)

        self.chat_listwidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat App", None))
        self.actionQQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.username_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))

        __sortingEnabled = self.chat_listwidget.isSortingEnabled()
        self.chat_listwidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.chat_listwidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Please enter a username and click connect...", None));
        self.chat_listwidget.setSortingEnabled(__sortingEnabled)

        self.message_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here... (max 240 char.)", None))
#if QT_CONFIG(tooltip)
        self.send_button.setToolTip(QCoreApplication.translate("MainWindow", u"Click or Enter", None))
#endif // QT_CONFIG(tooltip)
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

