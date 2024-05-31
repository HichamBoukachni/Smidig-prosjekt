import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QComboBox, QSpacerItem, QSizePolicy
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
        top_layout.setContentsMargins(0, 0, 0, 0)


        # Middle layout for Title, margins og spacing
        middle_layout = QHBoxLayout()
        middle_spacer = QWidget()
        middle_spacer.setFixedHeight(-50)
        main_layout.addWidget(middle_spacer)
        middle_layout.setContentsMargins(0, 70, 0, 0)
        middle_layout.setSpacing(0)

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
                                        image: url(icons/arrowdownO.png);
                                        max-width: 150%; 
                                        max-height: 150%;
                                    }
                                    """)
        top_layout.addWidget(self.dropdown, alignment=Qt.AlignTop | Qt.AlignLeft)
        top_layout.addStretch()

        # Profile og Settings buttons
        self.profile_btn = QPushButton()
        self.profile_btn.setIcon(QIcon("icons/profile.png"))
        self.profile_btn.setIconSize(QSize(40, 40))
        self.profile_btn.setStyleSheet("QPushButton { background-color: ; border: none;}")
        top_layout.addWidget(self.profile_btn, alignment=Qt.AlignTop)

        self.settings_btn = QPushButton()
        self.settings_btn.setIcon(QIcon("icons/settings.png"))
        self.settings_btn.setIconSize(QSize(40, 40))
        self.settings_btn.setStyleSheet("QPushButton { background-color: ; border: none; }")
        top_layout.addWidget(self.settings_btn, alignment=Qt.AlignTop)

        main_layout.addLayout(top_layout)

        # Title
        self.titleVol = QLabel("Volatility3 ")
        self.titleVol.setStyleSheet("color: rgb(177, 188, 200); font-size: 80px; font-weight: bold;")
        self.titleVol.setAlignment(Qt.AlignCenter)

        self.titleBy = QLabel("by")
        self.titleBy.setStyleSheet("color: rgb(177, 188, 200); font-size: 40px; font-weight: bold; margin-top: 34%;")
        self.titleBy.setAlignment(Qt.AlignCenter)

        # Legger til Title til middle layout
        middle_layout.addWidget(self.titleVol)
        middle_layout.addWidget(self.titleBy)

        main_layout.addLayout(middle_layout)
        main_layout.setAlignment(middle_layout, Qt.AlignTop | Qt.AlignHCenter)

        # Logo
        self.logo = QLabel()
        self.logo.setStyleSheet("width: ;")
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setPixmap(QPixmap("icons/mnemoniclogo.png"))

        middle_layout.addWidget(self.logo)
        main_layout.addSpacerItem(QSpacerItem(40, 40, QSizePolicy.Maximum, QSizePolicy.Expanding))

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
        # pluginupload_btn.setIcon(QPixmap("icons/uploadgray.png"))
        pluginupload_btn.setStyleSheet(button_style)

        # Result button
        result_btn = QPushButton("Result")
        result_btn.setStyleSheet(button_style)
        """

        # Icons
        icons = [
            (QPixmap("icons/cmd.png"), "Command"),
            (QPixmap("icons/plugin.png"), "Plugin"),
            (QPixmap("icons/results.png"), "Result")
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