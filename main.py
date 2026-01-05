import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Import the generated UI file (DO NOT MODIFY IT)
from data_extractor import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.buttonBox.accepted.connect(self.validate_and_submit)
        self.ui.buttonBox.rejected.connect(self.close)

    # -----------------------------
    # Validation Helpers
    # -----------------------------
    def mark_invalid(self, widget):
        widget.setStyleSheet("border: 2px solid red;")

    def clear_invalid(self, widget):
        widget.setStyleSheet("")

    # -----------------------------
    # Main Validation Logic
    # -----------------------------
    def validate_and_submit(self):

        # Required QLineEdit fields
        required_line_edits = [
            self.ui.in_db_schema_2,     # Job Name
            self.ui.in_db_schema,       # Database Schema
            self.ui.in_output_path,     # Output Path
            self.ui.in_output_file,     # Output File Name
            self.ui.in_output_extension,# Output Extension
            self.ui.in_output_delimiter,# Output Delimiter
            self.ui.in_sheet_name,      # Sheet Name
            self.ui.in_chunk            # Chunk Size
        ]

        # Required QTextEdit fields
        required_text_edits = [
            self.ui.in_query             # SQL Query
        ]

        # Required QComboBox fields
        required_combo_boxes = [
            self.ui.in_custom_header,
            self.ui.in_date_format,
            self.ui.in_csv_quoting,
            self.ui.in_output_mode
        ]

        errors = []

        # Validate QLineEdit
        for field in required_line_edits:
            if not field.text().strip():
                self.mark_invalid(field)
                errors.append(field.objectName())
            else:
                self.clear_invalid(field)

        # Validate QTextEdit
        for field in required_text_edits:
            if not field.toPlainText().strip():
                self.mark_invalid(field)
                errors.append(field.objectName())
            else:
                self.clear_invalid(field)

        # Validate QComboBox
        for combo in required_combo_boxes:
            value = combo.currentText().strip()
            if not value or value.lower() == "none":
                self.mark_invalid(combo)
                errors.append(combo.objectName())
            else:
                self.clear_invalid(combo)

        # Stop if errors exist
        if errors:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please fill all required fields before submitting."
            )
            return

        # All validations passed
        self.submit_form()

    # -----------------------------
    # Submit Handler
    # -----------------------------
    def submit_form(self):
        QMessageBox.information(
            self,
            "Success",
            "Form submitted successfully!"
        )
        # 👉 Add your extraction logic here


# -----------------------------
# Application Entry Point
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
