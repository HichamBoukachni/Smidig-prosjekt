import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QComboBox, QGridLayout, QFormLayout, \
    QDialogButtonBox, QLineEdit, QSpinBox, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 460, 500)
        self.default_stylesheet = self.get_stylesheet()
        self.setStyleSheet(self.default_stylesheet)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint & ~Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Tar vekk den hvite greia på toppen

        self.initUI()

    def resizeEvent(self, event):
        # Update the border_frame size to match the window size
        self.border_frame.setGeometry(self.rect())
        super().resizeEvent(event)

    def initUI(self):
        self.layout = QGridLayout()

        # Create a QFrame to add the border
        self.border_frame = QFrame(self)
        self.border_frame.setStyleSheet("border: 2px solid rgb(42, 53, 65);")
        self.border_frame.setLineWidth(2)

        # Make QFrame the same size as the main window
        self.border_frame.setGeometry(self.rect())

        # Create a layout inside the border frame
        layout = QVBoxLayout(self.border_frame)
        self.border_frame.setLayout(layout)

        # Header
        self.header_label = QLabel("Settings")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 10px; margin-bottom: 20px;")
        self.layout.addWidget(self.header_label, 0, 0, 1, 4)

        # Automatically save to cloud
        self.autosave_button = QPushButton("Automatically save to cloud", self)
        self.autosave_button.clicked.connect(self.show_autosave_settings)
        self.layout.addWidget(self.autosave_button, 1, 0, 1, 2)

        # Language Selection
        self.language_label = QLabel("Language", self)
        self.language_combo = QComboBox(self)
        self.language_combo.addItem("English - US")
        self.language_combo.addItem("Norwegian - NO")
        self.language_combo.currentIndexChanged.connect(self.change_language)
        self.layout.addWidget(self.language_label, 1, 2, 1, 1)
        self.layout.addWidget(self.language_combo, 1, 3, 1, 1)

        # User Settings
        self.user_button = QPushButton("User Settings", self)
        self.user_button.clicked.connect(self.show_user_settings)
        self.layout.addWidget(self.user_button, 2, 2, 1, 2)

        # Notification Settings
        self.notification_button = QPushButton("Notification Settings", self)
        self.notification_button.clicked.connect(self.show_notification_settings)
        self.layout.addWidget(self.notification_button, 2, 0, 1, 2)

        # Network Settings
        self.network_button = QPushButton("Network Settings", self)
        self.network_button.clicked.connect(self.show_network_settings)
        self.layout.addWidget(self.network_button, 3, 0, 1, 2)

        # Security Settings
        self.security_button = QPushButton("Security Settings", self)
        self.security_button.clicked.connect(self.show_security_settings)
        self.layout.addWidget(self.security_button, 3, 2, 1, 2)

        # Accessibility and Darkmode Settings
        self.accessibility_button = QPushButton("Accessibility Settings", self)
        self.accessibility_button.clicked.connect(self.show_accessibility_settings)
        self.darkmode_button = QPushButton("Darkmode", self)
        self.darkmode_button.setCheckable(True)
        self.darkmode_button.clicked.connect(self.toggle_darkmode)
        self.layout.addWidget(self.accessibility_button, 4, 0, 1, 2)
        self.layout.addWidget(self.darkmode_button, 4, 2, 1, 2)

        # Quit button
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.accept)
        self.layout.addWidget(self.quit_button, 5, 0, 1, 4)

        self.setLayout(self.layout)

        self.language_dict = {
            "English - US": {
                "header": "Settings",
                "autosave": "Automatically save to cloud",
                "user_settings": "User Settings",
                "notification_settings": "Notification Settings",
                "network_settings": "Network Settings",
                "security_settings": "Security Settings",
                "accessibility_settings": "Accessibility Settings",
                "darkmode": "Darkmode",
                "quit": "Quit",
                "language": "Language"
            },
            "Norwegian - NO": {
                "header": "Innstillinger",
                "autosave": "Lagre automatisk til skyen",
                "user_settings": "Brukerinnstillinger",
                "notification_settings": "Varslingsinnstillinger",
                "network_settings": "Nettverksinnstillinger",
                "security_settings": "Sikkerhetsinnstillinger",
                "accessibility_settings": "Tilgjengelighetsinnstillinger",
                "darkmode": "Mørk modus",
                "quit": "Avslutt",
                "language": "Språk"
            }
        }

        self.update_language("English - US")

    def get_stylesheet(self):
        return """
            QDialog {
                background-color: rgb(255, 255, 255); 
                color: rgb(0, 0, 0);
            }
            QLabel {
                color: rgb(0, 0, 0);
                font-size: 14px;
            }
            QComboBox {
                background-color: rgb(255, 255, 255); 
                color: rgb(0, 0, 0); 
                border: 1px solid rgb(217, 111, 51); 
                border-radius: 5px;
                padding: 5px;
                margin: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                selection-background-color: #FF4500;
            }
            QComboBox::drop-down {
                border-radius: 10px; 
                width: 40%;
            }
            QComboBox::down-arrow {
                image: url(images/_arrowdownO.png);
                max-width: 150%; 
                max-height: 150%;
            }
            QPushButton {
                background-color: rgb(255, 255, 255); 
                color: rgb(0, 0, 0); 
                border: 1px solid rgb(217, 111, 51); 
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
            }
            QPushButton:checked {
                background-color: #FF4500; 
                color: rgb(255, 255, 255);
            }
            QPushButton:hover {
                background-color: #FF6347;
            }
            QComboBox:hover {
                border: 1px solid #FF6347;
            }
        """

    def get_darkmode_stylesheet(self):
        return """
            QDialog {
                background-color: rgb(28, 37, 48); 
                color: rgb(177, 188, 200);
            }
            QLabel {
                color: rgb(177, 188, 200);
                font-size: 14px;
            }
            QComboBox {
                background-color: rgb(42, 53, 65); 
                color: rgb(177, 188, 200); 
                border: 1px solid rgb(217, 111, 51);
                border-radius:5px; 
                padding: 5px;
                margin: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: rgb(42, 53, 65);
                color: rgb(177, 188, 200);
                selection-background-color: rgb(217, 111, 51);
            }
            QComboBox::drop-down {
                border-radius: 10px; 
                width: 40%;
            }
            QComboBox::down-arrow {
                image: url(images/_arrowdownO.png);
                max-width: 150%; 
                max-height: 150%;
            }
            QPushButton {
                background-color: rgb(42, 53, 65); 
                color: rgb(177, 188, 200); 
                border: 1px solid rgb(217, 111, 51); 
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
            }
            QPushButton:checked {
                background-color: #FF4500; 
                color: #C0C0C0;
            }
            QPushButton:hover {
                background-color: #FF6347;
            }
            QComboBox:hover {
                border: 1px solid #FF6347;
            }
        """

    def update_language(self, language):
        self.header_label.setText(self.language_dict[language]["header"])
        self.autosave_button.setText(self.language_dict[language]["autosave"])
        self.user_button.setText(self.language_dict[language]["user_settings"])
        self.notification_button.setText(self.language_dict[language]["notification_settings"])
        self.network_button.setText(self.language_dict[language]["network_settings"])
        self.security_button.setText(self.language_dict[language]["security_settings"])
        self.accessibility_button.setText(self.language_dict[language]["accessibility_settings"])
        self.darkmode_button.setText(self.language_dict[language]["darkmode"])
        self.quit_button.setText(self.language_dict[language]["quit"])
        self.language_label.setText(self.language_dict[language]["language"])

    def change_language(self):
        selected_language = self.language_combo.currentText()
        self.update_language(selected_language)

    def show_autosave_settings(self):
        self.show_popup("Autosave Settings", "Configure your autosave settings here.")

    def show_user_settings(self):
        dialog = QDialog(self)
        dialog.setWindowTitle(self.user_button.text())
        dialog.setGeometry(150, 150, 300, 300)
        dialog.setStyleSheet(self.get_stylesheet())

        layout = QFormLayout()
        layout.addRow(QLabel(self.user_button.text()))

        name_input = QLineEdit(dialog)
        name_input.setPlaceholderText("Name")
        layout.addRow("Name:", name_input)

        email_input = QLineEdit(dialog)
        email_input.setPlaceholderText("Email")
        layout.addRow("Email:", email_input)

        password_input = QLineEdit(dialog)
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setPlaceholderText("Password")
        layout.addRow("Password:", password_input)

        confirm_password_input = QLineEdit(dialog)
        confirm_password_input.setEchoMode(QLineEdit.Password)
        confirm_password_input.setPlaceholderText("Confirm Password")
        layout.addRow("Confirm Password:", confirm_password_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, dialog)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        dialog.setLayout(layout)
        dialog.exec_()

    def show_notification_settings(self):
        self.show_popup("Notification Settings", "Configure your notification settings here.")

    def show_network_settings(self):
        self.show_popup("Network Settings", "Configure your network settings here.")

    def show_security_settings(self):
        self.show_popup("Security Settings", "Configure your security settings here.")

    def show_accessibility_settings(self):
        self.show_popup("Accessibility Settings", "Configure your accessibility settings here.")

    def show_popup(self, title, text):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setGeometry(150, 150, 300, 200)
        dialog.setStyleSheet(self.get_stylesheet())
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        dialog.setLayout(layout)
        dialog.exec_()

    def toggle_darkmode(self):
        if self.darkmode_button.isChecked():
            self.setStyleSheet(self.get_darkmode_stylesheet())
        else:
            self.setStyleSheet(self.default_stylesheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SettingsDialog()
    dialog.show()
    sys.exit(app.exec_())
