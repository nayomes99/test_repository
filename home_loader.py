import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from home import Ui_MainWindow
from Main_data_loader import DataLoaderApp   # <-- your data loader window


class HomeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ---------- CONNECT BUTTONS ----------
        self.ui.db_extract.clicked.connect(self.database_extract)
        self.ui.db_load.clicked.connect(self.database_load)
        self.ui.file_converter.clicked.connect(self.file_conversion)

        self.ui.adhoc_extract.clicked.connect(self.adhoc_extract)
        self.ui.adhoc_load.clicked.connect(self.adhoc_load)
        self.ui.adhoc_convert.clicked.connect(self.adhoc_file_conversion)

        # Keep child windows alive
        self.child_window = None

    # ---------- FUNCTIONS ----------
    def database_extract(self):
        QMessageBox.information(self, "Info", "Database Extract clicked")

    def database_load(self):
        """
        Opens Data Loader window
        """
        self.child_window = DataLoaderApp()
        self.child_window.show()

    def file_conversion(self):
        QMessageBox.information(self, "Info", "File Conversion clicked")

    def adhoc_extract(self):
        QMessageBox.information(self, "Info", "Adhoc Database Extract clicked")

    def adhoc_load(self):
        QMessageBox.information(self, "Info", "Adhoc Database Load clicked")

    def adhoc_file_conversion(self):
        QMessageBox.information(self, "Info", "Adhoc File Conversion clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeApp()
    window.show()
    sys.exit(app.exec_())
