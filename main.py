"""
Приложение
"""
import configparser
import logging

from PyQt5 import QtWidgets, QtGui
from gui import MainWindow
from utils import lower2

__version__ = '0.1'

log = logging.getLogger(__name__)
config = configparser.ConfigParser()


class Application(QtWidgets.QApplication):
    """Приложение на Qt"""

    def __init__(self, config: configparser.ConfigParser, argv: list):
        super().__init__(argv)
        self.config = config
        self.setApplicationName('FManager ' + __version__)
        self.set_palette()

    def set_palette(self):
        """Применить тему из конфига"""
        if 'palette' not in self.config:
            return
        palette = QtGui.QPalette()
        for name, color in self.config['palette'].items():
            name = lower2(name)
            try:
                pal = getattr(QtGui.QPalette, name)
                palette.setColor(pal, QtGui.QColor(color))
            except Exception as ex:
                log.debug('%s = %s', name, color)
                log.exception(ex)
        self.setPalette(palette)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        config.read('config.ini')
    except Exception as ex:
        log.exception(ex)
        # todo write config

    app = Application(config, [])
    window = MainWindow(config)
    window.show()
    app.exec_()
