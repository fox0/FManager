from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self):
        super().__init__()
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

        action = toolbar.addAction('F2 rename')
        action.setShortcut('F2')
        action.triggered.connect(self.on_f2)

        action = toolbar.addAction('F5 copy')
        action.setShortcut('F5')
        action.triggered.connect(self.on_f5)

        action = toolbar.addAction('F6 move')
        action.setShortcut('F6')
        action.triggered.connect(self.on_f6)

        action = toolbar.addAction('F7 mkdir')
        action.setShortcut('F7')
        action.triggered.connect(self.on_f7)

        action = toolbar.addAction('F8 remove')
        action.setShortcut('F8')
        action.triggered.connect(self.on_f8)

        action = toolbar.addAction('F9 term')
        action.setShortcut('F9')
        action.triggered.connect(self.on_f9)

        action = toolbar.addAction('F10 exit')
        action.setShortcut('F10')
        action.triggered.connect(QtWidgets.qApp.quit)

        self.addToolBar(QtCore.Qt.BottomToolBarArea, toolbar)

        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        #
        # self.Search_Bar = QLineEdit("Search")
        # self.Button = QPushButton('button')
        #
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
        print('F9')
