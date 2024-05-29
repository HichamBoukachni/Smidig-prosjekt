import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Design for grunnsiden
        self.setWindowTitle("Volatility3")
        self.setGeometry(100, 100, 800, 400)
        self.setStyleSheet("background-color:  rgb(18, 25, 33);"
                           "color: rgb(230, 232, 234)")
        # self.showMaximized()

        # Main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Dropdown
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Linux", "Windows", "macOS"])
        self.dropdown.setStyleSheet("""
                                    QComboBox { 
                                        background-color: rgb(59, 73, 89);
                                        color: rgb(230, 232, 234); 
                                        padding: 5px; 
                                        font-size: 20px;
                                        border-style: solid; 
                                        border-color: rgb(217, 111, 51);
                                        border-width: 2px;
                                        border-radius: 10px; 
                                        width: 150%;
                                    } 
                                    QComboBox::drop-down {
                                        border-radius: 10px; 
                                        width: 40%;
                                    }
                                    QComboBox::down-arrow {
                                        image: url(chrBilder/orangearrow.png);
                                        max-width: 150%; 
                                        max-height: 150%;
                                    }
                                    """)
        main_layout.addWidget(self.dropdown, alignment=Qt.AlignLeft)

        # Title
        title = QLabel(f"Volatility 3 by\n")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
                            font-size: 70px; 
                            padding-top: 60%; 
                            padding-bottom: -400%
                            """)
        main_layout.addWidget(title)

        # Logo
        label = QLabel(self)
        logo = QPixmap("chrBilder/mnemoniclogo.png")
        scaled_logo = logo.scaled(320, 256, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_logo)
        label.setStyleSheet("""
                            padding-bottom: 100%; 
                            padding-top: -450%;
                            margin-bottom: -50%; 
                            margin-top: -50%;
                            """)
        label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label)

        # Icons layout
        icons_layout = QHBoxLayout()
        icons_container = QWidget()
        icons_container.setLayout(icons_layout)
        main_layout.addWidget(icons_container, alignment=Qt.AlignCenter)

        icons_container.setStyleSheet("""border-style: solid;
                                      border-width: 2px;
                                      border-radius: 10px;
                                      border-color: rgb(217, 111, 51);
                                      width: 300%;
                                      height: 160%;
                                      """)
        icons_layout.setSpacing(30)

        """
        button_style = 
                        QPushButton { 
                            background-color: rgb(28, 37, 48); 
                            border-style: solid; 
                            border-width: 2px;
                            border-radius: 10px;
                            broder-color: rgb(217, 111, 51);
                            padding: 20px; 
                        } 
                        QPushButton:hover { 
                            background-color: rgb(28, 37, 48); 
                        }

        # Cmd button
        cmd_btn = QPushButton("Command")
        cmd_btn.setStyleSheet(button_style)

        # Plugin button
        pluginupload_btn = QPushButton("Plugin", "Upload")
        # pluginupload_btn.setIcon(QPixmap("chrBilder/uploadgray.png"))
        pluginupload_btn.setStyleSheet(button_style)

        # Result button
        result_btn = QPushButton("Result")
        result_btn.setStyleSheet(button_style)
        """

        # Icons
        icons = [
            (QPixmap("chrBilder/cmdgray.png"), "Command"),
            (QPixmap("chrBilder/plugingray.png"), "Plugin"),
            (QPixmap("chrBilder/resultgray.png"), "Result")
        ]

        for icon, tooltip in icons:
            button = QPushButton()
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(90, 90))
            button.setToolTip(tooltip)
            button.setStyleSheet("""
                                QPushButton { 
                                    background-color:  rgb(28, 37, 48); 
                                    border-style: solid; 
                                    border-width: 2px;
                                    border-radius: 10px;
                                    broder-color: rgb(217, 111, 51);
                                    padding: 20px; 
                                    width: 200%
                                } 
                                QPushButton:hover { 
                                    background-color:  rgb(28, 37, 48); 
                                }
                                """)
            icons_layout.addWidget(button)

        # Settings and Profile icons
        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch()

        profile_button = QPushButton()
        profile_button.setIcon(QIcon("chrBilder/profile.png"))
        profile_button.setIconSize(QPixmap("chrBilder/profile.png").rect().size())
        profile_button.setStyleSheet(
            "QPushButton { background-color: ; border: none; } QPushButton:hover { background-color: ; }")
        top_right_layout.addWidget(profile_button)

        settings_button = QPushButton()
        settings_button.setIcon(QIcon("chrBilder/settings.png"))
        settings_button.setIconSize(QSize(90, 90))
        settings_button.setStyleSheet(
            "QPushButton { background-color: ; border: none; } QPushButton:hover { background-color: ; }")
        top_right_layout.addWidget(settings_button)

        top_right_container = QWidget()
        top_right_container.setLayout(top_right_layout)
        main_layout.addWidget(top_right_container, alignment=Qt.AlignTop | Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())