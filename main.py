import configparser
import logging

# from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtWidgets
from gui import MainWindow

__version__ = '0.1'

log = logging.getLogger(__name__)
config = configparser.ConfigParser()


class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setApplicationName('FManager ' + __version__)
        # if 'palette' in config:
        #     palette = QPalette()
        #     palette.setColor(QPalette.Window, QColor(config['palette'].get('window', '#fff')))
        #     palette.setColor(QPalette.WindowText, QColor(config['palette'].get('window_text', '#000')))
        #     self.setPalette(palette)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    config.read('config.ini')

    app = Application([])
    window = MainWindow()
    window.show()
    app.exec_()
