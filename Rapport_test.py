import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGroupBox, QPushButton, QLabel, QVBoxLayout, QSizePolicy


class GuiExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initiateGUI()

    def initiateGUI(self):
        main_layout = QHBoxLayout()

        self.setStyleSheet("background-color: rgb(28, 37, 48 );")

        # Creating the boxes it self for the ui
        main_layout.addWidget(self.createGroupBox1())
        # 50px space between the left side to the middle box
        main_layout.addSpacing(30)
        # 1 means that it can change size
        main_layout.addWidget(self.createGroupBox2(), 1)
        # 15 px space between the right side to the middle box
        main_layout.addSpacing(15)
        main_layout.addWidget(self.createGroupBox3())

        self.setLayout(main_layout)

        self.setWindowTitle('Raport GUI test v1')
        self.setGeometry(100, 100, 1280, 720)

    def createGroupBox1(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox {background-color: rgb(59, 73, 89);"
                               "border: 2px solid orange; "
                               "border-radius: 10px; }")
        vbox1 = QHBoxLayout()
        groupBox.setLayout(vbox1)
        groupBox.setFixedWidth(300)
        return groupBox
    def createGroupBox2(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox { background-color: rgb(59, 73, 89);"
                               "border: 2px solid orange; "
                               "border-radius: 10px; }")
        vbox2 = QHBoxLayout()
        groupBox.setLayout(vbox2)
        return groupBox
    def createGroupBox3(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox { background-color: rgb(59, 73, 89);"
                               "border: 2px solid orange; "
                               "border-radius: 10px; }")
        vbox3 = QVBoxLayout()

        ##Set the image names here
        images_files = [
            'settings.jpg',
            'download.jpg',
            'export.jpg',
            'content.jpg',
            'favorite.jpg',
            'delete.jpg',
            'graph1.png',
            'graph2.png',
            'graph3.png',
            'graph4.png'
        ]

        ##Uses a for statment to create 10 buttons with images instead with the width and hight of 20px
        for i in range(1, 11):
            button = QPushButton()
            pixmap = QPixmap(images_files)
            pixmap = pixmap.scaledToHeight(20)
            pixmap = pixmap.scaledToWidth(20)
            button.setIcon(QIcon(pixmap))
            button.setIconSize(pixmap.size())
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(lambda _, btn=i: self.on_button_clicked(btn))
            vbox3.addWidget(button)

        # set the widht of the right box at static 100px, so it doesnt move
        groupBox.setFixedWidth(100)
        groupBox.setLayout(vbox3)
        return groupBox


    # Def what the buttons do
    def on_button_clicked(self, button_number):
        print(f"Button {button_number} clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuiExample()
    ex.show()
    sys.exit(app.exec_())
