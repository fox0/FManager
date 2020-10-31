"""
Графический интерфейс: главное окно и прочее
"""
import configparser
import os
import logging
import shlex
import subprocess

from PyQt5 import QtCore, QtWidgets

from models import TableModel

log = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self, config: configparser.ConfigParser):
        super().__init__()
        self.config = config

        self.set_menubar()
        self.set_toolbar()
        self.set_central_widget()
        if self.config['main'].getboolean('show_statusbar'):
            self.statusBar()
        self.setMinimumSize(800, 600)
        # self.showMaximized()

    def _log(self, value: str):
        """Вывести сообщение в статус-бар"""
        if self.config['main'].getboolean('show_statusbar'):
            self.statusBar().showMessage(value)

    def set_menubar(self):
        """Добавить меню-бар"""
        if not self.config['main'].getboolean('show_menubar'):
            return
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu('File')
        action = menu.addAction('&Exit')
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Exit application')
        action.triggered.connect(QtWidgets.qApp.quit)

    def set_toolbar(self):
        """Добавить тулбар с кнопками"""
        if not self.config['main'].getboolean('show_toolbar'):
            return
        toolbar = QtWidgets.QToolBar()
        toolbar.setMovable(False)
        for i in ('F2 rename', 'F5 copy', 'F6 move', 'F7 mkdir', 'F8 remove', 'F9 term', 'F10 exit'):
            widget = QtWidgets.QWidget()
            widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            toolbar.addWidget(widget)
            action = toolbar.addAction(i)
            attr = i.split(' ', 1)[0]
            action.setShortcut(attr)
            action.triggered.connect(getattr(self, 'on_' + attr.lower()))
        widget = QtWidgets.QWidget()
        widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        toolbar.addWidget(widget)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, toolbar)

    def set_central_widget(self):
        """Отрисовать остальное содержимое окна"""
        central_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        view = QtWidgets.QTableView()
        view.setModel(TableModel())  # todo!

        view.setColumnWidth(0, 200)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        vv = view.verticalHeader()
        vv.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        vv.setDefaultSectionSize(20)
        vh = view.horizontalHeader()
        vh.setStretchLastSection(True)

        main_layout.addWidget(view, stretch=True)
        main_layout.addWidget(QtWidgets.QLabel('fdgfhgfd'), stretch=True)

        # # w = QTabWidget()
        # # w.addTab(text)
        self.setCentralWidget(central_widget)

    def on_f2(self):
        """F2 rename"""
        log.debug('on_f2')

    def on_f5(self):
        """F5 copy"""
        log.debug('on_f5')

    def on_f6(self):
        """F6 move"""
        log.debug('on_f6')

    def on_f7(self):
        """F7 mkdir"""
        log.debug('on_f7')

    def on_f8(self):
        """F8 remove"""
        log.debug('on_f8')

    def on_f9(self):
        """F9 term"""
        log.debug('on_f9')
        try:
            args = shlex.split(self.config['main']['term'])
            args.append('/')  # todo
            log.debug('%s', args)
            subprocess.Popen(args)
        except Exception as ex:
            self._log(f'{ex.__class__.__name__}: {ex}')
            log.exception(ex)

    @staticmethod
    def on_f10():
        """F10 exit"""
        log.debug('on_f10')
        QtWidgets.qApp.quit()
