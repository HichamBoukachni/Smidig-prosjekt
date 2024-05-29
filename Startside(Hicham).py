import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Sett hovedlayout
        main_layout = QVBoxLayout()

        # Dropdown-meny for plattformvalg
        self.combo = QComboBox(self)
        self.combo.addItems(["Linux", "Windows", "Mac"])
        self.combo.setFixedWidth(300)  # Økt bredde på dropdown-menyen
        self.combo.setFixedHeight(60)  # Økt høyde på dropdown-menyen
        # Gjør teksten hvit i dropdown-menyen
        self.combo.setStyleSheet("""
            QComboBox {
                color: white;
                background-color: #2b2b2b;
                font-size: 20px;
            }
            QComboBox QAbstractItemView {
                color: white;
                background-color: #2b2b2b;
                selection-background-color: #3d3d3d;
            }
        """)
        combo_layout = QHBoxLayout()
        combo_layout.addWidget(self.combo)
        combo_layout.addStretch()
        main_layout.addLayout(combo_layout)

        # Etikett for hovedtekst "Volatility 3 by"
        self.title = QLabel('Volatility 3 by')
        self.title.setStyleSheet("color: white;")
        self.title.setFont(QFont('Arial', 24))
        self.title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title)

        # Etikett for "Mnemonic"
        self.subtitle = QLabel('Mnemonic')
        self.subtitle.setStyleSheet("color: white;")
        self.subtitle.setFont(QFont('Arial', 48, QFont.Bold))
        self.subtitle.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.subtitle)

        # Spacing for å flytte knappene ned
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Knapper med logoer
        button_layout = QHBoxLayout()
        button_layout.setSpacing(30)  # Sett avstand mellom knappene
        button_style = """
            QPushButton {
                background-color: #333;
                border: 2px solid orange;
                margin: 2px;
                padding: 0px;
            }
            QPushButton:hover {
                background-color: #444;
            }
        """

        self.button1 = QPushButton(self)
        self.button1.setIcon(QIcon(r'C:\users\hicha\Downloads\CMD 1.png'))  # Endret til riktig bane for Terminal-logoen
        self.button1.setIconSize(QSize(240, 240))  # Økt ikonstørrelse
        self.button1.setFixedSize(300, 300)  # Økt knappestørrelse
        self.button1.setStyleSheet(button_style)
        self.button1.clicked.connect(self.open_terminal)

        self.button2 = QPushButton(self)
        self.button2.setIcon(QIcon(r'C:\users\hicha\Downloads\Plug.png'))  # Endret til riktig bane for Tools-logoen
        self.button2.setIconSize(QSize(240, 240))  # Økt ikonstørrelse
        self.button2.setFixedSize(300, 300)  # Økt knappestørrelse
        self.button2.setStyleSheet(button_style)

        self.button3 = QPushButton(self)
        self.button3.setIcon(QIcon(r'C:\users\hicha\Downloads\bar chart.png'))  # Endret til riktig bane for Documentation-logoen
        self.button3.setIconSize(QSize(260, 260))  # Økt ikonstørrelse for å matche andre logoer
        self.button3.setFixedSize(300, 300)  # Økt knappestørrelse
        self.button3.setStyleSheet(button_style)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(button_layout)

        # Spacing for å flytte knappene ned
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Sett layout og vindusinnstillinger
        self.setLayout(main_layout)
        self.setWindowTitle('Volatility 3 Start Page')
        self.setGeometry(100, 100, 1200, 1000)  # Økt størrelse på vinduet
        self.setStyleSheet("background-color: #2b2b2b;")

    def open_terminal(self):
        volatility3_path = r"C:\Users\hicha\volatility3"  # Change to the actual path of Volatility 3
        if sys.platform == "win32":
            subprocess.Popen(f"start wt.exe cmd /K cd {volatility3_path}", shell=True)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", "Terminal", volatility3_path])
        elif sys.platform == "linux":
            subprocess.Popen(["x-terminal-emulator", "-e", f"cd {volatility3_path} && bash"])

def main():
    app = QApplication(sys.argv)
    ex = StartPage()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
