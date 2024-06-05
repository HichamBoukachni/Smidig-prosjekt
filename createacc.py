import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QFrame, QDesktopWidget)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import bcrypt  # Import bcrypt for password hashing
import mysql.connector  # Import MySQL connector to connect to the database

# Define the RegisterForm class, inheriting from QWidget
class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Call the method to initialize the UI

    def initUI(self):
        self.setWindowTitle('Opprett konto')  # Set the window title
        self.setFixedSize(400, 500)  # Set a fixed window size
        self.setStyleSheet('background-color: #2c2f38; color: #ffffff;')  # Set background and text color
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window title bar

        self.center()  # Center the window upon initialization

        main_layout = QVBoxLayout()  # Create the main vertical layout

        top_layout = QHBoxLayout()  # Create a horizontal layout for the top section

        # Gray box without back button
        self.back_box = QLabel(self)
        back_pixmap = QPixmap(50, 50)
        back_pixmap.fill(Qt.gray)  # Placeholder color for the back box
        self.back_box.setPixmap(back_pixmap)
        self.back_box.setAlignment(Qt.AlignCenter)  # Center align the box

        top_layout.addStretch()  # Add stretchable space to the left
        top_layout.addWidget(self.back_box)  # Add the back box widget

        main_layout.addLayout(top_layout)  # Add the top layout to the main layout

        layout = QVBoxLayout()  # Create another vertical layout for form elements

        # Profile picture icon
        self.profile_icon = QLabel(self)
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.gray)  # Placeholder color for the profile picture
        self.profile_icon.setPixmap(pixmap)
        self.profile_icon.setAlignment(Qt.AlignCenter)  # Center align the icon
        layout.addWidget(self.profile_icon)
        layout.addSpacing(40)  # Increased vertical spacing

        # Horizontal line
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)  # Set the frame shape to horizontal line
        self.line.setFrameShadow(QFrame.Sunken)  # Set the frame shadow
        self.line.setStyleSheet("color: #D96F33; background-color: #D96F33;")  # Set line color
        layout.addWidget(self.line)

        # Your name
        self.label_name = QLabel('Your name', self)
        layout.addWidget(self.label_name)
        self.entry_name = QLineEdit(self)
        self.entry_name.setStyleSheet(self.get_entry_stylesheet())  # Apply stylesheet to entry
        layout.addWidget(self.entry_name)

        # Email address
        self.label_email = QLabel('Email address', self)
        layout.addWidget(self.label_email)
        self.entry_email = QLineEdit(self)
        self.entry_email.setStyleSheet(self.get_entry_stylesheet())  # Apply stylesheet to entry
        layout.addWidget(self.entry_email)

        # Create password
        self.label_password = QLabel('Create password', self)
        layout.addWidget(self.label_password)
        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)  # Set echo mode to password
        self.entry_password.setStyleSheet(self.get_entry_stylesheet())  # Apply stylesheet to entry
        layout.addWidget(self.entry_password)

        # Retype password
        self.label_retype_password = QLabel('Retype password', self)
        layout.addWidget(self.label_retype_password)
        self.entry_retype_password = QLineEdit(self)
        self.entry_retype_password.setEchoMode(QLineEdit.Password)  # Set echo mode to password
        self.entry_retype_password.setStyleSheet(self.get_entry_stylesheet())  # Apply stylesheet to entry
        layout.addWidget(self.entry_retype_password)

        # Create account button with centered alignment
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Add stretchable space to the left
        self.button_create_account = QPushButton('Create account', self)
        self.button_create_account.setStyleSheet(self.get_button_stylesheet())  # Apply stylesheet to button
        self.button_create_account.setFixedWidth(200)  # Half the width of the form
        self.button_create_account.clicked.connect(self.create_account)  # Connect button click to create_account method
        button_layout.addWidget(self.button_create_account)
        button_layout.addStretch()  # Add stretchable space to the right

        layout.addLayout(button_layout)  # Add button layout to the main layout

        main_layout.addLayout(layout)  # Add form layout to the main layout
        self.setLayout(main_layout)  # Set the main layout

    def center(self):
        # Center the window on the screen
        qr = self.frameGeometry()  # Get the frame geometry
        cp = QDesktopWidget().availableGeometry().center()  # Get the center point of the screen
        qr.moveCenter(cp)  # Move the frame geometry to the center
        self.move(qr.topLeft())  # Move the window to the top left position of the frame geometry

    def get_entry_stylesheet(self):
        # Return the stylesheet for QLineEdit entries
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
        # Return the stylesheet for QPushButton
        return """
        QPushButton {
            background-color: #e39443;
            color: #ffffff;
            border-radius: 5px;
            padding: 5px 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #cf7a3a;
        }
        """

    def create_account(self):
        # Get the values from the input fields
        username = self.entry_name.text()
        email = self.entry_email.text()
        password = self.entry_password.text()
        retype_password = self.entry_retype_password.text()

        # Check if all fields are filled out
        if not username or not email or not password or not retype_password:
            QMessageBox.warning(self, "Feil", "Alle felt må fylles ut")  # Show warning if any field is empty
            return

        # Check if the passwords match
        if password != retype_password:
            QMessageBox.warning(self, "Feil", "Passordene stemmer ikke overens")  # Show warning if passwords do not match
            return

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Save user to database
        try:
            conn = mysql.connector.connect(
                host='localhost',  # Database host
                user='root',  # Replace with your MySQL username
                password='Timerbest123!',  # Replace with your MySQL password
                database='accounts_login'  # Database name
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))  # Execute the SQL query to insert the new user
            conn.commit()  # Commit the transaction
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection

            print(f"Bruker opprettet: {username}, {email}, {hashed_password}")  # Print user details to console
            QMessageBox.information(self, "Suksess", "Konto opprettet")  # Show success message
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Databasefeil", f"Kunne ikke koble til databasen: {err}")  # Show error message if database connection fails
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    form = RegisterForm()  # Create an instance of RegisterForm
    form.show()  # Show the register form
    sys.exit(app.exec_())  # Execute the application
