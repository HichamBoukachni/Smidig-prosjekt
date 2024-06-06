import os
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, \
    QPushButton, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def plugin_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "Plugins.py")
        # subprocess.Popen(['python', target_file])
        # Bytt ut gjeldende prosess med target_file
        os.execl(sys.executable, sys.executable, target_file)

    def profile_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "mainlogin.py")
        # Åpner i nytt vindu
        subprocess.Popen(['python', target_file])
        # Bytt ut gjeldende prosess med target_file
        # os.execl(sys.executable, sys.executable, target_file)

    def command_button_clicked(self):
        # Open the command prompt
        subprocess.run(["start", "cmd", "/k", "cd volatility3"], shell=True)

    def __init__(self):
        super().__init__()

        # Main window styling
        self.setWindowTitle("Volatility3")
        self.resize(800, 600)
        self.setStyleSheet("background-color:  rgb(28, 37, 48);"
                           "color: rgb(177, 188, 200);")

        # Main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Dropdown menu for OS
        dropdown_layout = QHBoxLayout()
        dropdown = QComboBox()
        dropdown.addItems(["Linux", "Windows", "macOS"])
        dropdown.setStyleSheet("""
                                QComboBox { 
                                    background-color: rgb(42, 53, 65);
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
                                    image: url(images/_arrowdownO.png);
                                    max-width: 150%; 
                                    max-height: 150%;
                                }
                                """)
        dropdown_layout.addWidget(dropdown, alignment=Qt.AlignLeft)

        # Spacer to push dropdown up
        dropdown_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Profile and settings buttons
        profilesetting_layout = QHBoxLayout()
        profile_btn = QPushButton()
        profile_btn.setIcon(QIcon("images/_profile.png"))
        profile_btn.setStyleSheet("background-color: transparent;")
        profile_btn.setFixedSize(40, 40)
        profile_btn.setIconSize(profile_btn.size())
        profile_btn.clicked.connect(self.profile_button_clicked)

        setting_btn = QPushButton()
        setting_btn.setIcon(QIcon("images/_settings.png"))
        setting_btn.setStyleSheet("background-color: transparent;")
        setting_btn.setFixedSize(40, 40)
        setting_btn.setIconSize(setting_btn.size())

        # Adding profile and settings buttons to profilesettings_layout
        profilesetting_layout.addWidget(profile_btn)
        profilesetting_layout.addWidget(setting_btn)

        # Adding dropdown_layout to profilesettings_layout
        dropdown_layout.addLayout(profilesetting_layout)
        main_layout.addLayout(dropdown_layout)

        # Spacer to push title and icon upwards
        main_layout.addSpacerItem(QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Title and Icon
        title_layout = QHBoxLayout()

        # Spacer to create space over the title
        title_layout.addSpacerItem(QSpacerItem(40, 60, QSizePolicy.Expanding, QSizePolicy.Minimum))

        title = QLabel("<span style='font-size:80px'>Volatility3  </span> <span style='font-size:40px'>by</span>")
        title.setFont(QFont("Arial"))
        title.setStyleSheet("color: rgb(177, 188, 200); font-weight: bold")
        title_layout.addWidget(title)

        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("image: url(images/_mnemoniclogo.png);")
        title_layout.addWidget(icon_label)

        # Spacer to create space under the title
        title_layout.addSpacerItem(QSpacerItem(40, 60, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(title_layout)

        # Spacer between title and buttons
        main_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))

        # Buttons container and layout
        icon_layout = QHBoxLayout()
        icon_container = QWidget()
        icon_container.setLayout(icon_layout)
        icon_container.setFixedSize(950, 200)
        main_layout.addWidget(icon_container, alignment=Qt.AlignCenter)

        icon_container.setStyleSheet("""
                                             border-style: solid;
                                             border-width: 2px;
                                             border-radius: 15px;
                                             border-color: rgb(217, 111, 51);
                                             background-color: rgb(28, 37, 48);
                                             width: 300%;
                                             height: 90%;
                                        """)

        # Buttons images in a list

        icons = [
            (QPixmap("images/_cmd.png"), "Command"),
            (QPixmap("images/_plugin.png"), "Plugin"),
            (QPixmap("images/_results.png"), "Result")
        ]

        # Loop to create a button for each item in the icons list
        for icon, tooltip in icons:
            button = QPushButton()
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(90, 90))
            button.setToolTip(tooltip)
            button.setStyleSheet("""
                                 QPushButton { 
                                    background-color: rgb(42, 53, 65); 
                                    border-style: solid; 
                                    border-width: 2px;
                                    border-radius: 15px;
                                    broder-color: rgb(217, 111, 51);
                                    margin: 10%;
                                    padding: 50%; 
                                    width: 150%
                                 } 
                                 QPushButton:hover { 
                                    background-color:  rgb(28, 37, 48); 
                                 }
                                 """)

            if tooltip == "Plugin":
                button.clicked.connect(self.plugin_button_clicked)
            elif tooltip == "Command":
                button.clicked.connect(self.command_button_clicked)

            icon_layout.addWidget(button)

        # Spacer to push buttons upwards
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
