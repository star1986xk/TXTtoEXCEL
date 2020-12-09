# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_win.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#widget{border-image: url(:/newPrefix/1.jpg);}\n"
"QPushButton{\n"
"background-color: rgb(220, 220, 220,200);\n"
"border-style:none;border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color: rgb(200, 200, 200,120);\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180,120);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:5px;\n"
"background-color: rgb(220, 220, 220,200);\n"
"}\n"
"\n"
"/*QLabel{color: rgb(255, 255, 255);}\n"
"QLabel{font-weight: bold;}*/")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_close.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setStyleSheet("QPushButton{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(255,255,255,0);\n"
"border-style:none;\n"
"border-radius: 5px;\n"
"image:url(:/newPrefix/关闭1.png);\n"
"width:15px;height:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px 2px 2px 2px;\n"
"image:url(:/newPrefix/关闭.png);\n"
"background-color: rgb(220, 220, 220,100);\n"
"border-radius: 5px;\n"
"width:15px;height:15px;\n"
"}\n"
"QPushButton:pressed {\n"
"padding:2px 2px 2px 2px;\n"
"    image:url(:/newPrefix/关闭1.png);\n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(180, 180, 180,100);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"border-radius: 5px;\n"
"}")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_txt = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_txt.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_txt.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_txt.setFont(font)
        self.pushButton_txt.setObjectName("pushButton_txt")
        self.horizontalLayout_3.addWidget(self.pushButton_txt)
        self.lineEdit_path = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_path.setFont(font)
        self.lineEdit_path.setReadOnly(True)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_path)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_row = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_row.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_row.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_row.setFont(font)
        self.lineEdit_row.setReadOnly(False)
        self.lineEdit_row.setObjectName("lineEdit_row")
        self.horizontalLayout.addWidget(self.lineEdit_row)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_column = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_column.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_column.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_column.setFont(font)
        self.lineEdit_column.setReadOnly(False)
        self.lineEdit_column.setObjectName("lineEdit_column")
        self.horizontalLayout.addWidget(self.lineEdit_column)
        self.pushButton_export = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_export.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_export.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout.addWidget(self.pushButton_export)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "TxT导出ExceL"))
        self.pushButton_txt.setText(_translate("Form", "选择TxT"))
        self.label.setText(_translate("Form", "指定行："))
        self.label_2.setText(_translate("Form", "指定列："))
        self.pushButton_export.setText(_translate("Form", "导出结果"))
import img_rc
