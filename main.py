import sys

from PyQt5.QtWidgets import QApplication, QWidget


class MainWidget(QWidget):

    def __init__(self):
        # 调用父类的初始化方法
        super().__init__()
        # 完成对本widget的初始化操作
        self.__init_ui()

    def __init_ui(self):
        self.resize(780, 400)
        self.setWindowTitle('抖音下载器(无水印)')

        # 显示在屏幕上
        self.show()


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。
    # sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # 创建一个要现实的窗口
    main_widget = MainWidget()

    # 系统exit()方法确保应用程序干净的退出，
    # exec_()方法有下划线 因为exec是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
