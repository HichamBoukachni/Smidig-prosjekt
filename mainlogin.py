import sys
import mysql.connector  # Import MySQL connector to connect to the database
from PyQt5.QtWidgets import (  # Import necessary PyQt5 widgets for the GUI
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QFrame, QMessageBox
)
from PyQt5.QtGui import QFont, QColor  # Import PyQt5 modules for fonts and colors
from PyQt5.QtCore import Qt  # Import Qt core module for alignment constants
import bcrypt  # Import bcrypt for password hashing

# Define the LoginWindow class, inheriting from QWidget
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()  # Initialize the base class
        self.initUI()  # Call the method to initialize the UI

    def initUI(self):
        main_layout = QVBoxLayout()  # Create the main vertical layout

        # Grey square at the top-right corner
        top_right_square = QLabel(self)
        top_right_square.setFixedSize(15, 15)  # Set fixed size for the square
        top_right_square.setStyleSheet("background-color: gray;")  # Set background color
        top_right_square.setAlignment(Qt.AlignCenter)  # Center align the square

        # Layout to align the square to the right
        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch()  # Add stretchable space
        top_right_layout.addWidget(top_right_square)  # Add the square widget
        main_layout.addLayout(top_right_layout)  # Add the layout to the main layout

        # Top spacer for spacing from the top
        top_spacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Create a spacer item
        main_layout.addItem(top_spacer)  # Add the spacer to the main layout

        # Grey square at the top in the center
        center_square = QLabel(self)
        center_square.setFixedSize(25, 25)  # Set fixed size for the square
        center_square.setStyleSheet("background-color: gray;")  # Set background color
        center_square.setAlignment(Qt.AlignCenter)  # Center align the square
        center_square_layout = QHBoxLayout()
        center_square_layout.addStretch(1)  # Add stretchable space to the left
        center_square_layout.addWidget(center_square)  # Add the square widget
        center_square_layout.addStretch(1)  # Add stretchable space to the right
        main_layout.addLayout(center_square_layout)  # Add the layout to the main layout

        # Spacer for equal spacing between the square and email input
        equal_spacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Create a spacer item
        main_layout.addItem(equal_spacer)  # Add the spacer to the main layout

        # Horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # Set the frame shape to horizontal line
        line.setFrameShadow(QFrame.Sunken)  # Set the frame shadow
        line.setStyleSheet("background-color: #D96F33;")  # Set background color
        main_layout.addWidget(line)  # Add the line to the main layout

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("email@domain.com")  # Set placeholder text
        self.email_input.setFixedHeight(40)  # Set fixed height
        self.email_input.setStyleSheet("background-color: white; color: black; padding: 10px; border: 2px solid #ccc; border-radius: 5px;")  # Set styles
        main_layout.addWidget(self.email_input)  # Add the email input to the main layout

        # Spacer between email input and password input
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password...")  # Set placeholder text
        self.password_input.setEchoMode(QLineEdit.Password)  # Set echo mode to password
        self.password_input.setFixedHeight(40)  # Set fixed height
        self.password_input.setStyleSheet("background-color: white; color: black; padding: 10px; border: 2px solid #ccc; border-radius: 5px;")  # Set styles
        main_layout.addWidget(self.password_input)  # Add the password input to the main layout

        # Spacer between password input and sign in button
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Button size
        button_width = 170  # Increased width by 10 px
        button_height = 40

        # Sign in button
        sign_in_button = QPushButton("Sign in", self)
        sign_in_button.setFixedHeight(button_height)  # Set fixed height
        sign_in_button.setFixedWidth(button_width)  # Set fixed width
        sign_in_button.setStyleSheet("""
            QPushButton {
                background-color: #D96F33; 
                color: black; 
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
        sign_in_layout.addStretch(1)  # Add stretchable space to the left
        sign_in_layout.addWidget(sign_in_button)  # Add the sign in button
        sign_in_layout.addStretch(1)  # Add stretchable space to the right
        main_layout.addLayout(sign_in_layout)  # Add the layout to the main layout

        # Spacer between sign in button and sign up label
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Sign up link
        sign_up_label = QLabel("Create an account")
        sign_up_label.setStyleSheet("color: white;")  # Set text color
        sign_up_label.setFont(QFont('Arial', 12))  # Set font
        sign_up_label.setAlignment(Qt.AlignCenter)  # Center align the label
        main_layout.addWidget(sign_up_label)  # Add the sign up label to the main layout

        sign_up_desc = QLabel("Enter your email to sign up for this app")
        sign_up_desc.setStyleSheet("color: gray;")  # Set text color
        sign_up_desc.setFont(QFont('Arial', 10))  # Set font
        sign_up_desc.setAlignment(Qt.AlignCenter)  # Center align the label
        main_layout.addWidget(sign_up_desc)  # Add the sign up description to the main layout

        # Spacer between sign up description and sign up button
        main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Add a spacer item

        # Sign up button
        sign_up_button = QPushButton("Sign up with email", self)
        sign_up_button.setFixedHeight(button_height)  # Set fixed height
        sign_up_button.setFixedWidth(button_width)  # Set fixed width
        sign_up_button.setStyleSheet("""
            QPushButton {
                background-color: #D96F33; 
                color: black; 
                margin-top: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #cc7634;
            }
        """)  # Set styles for the button

        # Center sign up button
        sign_up_layout = QHBoxLayout()
        sign_up_layout.addStretch(1)  # Add stretchable space to the left
        sign_up_layout.addWidget(sign_up_button)  # Add the sign up button
        sign_up_layout.addStretch(1)  # Add stretchable space to the right
        main_layout.addLayout(sign_up_layout)  # Add the layout to the main layout

        self.setLayout(main_layout)  # Set the main layout
        self.setWindowTitle('Login')  # Set the window title
        self.setGeometry(600, 300, 400, 500)  # Set the window geometry
        self.setAutoFillBackground(True)  # Enable auto fill background
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#2A3541"))  # Set background color
        self.setPalette(palette)  # Apply the palette

    def handle_login(self):
        email = self.email_input.text()  # Get the text from the email input
        password = self.password_input.text()  # Get the text from the password input

        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',  # Replace with your host
            user='root',  # Replace with your MySQL username
            password='Timerbest123!',  # Replace with your MySQL password
            database='accounts_login'  # Replace with your database name
        )
        cursor = conn.cursor()

        # Execute SQL query to fetch the hashed password for the provided email
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        # Check if a result was found and if the provided password matches the hashed password
        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            QMessageBox.information(self, 'Login Successful', 'You have successfully logged in.')  # Show success message
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid email or password.')  # Show failure message

        cursor.close()  # Close the cursor
        conn.close()  # Close the connection

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    login = LoginWindow()  # Create an instance of LoginWindow
    login.show()  # Show the login window
    sys.exit(app.exec_())  # Execute the application
