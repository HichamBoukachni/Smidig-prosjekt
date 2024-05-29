import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # User icon
        user_icon = QLabel(self)
        user_pixmap = QPixmap(r'C:\users\hicha\Downloads\userAvatarwhite.png')  # Update path
        user_pixmap = user_pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        user_icon.setPixmap(user_pixmap)
        user_icon.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(user_icon)

        # Email input
        email_input = QLineEdit(self)
        email_input.setPlaceholderText("email@domain.com")
        email_input.setFixedHeight(40)
        email_input.setStyleSheet("background-color: #444; color: white; padding: 10px; border: none;")
        main_layout.addWidget(email_input)

        # Password input
        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password...")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setFixedHeight(40)
        password_input.setStyleSheet("background-color: #444; color: white; padding: 10px; border: none;")
        main_layout.addWidget(password_input)

        # Sign in button
        sign_in_button = QPushButton("Sign in", self)
        sign_in_button.setFixedHeight(40)
        sign_in_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6600; 
                color: white; 
                border: none;
                margin-top: 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #FF3300;
            }
        """)
        main_layout.addWidget(sign_in_button)

        # Sign up link
        sign_up_label = QLabel("Create an account")
        sign_up_label.setStyleSheet("color: white;")
        sign_up_label.setFont(QFont('Arial', 12))
        sign_up_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(sign_up_label)

        sign_up_desc = QLabel("Enter your email to sign up for this app")
        sign_up_desc.setStyleSheet("color: gray;")
        sign_up_desc.setFont(QFont('Arial', 10))
        sign_up_desc.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(sign_up_desc)

        sign_up_button = QPushButton("Sign up with email", self)
        sign_up_button.setFixedHeight(40)
        sign_up_button.setStyleSheet("""
            QPushButton {
                background-color: transparent; 
                color: #FF6600; 
                border: 2px solid #FF6600;
                margin-top: 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #FF6600;
                color: white;
            }
        """)
        main_layout.addWidget(sign_up_button)

        self.setLayout(main_layout)
        self.setWindowTitle('Login')
        self.setGeometry(600, 300, 400, 500)
        self.setStyleSheet("background-color: #2b2b2b;")


def show_login():
    login = LoginWindow()
    login.show()
    return login
