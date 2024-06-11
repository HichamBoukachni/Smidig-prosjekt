# settings_window.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton,
                             QComboBox, QHBoxLayout, QCheckBox, QSizePolicy, QSpacerItem)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)

        # Move the title higher
        title_label = QLabel('Settings')
        title_label.setFont(QFont('Arial', 30))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Define style for widgets
        label_style = "color: rgb(177, 188, 200); font-size: 18px;"
        combo_style = """
            QComboBox {
                color: rgb(177, 188, 200);
                background-color: rgb(42, 53, 65);
                font-size: 18px;
                padding: 5px;
                border: 1px solid rgb(217, 111, 51);
                border-radius:5px; 
            }
            QComboBox QAbstractItemView {
                color: rgb(177, 188, 200);
                background-color: rgb(42, 53, 65);
                selection-background-color: #FF6347;
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
        """
        toggle_style = """
            QCheckBox {
                color: rgb(177, 188, 200);
                font-size: 18px;
            }
        """
        button_style = """
            QPushButton {
                color: rgb(177, 188, 200);
                background-color: rgb(42, 53, 65);
                border: 2px solid rgb(217, 111, 51);
                padding: 10px;
                font-size: 18px;
                border: 1px solid rgb(217, 111, 51);
                border-radius:5px; 
            }
            QPushButton:hover {
                background-color: #FF6347;
            }
        """

        # Arrange widgets in a 6x2 grid with toggles under the text
        def add_labeled_toggle(row, text, col, grid_layout):
            label = QLabel(text)
            label.setStyleSheet(label_style)
            grid_layout.addWidget(label, row, col, alignment=Qt.AlignLeft)
            toggle = QCheckBox()
            toggle.setStyleSheet(toggle_style)
            grid_layout.addWidget(toggle, row + 1, col, alignment=Qt.AlignLeft)
            return toggle

        # First column
        lang_label = QLabel('Language')
        lang_label.setStyleSheet(label_style)
        grid_layout.addWidget(lang_label, 0, 0)

        self.combo = QComboBox(self)
        self.combo.addItems(["English - US", "Spanish - ES", "French - FR"])
        self.combo.setStyleSheet(combo_style)
        self.combo.setFixedHeight(40)  # Increase height
        grid_layout.addWidget(self.combo, 1, 0)

        # Add labeled toggles
        self.auto_save_toggle = add_labeled_toggle(2, 'Automatically save to cloud', 0, grid_layout)
        self.unknown_toggle1 = add_labeled_toggle(4, '?', 0, grid_layout)
        self.dark_mode_toggle = add_labeled_toggle(6, 'Darkmode', 0, grid_layout)

        # Second column
        self.start_toggle = add_labeled_toggle(0, 'Start when startup', 1, grid_layout)
        self.alert_toggle = add_labeled_toggle(2, 'Alert when progress is done', 1, grid_layout)
        self.unknown_toggle2 = add_labeled_toggle(4, '?', 1, grid_layout)

        main_layout.addLayout(grid_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add Quit button at the bottom left
        quit_button_layout = QHBoxLayout()
        quit_button = QPushButton('Quit')
        quit_button.setStyleSheet(button_style)
        quit_button.setFixedHeight(50)  # Increase height
        quit_button.setFixedWidth(100)  # Increase width
        quit_button.clicked.connect(self.quit_action)
        quit_button_layout.addWidget(quit_button, alignment=Qt.AlignLeft)
        quit_button_layout.addStretch()
        main_layout.addLayout(quit_button_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Settings')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: rgb(28, 37, 48); color: rgb(177, 188, 200);")
        self.setWindowFlags(Qt.FramelessWindowHint)  # Tar vekk den hvite greia på toppen

    def quit_action(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsWindow()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
