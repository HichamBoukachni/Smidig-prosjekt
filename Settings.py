import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QPushButton, QComboBox, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 460, 500)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2A2A2A; 
                color: #FFFFFF;
            }
            QLabel {
                color: #FFFFFF;
                font-size: 14px;
            }
            QComboBox {
                background-color: #2A2A2A; 
                color: #FFFFFF; 
                border: 1px solid #FF4500; 
                padding: 5px;
                margin: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #444444;
                color: #FFFFFF;
                selection-background-color: #FF4500;
            }
            QCheckBox, QPushButton {
                background-color: #444444; 
                color: #FFFFFF; 
                border: 1px solid #FF4500; 
                padding: 10px;
                margin: 5px;
                border-radius: 5px;
            }
            QCheckBox::indicator {
                width: 30px; 
                height: 20px;
            }
            QPushButton {
                background-color: #FF4500; 
                color: #FFFFFF; 
                padding: 10px;
                border: 1px solid #FF4500; 
                border-radius: 5px;
                margin: 5px;
            }
        """)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        # Header
        self.header_label = QLabel("Settings")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 10px; margin-bottom: 20px;")
        layout.addWidget(self.header_label, 0, 0, 1, 4)

        # Automatically save to cloud (position swapped with Language)
        self.autosave_checkbox = QCheckBox("Automatically save to cloud", self)
        layout.addWidget(self.autosave_checkbox, 1, 0, 1, 2)

        # Language Selection (position swapped with Automatically save to cloud)
        self.language_label = QLabel("Language", self)
        self.language_combo = QComboBox(self)
        self.language_combo.addItem("English - US")
        layout.addWidget(self.language_label, 1, 2, 1, 1)
        layout.addWidget(self.language_combo, 1, 3, 1, 1)

        # Start when startup
        self.startup_checkbox = QCheckBox("Start when startup", self)
        layout.addWidget(self.startup_checkbox, 2, 2, 1, 2)

        # Notification Settings (position swapped with Automatically save to cloud)
        self.notification_checkbox = QCheckBox("Notification Settings", self)
        layout.addWidget(self.notification_checkbox, 2, 0, 1, 2)

        # Network Settings
        self.network_checkbox = QCheckBox("Network Settings", self)
        layout.addWidget(self.network_checkbox, 3, 0, 1, 2)

        # Security Settings
        self.security_checkbox = QCheckBox("Security Settings", self)
        layout.addWidget(self.security_checkbox, 3, 2, 1, 2)

        # Accessibility and Darkmode Settings
        self.accessibility_checkbox = QCheckBox("Accessibility Settings", self)
        self.darkmode_checkbox = QCheckBox("Darkmode", self)
        layout.addWidget(self.accessibility_checkbox, 4, 0, 1, 2)
        layout.addWidget(self.darkmode_checkbox, 4, 2, 1, 2)

        # Quit button
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button, 5, 0, 1, 4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec_())
