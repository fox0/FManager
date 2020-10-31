"""
Модели для отрисовки данных в таблице
"""
from PyQt5 import QtCore

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]


class TableModel(QtCore.QAbstractTableModel):
    """Таблица с файлами"""

    def rowCount(self, parent):  # noqa pylint: disable=invalid-name, no-self-use, unused-argument
        # How many rows are there?
        return len(rows)

    def columnCount(self, parent):  # noqa pylint: disable=invalid-name, no-self-use, unused-argument
        # How many columns?
        return len(headers)

    def data(self, index, role):  # noqa pylint: disable=no-self-use
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        # What's the value of the cell at the given index?
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):  # noqa pylint: disable=invalid-name, no-self-use
        if role != QtCore.Qt.DisplayRole or orientation != QtCore.Qt.Horizontal:
            return QtCore.QVariant()
        # What's the header for the given column?
        return headers[section]
