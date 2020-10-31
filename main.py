import configparser
import logging

from PyQt5 import QtWidgets, QtGui
from gui import MainWindow
from utils import lower2

__version__ = '0.1'

log = logging.getLogger(__name__)
config = configparser.ConfigParser()


class Application(QtWidgets.QApplication):
    def __init__(self, config: configparser.ConfigParser, argv: list):
        super().__init__(argv)
        self.config = config
        self.setApplicationName('FManager ' + __version__)
        self.set_palette()

    def set_palette(self):
        if 'palette' not in self.config:
            return
        palette = QtGui.QPalette()
        for k, v in self.config['palette'].items():
            k = lower2(k)
            try:
                p = getattr(QtGui.QPalette, k)
                palette.setColor(p, QtGui.QColor(v))
            except Exception as e:
                log.debug('%s = %s', k, v)
                log.exception(e)
        self.setPalette(palette)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        config.read('config.ini')
    except Exception as e:
        log.exception(e)
        # todo write config

    app = Application(config, [])
    window = MainWindow(config)
    window.show()
    app.exec_()
