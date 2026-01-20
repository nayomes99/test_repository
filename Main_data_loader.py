import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from data_loader import Ui_MainWindow   # <-- your UI file name


class DataLoaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.buttonBox.accepted.connect(self.submit_form)
        self.ui.buttonBox.rejected.connect(self.close)

    def submit_form(self):
        """
        Validate inputs → Store → Display
        """

        # -------- REQUIRED FIELDS --------
        required_fields = {
            "DB Schema": self.ui.in_db_schema.text(),
            "Table Name": self.ui.in_tablename.text(),
            "Input File Name": self.ui.in_input_file.text(),
            "Input File Path": self.ui.in_input_path.text(),
            "Delimiter": self.ui.in_delimiter.text(),
            "Chunk": self.ui.in_chunk.text(),
            "Encoding": self.ui.in_encoding.text()
        }

        # Check empty fields
        missing = [name for name, value in required_fields.items() if not value.strip()]

        if missing:
            QMessageBox.warning(
                self,
                "Missing Fields",
                "Please fill all required fields:\n\n" + "\n".join(missing)
            )
            return

        # -------- RADIO BUTTON VALUES --------
        cob_server = "Y" if self.ui.in_cob_server_yes.isChecked() else "N"
        header = "TRUE" if self.ui.in_header_yes.isChecked() else "FALSE"

        # -------- STORE ALL INPUT DATA --------
        form_data = {
            "db_schema": self.ui.in_db_schema.text(),
            "table_name": self.ui.in_tablename.text(),
            "cob_server": cob_server,
            "chunk": self.ui.in_chunk.text(),
            "custom_header": self.ui.in_customheader.toPlainText(),
            "columns_needed": self.ui.in_column_needed.toPlainText(),
            "skip_header": self.ui.in_skip_header.text(),
            "skip_footer": self.ui.in_skip_footer.text(),
            "sheet_name": self.ui.in_sheet_name_2.text(),
            "parquet_filter": self.ui.in_parquet_filter.text(),
            "column_alias": self.ui.in_column_alias.text(),
            "column_datatype": self.ui.in_datatype.text(),
            "csv_ignores": self.ui.in_scsv_ignores.text(),
            "input_file": self.ui.in_input_file.text(),
            "input_path": self.ui.in_input_path.text(),
            "delimiter": self.ui.in_delimiter.text(),
            "header": header,
            "encoding": self.ui.in_encoding.text(),
            "row_limit": self.ui.in_row_limit.text(),
            "source_dl": self.ui.in_source_dl.text()
        }

        # -------- DISPLAY DATA --------
        display_text = "\n".join(f"{k} : {v}" for k, v in form_data.items())

        QMessageBox.information(
            self,
            "Form Submitted Successfully",
            display_text
        )

        # Optional: print to console (for debugging)
        print(form_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataLoaderApp()
    window.show()
    sys.exit(app.exec_())
