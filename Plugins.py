import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
                             QProgressBar, QComboBox, QWidget, QLabel, QTreeWidget, QTreeWidgetItem, QLineEdit,
                             QFileDialog, QCheckBox, QTextEdit, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
import subprocess


class Worker(QThread):
    result_ready = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            result = subprocess.run(self.command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            filtered_stdout = self.filter_progress_lines(result.stdout)
            filtered_stderr = self.filter_progress_lines(result.stderr)
            self.result_ready.emit(f"Output:\n{filtered_stdout}\nError:\n{filtered_stderr}")
        except subprocess.CalledProcessError as e:
            filtered_stderr = self.filter_progress_lines(e.stderr)
            self.result_ready.emit(f"Error running command {self.command}: {e}\n{filtered_stderr}")

    def filter_progress_lines(self, text):
        lines = text.splitlines()
        filtered_lines = [line for line in lines if not line.startswith("Progress:")]
        return "\n".join(filtered_lines)


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
        self.search_bar.textChanged.connect(self.filter_plugins)
        self.search_layout.addWidget(self.search_bar)
        self.sidebar_layout.addLayout(self.search_layout)

        # Combobox for All Plugins and Favorites
        self.favorites_combobox = QComboBox(self)
        self.favorites_combobox.addItem("All Plugins")
        self.favorites_combobox.addItem("Favorites")
        self.favorites_combobox.currentIndexChanged.connect(self.change_plugin_list)
        self.sidebar_layout.addWidget(self.favorites_combobox)

        # Plugins list for All Plugins
        self.plugins_list = QTreeWidget(self)
        self.plugins_list.setHeaderHidden(True)
        self.sidebar_layout.addWidget(self.plugins_list)

        self.add_plugins()

        # Plugins list for Favorites
        self.favorites_list = QTreeWidget(self)
        self.favorites_list.setHeaderHidden(True)
        self.favorites_list.hide()
        self.sidebar_layout.addWidget(self.favorites_list)

        # Track which plugins are in favorites
        self.favorites = set()

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

        # Analyze Button
        self.analyze_button = QPushButton("Analyze", self)
        self.analyze_button.setVisible(False)
        self.analyze_button.clicked.connect(self.analyze_memory_dump)
        self.content_layout.addWidget(self.analyze_button)

        # Output TextEdit for displaying Volatility results
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setReadOnly(True)
        self.output_text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.content_layout.addWidget(self.output_text_edit)

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
            QTextEdit {
                background-color: #333;
                color: white;
                border: none;
                padding: 10px;
            }
        """)

    def add_plugins(self):
        self.plugin_items = []  # Store references to all plugin items for easy access
        self.parent_items = []  # Store references to parent items

        processes_item = QTreeWidgetItem(self.plugins_list)
        processes_item.setText(0, "Processes and Threads")
        self.parent_items.append(processes_item)

        for sub_item in ["windows.pslist.PsList", "windows.psscan.PsScan", "windows.threads.Threads",
                         "windows.ldrmodules.LdrModules"]:
            self.add_plugin_item(processes_item, sub_item)

        file_system_item = QTreeWidgetItem(self.plugins_list)
        file_system_item.setText(0, "File system")
        self.parent_items.append(file_system_item)

        for sub_item in ["windows.filescan.FileScan", "windows.dumpfiles.DumpFiles", "windows.envars.Envars"]:
            self.add_plugin_item(file_system_item, sub_item)

        network_item = QTreeWidgetItem(self.plugins_list)
        network_item.setText(0, "Network")
        self.parent_items.append(network_item)

        for sub_item in ["windows.netscan.NetScan", "windows.connections.Connections", "windows.sockets.Sockets"]:
            self.add_plugin_item(network_item, sub_item)

        registry_item = QTreeWidgetItem(self.plugins_list)
        registry_item.setText(0, "Registry")
        self.parent_items.append(registry_item)

        for sub_item in ["windows.printkey.PrintKey", "windows.hivelist.HiveList", "windows.userassist.UserAssist"]:
            self.add_plugin_item(registry_item, sub_item)

        memory_item = QTreeWidgetItem(self.plugins_list)
        memory_item.setText(0, "Memory and Handles")
        self.parent_items.append(memory_item)

        for sub_item in ["windows.handles.Handles", "windows.dlllist.DllList", "windows.malfind.Malfind"]:
            self.add_plugin_item(memory_item, sub_item)

        system_info_item = QTreeWidgetItem(self.plugins_list)
        system_info_item.setText(0, "System Information")
        self.parent_items.append(system_info_item)

        for sub_item in ["windows.imageinfo.ImageInfo", "windows.kdbgscan.KdbgScan", "windows.info.Info"]:
            self.add_plugin_item(system_info_item, sub_item)

    def add_plugin_item(self, parent_item, plugin_name):
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(0, 0, 0, 0)
        item_label = QLabel(plugin_name)
        item_layout.addWidget(item_label)
        checkbox = QCheckBox(self)
        item_layout.addWidget(checkbox)

        # Add heart button for favorites
        heart_button = QPushButton("❤️")
        heart_button.setFlat(True)
        heart_button.setStyleSheet("color: white;")
        heart_button.clicked.connect(lambda: self.toggle_favorite(plugin_name, heart_button, checkbox))
        item_layout.addWidget(heart_button)

        item_widget.setLayout(item_layout)

        tree_item = QTreeWidgetItem(parent_item)
        self.plugins_list.setItemWidget(tree_item, 0, item_widget)
        self.plugin_items.append((plugin_name, checkbox))

    def filter_plugins(self, text):
        text = text.lower()
        for parent_item in self.parent_items:
            parent_item.setHidden(True)
            parent_has_visible_child = False
            for i in range(parent_item.childCount()):
                child_item = parent_item.child(i)
                widget = self.plugins_list.itemWidget(child_item, 0)
                label = widget.findChild(QLabel)
                if text in label.text().lower():
                    child_item.setHidden(False)
                    parent_item.setHidden(False)
                    parent_item.setExpanded(True)
                    parent_has_visible_child = True
                else:
                    child_item.setHidden(True)
            parent_item.setHidden(not parent_has_visible_child)

    def change_plugin_list(self, index):
        if index == 0:  # All Plugins
            self.favorites_list.hide()
            self.plugins_list.show()
        else:  # Favorites
            self.plugins_list.hide()
            self.favorites_list.show()

    def toggle_favorite(self, plugin_name, button, original_checkbox):
        if plugin_name in self.favorites:
            self.remove_from_favorites(plugin_name)
            button.setText("❤️")
        else:
            self.add_to_favorites(plugin_name, original_checkbox)
            button.setText("💔")

    def add_to_favorites(self, plugin_name, original_checkbox):
        if plugin_name not in self.favorites:
            self.favorites.add(plugin_name)
            favorite_item = QTreeWidgetItem(self.favorites_list)

            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_label = QLabel(plugin_name)
            item_layout.addWidget(item_label)
            checkbox = QCheckBox(self)
            checkbox.setChecked(original_checkbox.isChecked())
            item_layout.addWidget(checkbox)

            # Add heart button for removal from favorites
            heart_button = QPushButton("💔")
            heart_button.setFlat(True)
            heart_button.setStyleSheet("color: white;")
            heart_button.clicked.connect(lambda: self.toggle_favorite(plugin_name, heart_button, checkbox))
            item_layout.addWidget(heart_button)

            item_widget.setLayout(item_layout)
            self.favorites_list.setItemWidget(favorite_item, 0, item_widget)

            self.plugin_items.append((plugin_name, checkbox))

    def remove_from_favorites(self, plugin_name):
        if plugin_name in self.favorites:
            self.favorites.remove(plugin_name)
            root = self.favorites_list.invisibleRootItem()
            for i in range(root.childCount()):
                child = root.child(i)
                if child.text(0) == plugin_name:
                    root.removeChild(child)
                    break

            self.plugin_items = [(name, checkbox) for name, checkbox in self.plugin_items if name != plugin_name]

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Memory Dumps (*.mem)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            self.file_path = file_dialog.selectedFiles()[0]
            print(f"Selected file: {self.file_path}")
            self.analyze_button.setVisible(True)

    def analyze_memory_dump(self):
        selected_plugins = [plugin_name for plugin_name, checkbox in self.plugin_items if checkbox.isChecked()]
        if not selected_plugins:
            print("No plugins selected.")
            self.output_text_edit.append("No plugins selected.")
            return

        vol_path = "./volatility3/vol.py"  # Full path to vol.py
        for plugin in selected_plugins:
            print(f"Analyzing with plugin: {plugin}")
            self.output_text_edit.append(f"Analyzing with plugin: {plugin}")
            command = ["python", vol_path, "-f", self.file_path, plugin]
            self.worker = Worker(command)
            self.worker.result_ready.connect(self.display_result)
            self.worker.start()

    def display_result(self, result):
        self.output_text_edit.clear()
        self.output_text_edit.append(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
