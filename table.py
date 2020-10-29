from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPlainTextEdit, QTabWidget, QVBoxLayout, QDirModel, \
    QTreeView, QTableView, QWidget, QLineEdit, QPushButton, QHBoxLayout, QHeaderView, QGridLayout, QMenuBar, QMenu, qApp

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]


class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        # How many rows are there?
        return len(rows)

    def columnCount(self, parent=None, *args, **kwargs):
        # How many columns?
        return len(headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        # What's the value of the cell at the given index?
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        # What's the header for the given column?
        return headers[section]
