import os
import logging

from PyQt5 import QtCore, QtWidgets

log = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self, config):
        super().__init__()
        self.config = config

        # self.set_menu_bar()
        self.set_toolbar()
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        # self.showMaximized()
        # self.statusBar()
        # self.statusBar().showMessage('Ready')

    # def set_menu_bar(self):
    #     menu_bar = self.menuBar()
    #     menu = menu_bar.addMenu('File')
    #     action = menu.addAction('&Exit')
    #     action.setShortcut('Ctrl+Q')
    #     action.setStatusTip('Exit application')
    #     action.triggered.connect(QtWidgets.qApp.quit)

    def set_toolbar(self):
        toolbar = QtWidgets.QToolBar()
        toolbar.setMovable(False)
        for i in ('F2 rename', 'F5 copy', 'F6 move', 'F7 mkdir', 'F8 remove', 'F9 term', 'F10 exit'):
            w = QtWidgets.QWidget()
            w.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            toolbar.addWidget(w)
            a = toolbar.addAction(i)
            t = i.split(' ', 1)[0]
            a.setShortcut(t)
            a.triggered.connect(getattr(self, 'on_' + t.lower()))
        w = QtWidgets.QWidget()
        w.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        toolbar.addWidget(w)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, toolbar)

        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        # layout = QGridLayout(central_widget)
        # layout.setHorizontalSpacing(0)
        # layout.setContentsMargins(0, 0, 0, 0)
        #
        # model = TableModel()
        # view = QTableView()
        # view.setModel(model)
        #
        # view.setColumnWidth(0, 200)
        #
        # view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # vv = view.verticalHeader()
        # vv.setSectionResizeMode(QHeaderView.Fixed)
        # vv.setDefaultSectionSize(20)
        # vh = view.horizontalHeader()
        # vh.setStretchLastSection(True)
        #
        # layout.addWidget(view, 0, 0)
        # layout.addWidget(self.Search_Bar, 0, 1)

        #
        # text = QLabel('fdgfhgfd')
        # # w = QTabWidget()
        # # w.addTab(text)
        # # self.setCentralWidget(w)
        # # self.setCentralWidget(text)
        #

        # layout = QVBoxLayout()
        # layout.addWidget(view)
        # self.setLayout(layout)

    def on_f2(self):
        print('F2')

    def on_f5(self):
        print('F5')

    def on_f6(self):
        print('F6')

    def on_f7(self):
        print('F7')

    def on_f8(self):
        print('F8')

    def on_f9(self):
        """F9 term"""
        cmd = '{} {}'.format(self.config['main']['term'], '/')  # todo
        log.debug('%s', cmd)
        os.system(cmd)

    @staticmethod
    def on_f10():
        """F10 exit"""
        QtWidgets.qApp.quit()
