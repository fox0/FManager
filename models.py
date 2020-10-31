"""
Модели для отрисовки данных в таблице
"""
import os
import logging

from PyQt5 import QtCore

log = logging.getLogger(__name__)


class TableModel(QtCore.QAbstractTableModel):
    """Таблица с файлами"""
    HEADERS = ('Имя', 'Размер', 'Изменён')

    def __init__(self):
        super().__init__()
        self.rows = [(i, '', '') for i in os.listdir('/home/fox/')]
        self.rows.sort(key=lambda x: x[0])

    def columnCount(self, parent):  # noqa pylint: disable=invalid-name, unused-argument, missing-function-docstring
        return len(self.HEADERS)

    def headerData(self, column, orientation, role):  # noqa pylint: disable=invalid-name, missing-function-docstring
        if role != QtCore.Qt.DisplayRole or orientation != QtCore.Qt.Horizontal:
            return QtCore.QVariant()
        return self.HEADERS[column]

    def rowCount(self, parent):  # noqa pylint: disable=invalid-name, unused-argument
        return len(self.rows)

    def data(self, index, role):  # noqa
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        i, j = index.row(), index.column()
        log.debug('%d %d', i, j)
        return self.rows[i][j]
