import configparser
import os
import logging
import shlex
import subprocess

from PyQt5 import QtCore, QtWidgets

log = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self, config: configparser.ConfigParser):
        super().__init__()
        self.config = config

        self.set_menubar()
        self.set_toolbar()
        if self.config['main'].getboolean('show_statusbar'):
            self.statusBar()

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        # self.showMaximized()
        # self.statusBar().showMessage('Ready')

    def _log(self, value: str):
        if self.config['main'].getboolean('show_statusbar'):
            self.statusBar().showMessage(value)

    def set_menubar(self):
        if not self.config['main'].getboolean('show_menubar'):
            return
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu('File')
        action = menu.addAction('&Exit')
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Exit application')
        action.triggered.connect(QtWidgets.qApp.quit)

    def set_toolbar(self):
        if not self.config['main'].getboolean('show_toolbar'):
            return
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
        log.debug('on_f2')

    def on_f5(self):
        log.debug('on_f5')

    def on_f6(self):
        log.debug('on_f6')

    def on_f7(self):
        log.debug('on_f7')

    def on_f8(self):
        log.debug('on_f8')

    def on_f9(self):
        """F9 term"""
        log.debug('on_f9')
        try:
            args = shlex.split(self.config['main']['term'])
            args.append('/')  # todo
            log.debug('%s', args)
            subprocess.Popen(args)
        except Exception as e:
            self._log(f'{e.__class__.__name__}: {e}')
            log.exception(e)

    @staticmethod
    def on_f10():
        """F10 exit"""
        log.debug('on_f10')
        QtWidgets.qApp.quit()
