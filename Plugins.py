import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
                             QProgressBar, QComboBox, QWidget, QLabel, QTreeWidget, QTreeWidgetItem, QLineEdit, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Field")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)

        # Left sidebar layout
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_layout.setAlignment(Qt.AlignTop)
        self.main_layout.addLayout(self.sidebar_layout, 1)

        # Search bar
        self.search_layout = QHBoxLayout()
        self.search_icon = QLabel(self)
        search_pixmap = QPixmap(32, 32)
        search_pixmap.fill(Qt.white)  # Placeholder for actual search icon
        self.search_icon.setPixmap(search_pixmap)
        self.search_layout.addWidget(self.search_icon)
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search")
        self.search_layout.addWidget(self.search_bar)
        self.sidebar_layout.addLayout(self.search_layout)

        # Combobox for Favorites and Categories
        self.favorites_combobox = QComboBox(self)
        self.favorites_combobox.addItem("Favorites")
        self.sidebar_layout.addWidget(self.favorites_combobox)

        # Plugins list
        self.plugins_list = QTreeWidget(self)
        self.plugins_list.setHeaderHidden(True)
        self.sidebar_layout.addWidget(self.plugins_list)

        processes_item = QTreeWidgetItem(self.plugins_list)
        processes_item.setText(0, "Processes and Threads")

        for sub_item in ["pslist", "psscan", "threads", "ldrmodules"]:
            child_item = QTreeWidgetItem(processes_item)
            child_item.setText(0, sub_item)

        file_system_item = QTreeWidgetItem(self.plugins_list)
        file_system_item.setText(0, "File system")

        for sub_item in ["filescan", "dumpfiles", "envars"]:
            child_item = QTreeWidgetItem(file_system_item)
            child_item.setText(0, sub_item)

        network_item = QTreeWidgetItem(self.plugins_list)
        network_item.setText(0, "Network")

        for sub_item in ["netscan", "connections", "sockets"]:
            child_item = QTreeWidgetItem(network_item)
            child_item.setText(0, sub_item)

        registry_item = QTreeWidgetItem(self.plugins_list)
        registry_item.setText(0, "Registry")

        for sub_item in ["printkey", "hivelist", "userassist"]:
            child_item = QTreeWidgetItem(registry_item)
            child_item.setText(0, sub_item)

        memory_item = QTreeWidgetItem(self.plugins_list)
        memory_item.setText(0, "Memory and Handles")

        for sub_item in ["handles", "dlllist", "malfind"]:
            child_item = QTreeWidgetItem(memory_item)
            child_item.setText(0, sub_item)

        system_info_item = QTreeWidgetItem(self.plugins_list)
        system_info_item.setText(0, "System Information")

        for sub_item in ["imageinfo", "kdbgscan", "info"]:
            child_item = QTreeWidgetItem(system_info_item)
            child_item.setText(0, sub_item)

        # Main content area
        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.content_layout, 4)

        # Progress Bar
        self.progress_bar_layout = QHBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(40)  # Example progress
        self.progress_bar_layout.addWidget(self.progress_bar)

        # Control buttons next to progress bar
        self.view_result_button = QPushButton("View Result", self)
        self.progress_bar_layout.addWidget(self.view_result_button)

        # Adding play, pause, and stop buttons with icons
        icon_size = 24
        self.play_button = QPushButton(self)
        self.play_button.setIcon(QIcon(QPixmap(icon_size, icon_size)))
        self.progress_bar_layout.addWidget(self.play_button)

        self.pause_button = QPushButton(self)
        self.pause_button.setIcon(QIcon(QPixmap(icon_size, icon_size)))
        self.progress_bar_layout.addWidget(self.pause_button)

        self.stop_button = QPushButton(self)
        self.stop_button.setIcon(QIcon(QPixmap(icon_size, icon_size)))
        self.progress_bar_layout.addWidget(self.stop_button)

        self.content_layout.addLayout(self.progress_bar_layout)

        # Placeholder Area
        self.placeholder = QLabel(self)
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setText("")
        self.content_layout.addWidget(self.placeholder, alignment=Qt.AlignCenter)

        # Placeholder Image/Icon Button
        self.upload_button = QPushButton(self)
        self.upload_button.setIcon(QIcon(r'C:\Users\hicha\Downloads\Upload orange.png'))
        self.upload_button.setIconSize(QSize(192, 192))  # Making the icon three times larger
        self.upload_button.setFlat(True)
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.placeholder_layout = QVBoxLayout(self.placeholder)
        self.placeholder_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)

        # Set placeholder size
        self.placeholder.setFixedHeight(self.height() - self.progress_bar.height() - 20)
        self.placeholder.setFixedWidth(self.width() - self.sidebar_layout.sizeHint().width() - 20)

        # Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: white;
            }
            QComboBox, QLineEdit {
                color: white;
                background-color: #333;
            }
            QPushButton {
                background-color: #444;
                color: white;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QProgressBar {
                background-color: #444;
                color: white;
                text-align: center;
            }
            QTreeWidget {
                background-color: #333;
                color: white;
                border: none;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QTreeWidget::item:selected {
                background-color: #555;
                color: white;
            }
        """)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            print(f"Selected file: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
