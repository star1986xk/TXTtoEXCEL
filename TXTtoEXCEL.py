# -*-coding: UTF-8 -*-
import sys

import chardet
from PyQt5.QtWidgets import QApplication, QFrame, QFileDialog, QMessageBox
from UI.UI_win import Ui_Form
from PyQt5.QtCore import Qt
import openpyxl


class MainWindow(QFrame, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_txt.clicked.connect(self.open_file)
        self.pushButton_export.clicked.connect(self.out_excel)
        self.file_path_list = []

    # 得到选择文件的路径list
    def open_file(self):
        try:
            self.file_path_list, _ = QFileDialog.getOpenFileNames(self, '选择文件', '', 'txt files(*.txt;)')
            self.lineEdit_path.setText(','.join(self.file_path_list))
        except Exception as e:
            print(e)

    # 检测编码格式，读取内容
    def read(self, path):
        with open(path, 'rb') as f:
            text = f.read()
        encode = chardet.detect(text).get('encoding')
        with open(path, 'r', encoding=encode) as f:
            text_list = f.read().split('\n')
        return text_list

    # 创造指定行、列的索引数组
    def create_index(self, index_str: str) -> list:
        if index_str:
            result = list(map(lambda x: x.split('-'), index_str.split(',')))
            return [n for i in result for n in range(int(i[0]), int(i[-1]) + 1)]
        return []

    # 导出excel主逻辑
    def out_excel(self):
        # 未导入txt 退出
        if not self.file_path_list: return

        # 选择保存文件
        file_path, _ = QFileDialog.getSaveFileName(self, '选择保存路径', './', 'xlsx(*.xlsx)')

        # 未选择保存文件 退出
        if not file_path: return

        # 确定指定行、列
        row_list = self.create_index(self.lineEdit_row.text())
        column_list = self.create_index(self.lineEdit_column.text())

        # 生成数据
        datas = []
        for file in self.file_path_list:
            text_list = self.read(file)
            row_data_list = [text_list[r] for r in row_list] if row_list else text_list
            datas += [[float(r.split(',')[c]) for c in column_list] if column_list else [float(c) for c in r.split(',')]
                      for r in row_data_list]

        # 没有数据退出
        if not datas: return

        # 保存数据
        wb = openpyxl.Workbook()
        ws = wb.active
        for data in datas: ws.append(data)
        wb.save(file_path)

        QMessageBox.information(self, '提示', '导出成功!')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
