import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QFrame, QDesktopWidget
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import bcrypt


# import mysql.connector  # Import MySQL connector to connect to the database

# Define the RegisterForm class, inheriting from QWidget
class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Call the method to set up the UI

    def back_button_clicked(self):
        # Gets the directory of this script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Gets the path to the mainlogin.py file
        target_file = os.path.join(current_dir, "mainlogin.py")
        # Opens mainlogin.py in a new window
        os.execl(sys.executable, sys.executable, target_file)

    def resizeEvent(self, event):
        # Makes the border_frame size match the window size
        self.border_frame.setGeometry(self.rect())
        super().resizeEvent(event)

    def initUI(self):
        self.setWindowTitle('Create Account')  # Sets window title
        self.setFixedSize(400, 500)  # Sets fixed window size
        self.setStyleSheet("""background-color: rgb(28, 37, 48); 
                              color: rgb(177, 188, 200); 
                            """)  # Sets background and text color
        self.setWindowFlags(Qt.FramelessWindowHint)  # Removes window frame

        self.center()  # Centers the window

        main_layout = QVBoxLayout()  # Creates main vertical layout

        # Creates a frame to add a border around the window
        self.border_frame = QFrame(self)
        self.border_frame.setStyleSheet("border: 2px solid rgb(42, 53, 65);")
        self.border_frame.setLineWidth(2)

        # makes the frame the same size as the main window
        self.border_frame.setGeometry(self.rect())

        # Creates a layout inside the border frame
        layout = QVBoxLayout(self.border_frame)
        self.border_frame.setLayout(layout)

        top_layout = QHBoxLayout()  # Creates a horizontal layout for the top section

        # Back button to go back to mainlogin.py
        self.back_button = QPushButton(self)
        self.back_button.setIcon(QIcon("images/_navarrowleft.png"))
        self.back_button.setStyleSheet("background-color: transparent;")
        self.back_button.setFixedSize(22, 22)
        top_layout.addStretch()  # Adds space
        top_layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back_button_clicked)

        main_layout.addLayout(top_layout)  # Adds the top layout to the "main layout"

        layout = QVBoxLayout()  # Ceate another vertical layout for form elements

        # Profile picture icon
        profile_icon = QLabel(self)
        profile_icon.setFixedSize(75, 75)
        profile_icon.setStyleSheet("""
                                        background-color: transparent;
                                        image: url(images/_profile.png);
                                        border-style: solid; 
                                        border-color: rgb(217, 111, 51); 
                                        border-width: 2px;
                                        border-radius: 37px;
                                        padding: 8px;
                                    """)
        profile_icon.setAlignment(Qt.AlignCenter)  # Center the icon
        center_square_layout = QHBoxLayout()
        center_square_layout.addStretch(1)  # Adds space to the left
        center_square_layout.addWidget(profile_icon)
        center_square_layout.addStretch(1)  # Adds space to the right
        layout.addLayout(center_square_layout)  # Adds the layout to the "main layout"
        layout.addSpacing(20)  # adds space

        # Horizontal line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)  # set the line to be horizontal
        self.line.setFrameShadow(QFrame.Sunken)  # set the line style
        self.line.setStyleSheet("color: #D96F33; background-color: #D96F33;")  # Set color for the line
        layout.addWidget(self.line)  # adds the line to the layout

        # Name input field
        self.label_name = QLabel('Your name', self)
        layout.addWidget(self.label_name)  # Adds the name label to the layout
        self.entry_name = QLineEdit(self)
        self.entry_name.setStyleSheet(self.get_entry_stylesheet())  # Set styles for the name input
        layout.addWidget(self.entry_name)  # Adds the name input to the layout

        # Email input field
        self.label_email = QLabel('Email address', self)
        layout.addWidget(self.label_email)  # adds the email label to the layout
        self.entry_email = QLineEdit(self)
        self.entry_email.setStyleSheet(self.get_entry_stylesheet())  # Sets styles fir the email input
        layout.addWidget(self.entry_email)  # adds the email input to the layout

        # Password input field
        self.label_password = QLabel('Create password', self)
        layout.addWidget(self.label_password)  # Adds the password label to the layout
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)  # hides text as it's typed
        self.entry_password.setStyleSheet(self.get_entry_stylesheet())  # Sest styles for the password input
        layout.addWidget(self.entry_password)  # Adds the password input to the layout

        # Retype password input field
        self.label_retype_password = QLabel('Retype password', self)
        layout.addWidget(self.label_retype_password)  # Adds tge retype password label to the layout
        self.entry_retype_password = QLineEdit(self)
        self.entry_retype_password.setEchoMode(QLineEdit.Password)  # Hides text as it's typed
        self.entry_retype_password.setStyleSheet(
            self.get_entry_stylesheet())  # sets styles for the retype password input
        layout.addWidget(self.entry_retype_password)  # Adds the retype password input to the layout

        # create account button
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Adds space to the left
        self.button_create_account = QPushButton('Create account', self)
        self.button_create_account.setStyleSheet(self.get_button_stylesheet())  # Sets styles for the button
        self.button_create_account.setFixedWidth(200)  # Sets width on button
        self.button_create_account.clicked.connect(
            self.create_account)  # Connects button click to create_account method
        button_layout.addWidget(self.button_create_account)  # adds the button to the layout
        button_layout.addStretch()  # Adds space to the right

        layout.addLayout(button_layout)  # Adds button layout to the "main layout"

        main_layout.addLayout(layout)  # Adds form layout to the "main layout"
        self.setLayout(main_layout)  # sets the "main layout"

    def center(self):
        # Center the window on the screen
        qr = self.frameGeometry()  # gets the frame figures
        cp = QDesktopWidget().availableGeometry().center()  # gets the screen center
        qr.moveCenter(cp)  # Moves the frame to the center
        self.move(qr.topLeft())  # Moves the window to the top left of the frame

    def get_entry_stylesheet(self):
        # Tge stylesheet for input fields
        return """
        QLineEdit {
            background-color: #ffffff;
            color: #000000;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        """

    def get_button_stylesheet(self):
        # the stylesheet for buttons
        return """
        QPushButton {
            background-color: #e39443;
            color: rgb(28, 37, 48);
            border-radius: 5px;
            padding: 5px 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #cf7a3a;
        }
        """

    def create_account(self):
        # Gets the values from the input fields
        username = self.entry_name.text()
        email = self.entry_email.text()
        password = self.entry_password.text()
        retype_password = self.entry_retype_password.text()

        # check if all fields are filled out
        if not username or not email or not password or not retype_password:
            QMessageBox.warning(self, "Error", "All fields must be filled out")  # Shows popup if any field is empty
            return

        # Check if the passwords match
        if password != retype_password:
            QMessageBox.warning(self, "Error", "Passwords do not match")  # Shows popup if passwords do not match
            return

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # This is the SQL bit that was supposed to work. But I didn't have enough time to make it work.

        # try:
        #     conn = mysql.connector.connect(
        #         host='localhost',
        #         user='root',
        #         password='Timerbest123!',
        #         database='accounts_login'
        #     )
        #     cursor = conn.cursor()
        #     cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        #                    (username, email, hashed_password))
        #     conn.commit()
        #     cursor.close()
        #     conn.close()

        #     print(f"User created: {username}, {email}, {hashed_password}")
        #     QMessageBox.information(self, "Success", "Account created")
        # except mysql.connector.Error as err:
        #     QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {err}")
        #     return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegisterForm()
    form.show()
    sys.exit(app.exec_())