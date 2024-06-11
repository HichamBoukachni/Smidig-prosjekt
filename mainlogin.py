import os
import subprocess
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFrame
)
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import Qt
import bcrypt


# Define the LoginWindow class, inheriting from QWidget
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()  # begins the base class
        self.initUI()  # Call the method to set up the UI

    def resizeEvent(self, event):
        # Make the border_frame size match the window size
        self.border_frame.setGeometry(self.rect())
        super().resizeEvent(event)

    def createacc_button_clicked(self):
        # Get the directory of this script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Get the path to the createacc.py file
        target_file = os.path.join(current_dir, "createacc.py")
        # Open createacc.py in a new window
        os.execl(sys.executable, sys.executable, target_file)

    def initUI(self):
        main_layout = QVBoxLayout()  # Create the main layout that set up things vertically

        # Makes a frame, so it adds a boarder around the window
        self.border_frame = QFrame(self)
        self.border_frame.setStyleSheet("border: 2px solid rgb(42, 53, 65);")
        self.border_frame.setLineWidth(2)

        # Makes the frame the same size as the main window
        self.border_frame.setGeometry(self.rect())

        # Makes a layout inside the border frame
        layout = QVBoxLayout(self.border_frame)
        self.border_frame.setLayout(layout)

        # Button in the top-right corner to close the window
        top_right_square = QPushButton()
        top_right_square.setIcon(QIcon("images/_closeicon.png"))
        top_right_square.setStyleSheet("background-color: transparent;")
        top_right_square.setFixedSize(15, 15)  # Set size for the button
        top_right_square.clicked.connect(self.close)  # Close window when button is clicked

        # Layout to put the button on the right
        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch()  # Adds space
        top_right_layout.addWidget(top_right_square)  # Add the button to the layout
        main_layout.addLayout(top_right_layout)  # Add the layout to the "main layout"

        # Space between the top and the next object
        top_spacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Create a spacer item
        main_layout.addItem(top_spacer)  # Adds the space to the main layout

        # Picture in the center at the top
        center_square = QLabel(self)
        center_square.setFixedSize(75, 75)  # Sets size for the picture
        center_square.setStyleSheet("""background-color: transparent; 
                                        image: url(images/_profile.png); 
                                        border-style: solid; 
                                        border-color: rgb(217, 111, 51); 
                                        border-width: 2px;
                                        border-radius: 37px;
                                        padding: 8px;
                                    """)  # Sets picture and border
        center_square.setAlignment(Qt.AlignCenter)  # Centers the picture
        center_square_layout = QHBoxLayout()
        center_square_layout.addStretch(1)  # Adds space to the left
        center_square_layout.addWidget(center_square)  # Adds the picture to the layout
        center_square_layout.addStretch(1)  # Adds space to the right
        main_layout.addLayout(center_square_layout)  # Adds the layout to the "main layout"

        # Space between the picture and the email input
        equal_spacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Create spaces
        main_layout.addItem(equal_spacer)  # Add the spaces to the "main layout"

        # Horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # Set the line to be horizontal
        line.setFrameShadow(QFrame.Sunken)  # Set the line style
        line.setStyleSheet("background-color: rgb(217, 111, 51);")  # Set color for the line
        main_layout.addWidget(line)  # Add the line to the main layout

        # Email input field
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("email@domain.com")  # Set placeholder text
        self.email_input.setFixedHeight(40)  # Set height
        self.email_input.setStyleSheet(
            "background-color: white; color: black; padding: 10px; border: 2px solid #ccc; border-radius: 5px;")  # Set styles
        main_layout.addWidget(self.email_input)  # Add the email input to the main layout

        # Space between email input and password input
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Password input field
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password...")  # Set placeholder text
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide text as it's typed
        self.password_input.setFixedHeight(40)  # Set height
        self.password_input.setStyleSheet(
            "background-color: white; color: black; padding: 10px; border: 2px solid #ccc; border-radius: 5px;")  # Set styles
        main_layout.addWidget(self.password_input)  # Add the password input to the main layout

        # Space between password input and sign in button
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adds some space

        # Button size
        button_width = 170  # Width of the button
        button_height = 40  # Height of the button

        # Sign in button
        sign_in_button = QPushButton("Sign in", self)
        sign_in_button.setFixedHeight(button_height)  # Set height
        sign_in_button.setFixedWidth(button_width)  # Set width
        sign_in_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(217, 111, 51); 
                color: rgb(28, 37, 48); 
                margin-top: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #cc7634;
            }
        """)  # Set styles for the button
        sign_in_button.clicked.connect(self.handle_login)  # Connect the button click to handle_login method

        # Center sign in button
        sign_in_layout = QHBoxLayout()
        sign_in_layout.addStretch(1)  # Adds space to the left
        sign_in_layout.addWidget(sign_in_button)  # Adds the signin button
        sign_in_layout.addStretch(1)  # Adds space to the right
        main_layout.addLayout(sign_in_layout)  # Adds the layout to the main layout

        # Space between sign in button and sign up label
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adds some space

        # Sign up link
        sign_up_label = QLabel("Create an account")
        sign_up_label.setStyleSheet("color: white;")  # Set text color
        sign_up_label.setFont(QFont('Arial', 12))  # Set font size
        sign_up_label.setAlignment(Qt.AlignCenter)  # Centers the text
        main_layout.addWidget(sign_up_label)  # Add the signup label to the main layout

        sign_up_desc = QLabel("Enter your email to sign up for this app")
        sign_up_desc.setStyleSheet("color: gray;")  # Set text color
        sign_up_desc.setFont(QFont('Arial', 10))  # Set font size
        sign_up_desc.setAlignment(Qt.AlignCenter)  # Center align the text
        main_layout.addWidget(sign_up_desc)  # Add the signup description to the main layout

        # Space between sign up description and sign up button
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Sign up button
        sign_up_button = QPushButton("Sign up with email", self)
        sign_up_button.setFixedHeight(button_height)  # Set height
        sign_up_button.setFixedWidth(button_width)  # Set width
        sign_up_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(217, 111, 51); 
                color: rgb(28, 37, 48); 
                margin-top: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #cc7634;
            }
        """)  # Set styles for the button
        sign_up_button.clicked.connect(
            self.createacc_button_clicked)  # Connect button to createacc_button_clicked method

        # Center sign up button
        sign_up_layout = QHBoxLayout()
        sign_up_layout.addStretch(1)  # Adds space to the left
        sign_up_layout.addWidget(sign_up_button)  # Add the signup button
        sign_up_layout.addStretch(1)  # Adds space to the right
        main_layout.addLayout(sign_up_layout)  # Add the layout to the main layout

        # Main window
        self.setLayout(main_layout)  # Set the main layout
        self.setWindowTitle('Login')  # Set the window title
        self.setGeometry(600, 300, 400, 500)  # Set the window size and position
        self.setAutoFillBackground(True)  # Enable to fill the background
        self.setStyleSheet("""background-color: rgb(28, 37, 48); 
                              color: rgb(177, 188, 200); 
                            """)  # Set background and text color
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window frame

    def handle_login(self):
        email = self.email_input.text()  # Get the text from the email input
        password = self.password_input.text()  # Get the text from the password input

        # This is the SQL bit that where supossed to work. But i dindt have enough time to make it work.

        # Connect to MySQL database
        # conn = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     password='Timerbest123!',
        #     database='accounts_login'
        # )
        # cursor = conn.cursor()

        # Execute SQL query to fetch the hashed password for the provided email
        # query = "SELECT password FROM users WHERE email = %s"
        # cursor.execute(query, (email,))
        # result = cursor.fetchone()

        # Check if a result was found and if the provided password matches the hashed password
        # if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        #     QMessageBox.information(self, 'Login Successful', 'You have successfully logged in.')
        # else:
        #     QMessageBox.warning(self, 'Login Failed', 'Invalid email or password.')

        # cursor.close()
        # conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())