# Importing necessary modules for...
import os  # os-interactions
import subprocess  # running subprocesses
import sys  # system related operations
# Importing library from PyQt5 used for GUI-elements
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, \
    QPushButton, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

# Class to define the main window for the application
class MainWindow(QMainWindow):

# Buttons being connected to other .py files in the directory when pushed
    def profile_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "mainlogin.py")
        # Opens the target file in a new window
        subprocess.Popen(['python', target_file])

    def settings_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "Settings.py")
        # Opens the target file in a new window
        subprocess.Popen(['python', target_file])

    def plugin_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "Plugins.py")
        # Replacing the current running script with the target file
        os.execl(sys.executable, sys.executable, target_file)

    def command_button_clicked(self):
        # Open the command prompt
        subprocess.run(["start", "cmd", "/k", "cd volatility3"], shell=True)

    def result_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "Rapport_test.py")
        # Replacing the current running script with the target file
        os.execl(sys.executable, sys.executable, target_file)


    def __init__(self):
        super().__init__()  # Calling the constructor of QMainWindow

        # Main window styling
        self.setWindowTitle("Volatility3")  # Setting window title
        self.resize(800, 600)  # Setting window size
        # Setting background color and text color for the main window using CSS
        self.setStyleSheet("background-color:  rgb(28, 37, 48);"
                           "color: rgb(177, 188, 200);")

        # Main layout
        central_widget = QWidget()  # Creates a central widget
        self.setCentralWidget(central_widget)  # Setting central widget as main widget for the window
        main_layout = QVBoxLayout(central_widget)  # Creating a vertical layout on the central widget

        # Dropdown menu for OS
        dropdown_layout = QHBoxLayout()  # Creating a horizontal layout
        dropdown = QComboBox()  # Creating a combobox (dropdown menu)
        dropdown.addItems(["Linux", "Windows", "macOS"])  # Elements added to the combobox
        # Setting styling for the dropdown combobox
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
        # Adding the dropdown combobox to the horizontal layout
        dropdown_layout.addWidget(dropdown, alignment=Qt.AlignLeft)

        # Spacer to push dropdown combobox up
        dropdown_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Profile and settings buttons
        profilesetting_layout = QHBoxLayout() # Creating a horizontal layout
        profile_btn = QPushButton() # Creating a button
        profile_btn.setIcon(QIcon("images/_profile.png"))  # Setting an icon for the button
        profile_btn.setStyleSheet("background-color: transparent;")  # Setting background to transparent
        profile_btn.setFixedSize(40, 40)  # Setting button size
        profile_btn.setIconSize(profile_btn.size())  # Setting image size same as button size
        profile_btn.clicked.connect(self.profile_button_clicked)  # Connecting the button when clicked to the method

        setting_btn = QPushButton() # Creating a button
        setting_btn.setIcon(QIcon("images/_settings.png"))  # Setting an icon for the button
        setting_btn.setStyleSheet("background-color: transparent;")  # Setting background to transparent
        setting_btn.setFixedSize(40, 40)  # Setting button size
        setting_btn.setIconSize(setting_btn.size())  # Setting image size same as button size
        setting_btn.clicked.connect(self.settings_button_clicked)  # Connecting the button when clicked to the method

        # Adding profile and settings buttons to profilesettings_layout
        profilesetting_layout.addWidget(profile_btn)
        profilesetting_layout.addWidget(setting_btn)

        # Adding profilesettings_layout to dropdown_layout
        dropdown_layout.addLayout(profilesetting_layout)
        # Adding dropdown_layout to main_layout
        main_layout.addLayout(dropdown_layout)

        # Spacer to push title and icon upwards
        main_layout.addSpacerItem(QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Title and Icon
        title_layout = QHBoxLayout()  # Creating a horizontal layout

        # Spacer to create space over the title
        title_layout.addSpacerItem(QSpacerItem(40, 60, QSizePolicy.Expanding, QSizePolicy.Minimum))
        # Creating a QLabel with HTML-formating to set to different font sizes
        title = QLabel("<span style='font-size:80px'>Volatility3  </span> <span style='font-size:40px'>by</span>")
        # Setting styling for title
        title.setStyleSheet("color: rgb(177, 188, 200); font-style: Arial; font-weight: bold")
        title_layout.addWidget(title)  # Adding title widget to title_layout

        # Icon
        icon_label = QLabel()  # Creating a QLabel for the icon
        icon_label.setFixedSize(50, 50)  # Giving the QLabel a fixed size
        icon_label.setStyleSheet("image: url(images/_mnemoniclogo.png);")  # Giving the QLabel an image
        title_layout.addWidget(icon_label)  # Adding icon_label to title_layout

        # Spacer to create space under the title
        title_layout.addSpacerItem(QSpacerItem(40, 60, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(title_layout)  # Adding title_layout to main_layout

        # Spacer between title and buttons
        main_layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Minimum))

        # Buttons container and layout
        icon_layout = QHBoxLayout()  # Creating a horizontal layout
        icon_container = QWidget()  # Creating a widget used as a container
        icon_container.setLayout(icon_layout)  # Setting the layout for the icons_container
        icon_container.setFixedSize(950, 200)  # Giving the container a fixed size
        main_layout.addWidget(icon_container, alignment=Qt.AlignCenter)  # Adding icons_container to main_layout

        # Styling icons_container using CSS
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
            button = QPushButton()  # Creating a button
            button.setIcon(QIcon(icon))  # Setting icon from the list on button
            button.setIconSize(QSize(90, 90))  # Sizing the image
            button.setToolTip(tooltip)  # Setting tooltip when hovering the buttons
            # Styling for buttons
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
                                 QToolTip {
                                    border: none;
                                 }
                                 """)

            # Connects click-event to buttons based on tooltip
            if tooltip == "Plugin":
                button.clicked.connect(self.plugin_button_clicked)
            elif tooltip == "Command":
                button.clicked.connect(self.command_button_clicked)
            elif tooltip == "Result":
                button.clicked.connect(self.result_button_clicked)

            icon_layout.addWidget(button)  # Adding button to icon_layout

        # Spacer to push buttons upwards
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Creating an application instance
    window = MainWindow()  # Creating a window (MainWindow-object)
    window.show()  # Showing the window
    sys.exit(app.exec_())  # Starts and terminates the main loop of the application
