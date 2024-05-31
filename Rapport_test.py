import sys
import os
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGroupBox, QPushButton, QLabel, QVBoxLayout, QSizePolicy


class GuiExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        self.setStyleSheet("background-color: rgb(28, 37, 48);")

        #Creating the boxes it self for the ui
        main_layout.addWidget(self.createGroupBox1())
        #50px space between the left side to the middle box
        main_layout.addSpacing(30)
        #1 means that it can change size
        main_layout.addWidget(self.createGroupBox2(), 1)
        #15 px space between the right side to the middle box
        main_layout.addSpacing(10)
        main_layout.addWidget(self.createGroupBox3())

        self.setLayout(main_layout)

        self.setWindowTitle('Raport GUI test v1')
        self.setGeometry(100, 100, 1280, 720)

    #This is the left box, here is where you can see the report etc and add pages with the graphs
    def createGroupBox1(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox {background-color: rgb(59, 73, 89);"
                               "border: 2px solid rgb(217, 111, 51) ;"
                               "border-radius: 10px; }")
        lftBox = QHBoxLayout() #This takes the base settings for the boxes set in main_layout
        groupBox.setLayout(lftBox)
        groupBox.setFixedWidth(300)
        return groupBox

    #This is the middle box, here is going to show the graphs etc.
    def createGroupBox2(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox { background-color: rgb(59, 73, 89);"
                               "border: 2px solid rgb(217, 111, 51) ;"
                               "border-radius: 10px; }")
        midBox = QHBoxLayout() #This takes the base settings for the boxes set in main_layout
        groupBox.setLayout(midBox)
        return groupBox

    #Here is the right box, where contains the buttons and everything else which needs to be pressed
    def createGroupBox3(self):
        groupBox = QGroupBox()
        groupBox.setStyleSheet("QGroupBox { background-color: rgb(59, 73, 89);"
                               "border: 2px solid rgb(217, 111, 51) ; "
                               "border-radius: 10px; }")
        rgtBox = QVBoxLayout() #This takes the base settings for the boxes set in main_layout

        #Here is the images that are used as buttons and are called in os.path.join
        image_files = [
            'images\_settings.png',
            'images\_download.png',
            'images\_share.png',
            'images\_flag.png',
            'images\_heart.png',
            'images\_trash.png',
            'images\_barchart.png',
            'images\_piechart.png',
            'images\_lines.png',
            'images\_navarrowleft.png'

        ]

        # Uses a for statement to create 10 buttons with images instead with the width and height of 100px
        # Here it also assgings each button in the order of the images who so button 1 is settings etc.

        for i, image_file in enumerate(image_files):
            button = QPushButton()

            full_path = os.path.join(os.getcwd(), image_file)

            pixmap = QPixmap(full_path)

            pixmap = pixmap.scaled(30, 30)  # this just resizes the pixmap to 50x50

            button.setIcon(QIcon(pixmap))

            button.setIconSize(QSize(40, 50))  #Set icon size to the pixmap size

            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            button.clicked.connect(lambda _, btn=i: self.on_button_clicked(btn + 1))  # Connect button click to function

            rgtBox.addWidget(button)

            # Apply styles to make the button transparent and remove borders
            button.setStyleSheet("QPushButton "
                                 "{ border: none; background: transparent; }")

            rgtBox.addWidget(button)

        # Set the width of the right box at static 100px, so it doesn't move
        groupBox.setFixedWidth(70)
        groupBox.setLayout(rgtBox)
        return groupBox

    #this just defines what the buttons do when they are clicked.
    def on_button_clicked(self, button_number):
        print(f"Button {button_number} clicked")
        if button_number == 1:
            print("1")
        if button_number == 2:
            print("2")
        if button_number == 3:
            print("3")
        if button_number == 4:
            print("4")
        if button_number == 5:
            print("5")
        if button_number == 6:
            print("6")
        if button_number == 7:
            print("7")
        if button_number == 8:
            print("8")
        if button_number == 9:
            print("9")
        if button_number == 10:
            print("10")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuiExample()
    ex.show()
    sys.exit(app.exec_())