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

        # Top layout for Dropdown, Profile og Settings
        top_layout = QHBoxLayout()

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
        top_layout.addWidget(self.dropdown, alignment=Qt.AlignTop | Qt.AlignLeft)
        top_layout.addStretch()

        # Profile and Settings buttons
        self.profile_btn = QPushButton()
        self.profile_btn.setIcon(QIcon("chrBilder/profilegray.png"))
        self.profile_btn.setIconSize(QSize(40, 40))
        self.profile_btn.setStyleSheet("QPushButton { background-color: ; border: none;}")
        top_layout.addWidget(self.profile_btn, alignment=Qt.AlignTop)

        self.settings_btn = QPushButton()
        self.settings_btn.setIcon(QIcon("chrBilder/settings.png"))
        self.settings_btn.setIconSize(QSize(40, 40))
        self.settings_btn.setStyleSheet("QPushButton { background-color: ; border: none; }")
        top_layout.addWidget(self.settings_btn, alignment=Qt.AlignTop)

        main_layout.addLayout(top_layout)

        """
        # Settings and Profile icons
        topright_layout = QHBoxLayout()
        topright_layout.addStretch()

        profile_btn = QPushButton()
        profile_btn.setIcon(QIcon("chrBilder/profilegray.png"))
        profile_btn.setIconSize(QSize(40, 40))
        profile_btn.setStyleSheet(
            "QPushButton { background-color: ; border: none; }")
        topright_layout.addWidget(profile_btn)

        settings_btn = QPushButton()
        settings_btn.setIcon(QIcon("chrBilder/settings.png"))
        settings_btn.setIconSize(QSize(40, 40))
        settings_btn.setStyleSheet(
            "QPushButton { background-color: ; border: none; }")
        topright_layout.addWidget(settings_btn)

        topright_container = QWidget()
        topright_container.setStyleSheet("margin: 10%;"
                                         "margin-top: -20%;")
        topright_container.setLayout(topright_layout)
        main_layout.addWidget(topright_container, alignment=Qt.AlignTop | Qt.AlignRight)
        """

        title_layout = QHBoxLayout()
        title_container = QWidget()
        title_container.setLayout(title_layout)
        main_layout.addWidget(title_container, alignment=Qt.AlignCenter)

        # Title
        vol = QLabel(f"Volatility 3")
        vol.setAlignment(Qt.AlignCenter)
        vol.setStyleSheet("""
                            font-size: 70px; 
                            padding-top: 60%; 
                            padding-bottom: -400%
                            """)
        title_layout.addWidget(vol)

        by = QLabel(f"Volatility 3")
        vol.setAlignment(Qt.AlignCenter)

        # Logo
        label = QLabel(self)
        logo = QPixmap("chrBilder/mnemoniclogo.png")
        scaled_logo = logo.scaled(220, 156, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_logo)
        label.setStyleSheet(""" 
                            padding-top: -500%;
                            margin-top: -500%;
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
                                      border-radius: 15px;
                                      border-color: rgb(217, 111, 51);
                                      background-color: rgb(28, 37, 48);
                                      width: 300%;
                                      height: 90%;
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
                                    background-color: rgb(59, 73, 89); 
                                    border-style: solid; 
                                    border-width: 2px;
                                    border-radius: 15px;
                                    broder-color: rgb(217, 111, 51);
                                    margin: 20%;
                                    padding: 10%; 
                                    width: 150%
                                } 
                                QPushButton:hover { 
                                    background-color:  rgb(28, 37, 48); 
                                }
                                """)
            icons_layout.addWidget(button)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())