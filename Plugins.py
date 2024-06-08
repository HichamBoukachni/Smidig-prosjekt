import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
                             QProgressBar, QComboBox, QWidget, QLabel, QTreeWidget, QTreeWidgetItem, QLineEdit,
                             QFileDialog, QCheckBox, QTextEdit, QSizePolicy, QSplitter, QFrame)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QProcess

class Worker(QThread):
    result_ready = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        process = QProcess()
        process.setProcessChannelMode(QProcess.MergedChannels)
        process.start(' '.join(self.command))

        total_lines = 0
        output = ""
        while process.waitForReadyRead():
            output += process.readAll().data().decode()
            total_lines += 1
            progress_percentage = min(100, int((total_lines / 100.0) * 100))
            self.progress.emit(progress_percentage)

        process.waitForFinished()
        self.result_ready.emit(output)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.translations = {
            'current_language': 'English',
            'data_field': {'English': 'Data Field', 'Norwegian': 'Datafelt'},
            'result_window_title': {'English': 'Result Window', 'Norwegian': 'Resultatvindu'},
            'results_for_plugin': {'English': 'Results for plugin', 'Norwegian': 'Resultater for plugin'},
            'close_button': {'English': 'Close', 'Norwegian': 'Lukk'},
            'view_result_button': {'English': 'View Result', 'Norwegian': 'Vis Resultat'},
            'executing_plugin': {'English': 'Executing plugin', 'Norwegian': 'Utfører plugin'},
            'info': {'English': 'INFO', 'Norwegian': 'INFO'},
            'initializing': {'English': 'Initializing', 'Norwegian': 'Initialiserer'},
            'listing_processes': {'English': 'Listing processes', 'Norwegian': 'Lister prosesser'},
            'scanning_files': {'English': 'Scanning files', 'Norwegian': 'Skanner filer'},
            'found_file': {'English': 'Found file', 'Norwegian': 'Funnet fil'},
            'scanning_network': {'English': 'Scanning network', 'Norwegian': 'Skanner nettverk'},
            'ip_address': {'English': 'IP Address', 'Norwegian': 'IP-adresse'},
            'port': {'English': 'Port', 'Norwegian': 'Port'},
            'running': {'English': 'Running', 'Norwegian': 'Kjører'},
            'no_specific_output': {'English': 'No specific output for plugin',
                                   'Norwegian': 'Ingen spesifikk output for plugin'},
            'plugin_execution_completed': {'English': 'Plugin execution completed',
                                           'Norwegian': 'Pluginutførelse fullført'},
            'pid': {'English': 'PID', 'Norwegian': 'PID'},
            'name': {'English': 'Name', 'Norwegian': 'Navn'},
            'favorites': {'English': 'Favorites', 'Norwegian': 'Favoritter'},
            'processes_and_threads': {'English': 'Processes and Threads', 'Norwegian': 'Prosesser og Tråder'},
            'file_system': {'English': 'File system', 'Norwegian': 'Filsystem'},
            'network': {'English': 'Network', 'Norwegian': 'Nettverk'},
            'registry': {'English': 'Registry', 'Norwegian': 'Register'},
            'memory_and_handles': {'English': 'Memory and Handles', 'Norwegian': 'Minne og Håndtak'},
            'system_information': {'English': 'System Information', 'Norwegian': 'Systeminformasjon'},
            'search': {'English': 'Search', 'Norwegian': 'Søk'},
            'analyze_button': {'English': 'Analyze', 'Norwegian': 'Analyser'},
            'all_plugins': {'English': 'All Plugins', 'Norwegian': 'Alle Plugins'},
        }

        self.setWindowTitle(self.translations['data_field'][self.translations['current_language']])
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
        search_pixmap = QPixmap("images/_search.png")
        scaled_pixmap = search_pixmap.scaled(14, 14)
        self.search_icon.setPixmap(scaled_pixmap)
        self.search_layout.addWidget(self.search_icon)
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText(self.translations['search'][self.translations['current_language']])
        self.search_bar.setObjectName("search_bar")
        self.search_bar.textChanged.connect(self.filter_plugins)
        self.search_layout.addWidget(self.search_bar)
        self.sidebar_layout.addLayout(self.search_layout)

        # Combobox for All Plugins and Favorites
        self.favorites_combobox = QComboBox(self)
        self.favorites_combobox.addItem(self.translations['all_plugins'][self.translations['current_language']])
        self.favorites_combobox.addItem(self.translations['favorites'][self.translations['current_language']])
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

        # Placeholder Image/Icon Button
        self.upload_button = QPushButton(self)
        self.upload_button.setIconSize(QSize(185, 185))  # Making the icon three times larger
        self.upload_button.setFlat(True)
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.upload_button.setObjectName("upload_button")

        self.upload_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.upload_button.setMinimumHeight(182)
        self.sidebar_layout.addWidget(self.upload_button, alignment=Qt.AlignBottom)
        self.setLayout(self.sidebar_layout)

        # Main content area
        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.content_layout, 4)

        # Language selection
        self.language_combobox = QComboBox(self)
        self.language_combobox.addItem("English")
        self.language_combobox.addItem("Norwegian")
        self.language_combobox.currentIndexChanged.connect(self.change_language)
        self.content_layout.addWidget(self.language_combobox)

        # Progress Bar
        self.progress_bar_layout = QHBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)  # Reset progress
        self.progress_bar_layout.addWidget(self.progress_bar)

        # Control buttons next to progress bar
        self.view_result_button = QPushButton(
            self.translations['view_result_button'][self.translations['current_language']], self)
        self.view_result_button.setObjectName("view_result_button")
        self.progress_bar_layout.addWidget(self.view_result_button)

        # Add the button with icon
        self.back_button = QPushButton(self)
        icon_path = "images/_navarrowleft.png"
        self.back_button.setIcon(QIcon(icon_path))
        icon_size = 32  # Adjust the size to make the icon smaller
        self.back_button.setIconSize(QSize(icon_size, icon_size))
        self.back_button.setFixedSize(icon_size + 10, icon_size + 10)  # Add some padding around the icon
        self.back_button.setStyleSheet("background-color: transparent; border: none;")
        self.progress_bar_layout.addWidget(self.back_button)
        # Connect the button click to the function
        self.back_button.clicked.connect(self.back_button_clicked)

        # Adding progress_bar_layout to content_layout
        self.content_layout.addLayout(self.progress_bar_layout)

        # Analyze Button
        self.analyze_button = QPushButton(self.translations['analyze_button'][self.translations['current_language']], self)
        self.analyze_button.setVisible(False)
        self.analyze_button.clicked.connect(self.analyze_memory_dump)
        self.analyze_button.setObjectName("analyze_button")
        self.content_layout.addWidget(self.analyze_button)

        # Result Area
        self.result_area = QWidget()
        self.result_layout = QVBoxLayout(self.result_area)
        self.content_layout.addWidget(self.result_area)

        # Output TextEdit for displaying Volatility results
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setReadOnly(True)
        self.output_text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.result_layout.addWidget(self.output_text_edit)  # Endret fra content_layout til result_layout


        # Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgb(28, 37, 48);
            }
            QLabel {
                color: rgb(163, 174, 186);
            }
            QComboBox, QLineEdit {
                color: rgb(42, 53, 65);
                background-color: rgb(255, 255, 255);
                border-radius: 7px;
                margin-top: 5px;
            }
            QComboBox::drop-down {
                border-radius: 10px; 
                width: 40%;
            }
            QComboBox::down-arrow {
                image: url(images/_arrowdownO.png);
                max-width: 150%; 
                max-height: 150%;
            }
            QPushButton {
                color: white;
                border: none;
                padding: 10px;
            }
            QPushButton#upload_button {
                background-color: rgb(42, 53, 65);
                margin-bottom: 10px;
                padding: 20px;
                border-radius: 10px;
                image: url("images/_uploadorange.png");
            }
            QPushButton#view_result_button {
                background-color: rgb(42, 53, 65);
                border-style: solid;
                border-color: rgb(217, 111, 51);
                border-radius: 10px;
            }
            QPushButton:hover#upload_button {
                image: url(images/_uploadorangehover.png);
            }
            QPushButton:hover#view_result_button {
                background-color: rgb(64, 81, 99);
            }
            QPushButton#analyze_button {
                margin-top: 1px;
                margin-left: 10px;
                margin-right: 10px;
                background-color: rgb(42, 53, 65);
                font-size: 17px;
                color: white;
            }
            QProgressBar {
                background-color: rgb(217, 111, 51);
                color: white;
                text-align: center;
                margin-left: 10px;
            }
            QTreeWidget {
                background-color: rgb(42, 53, 65);
                color: white; 
                border-radius: 10px;
                margin-top: 10px;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QTreeWidget::item:selected {
                background-color: rgb(42, 53, 65);
                color: white;
            }
            QTextEdit {
                background-color: rgb(42, 53, 65);
                color: white;
                border: solid;
                border-color: rgb(217, 111, 51);
                border-width: 2px;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.vol_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'volatility3', 'vol.py')

    def add_plugins(self):
        self.plugin_items = {}  # Use a dictionary to store references to all plugin items for easy access
        self.parent_items = []  # Store references to parent items

        processes_item = QTreeWidgetItem(self.plugins_list)
        processes_item.setText(0, self.translations['processes_and_threads'][self.translations['current_language']])
        self.parent_items.append(processes_item)

        for sub_item in ["windows.pslist.PsList", "windows.psscan.PsScan", "windows.thrdscan.ThrdScan",
                         "windows.ldrmodules.LdrModules"]:
            self.add_plugin_item(processes_item, sub_item)

        file_system_item = QTreeWidgetItem(self.plugins_list)
        file_system_item.setText(0, self.translations['file_system'][self.translations['current_language']])
        self.parent_items.append(file_system_item)

        for sub_item in ["windows.filescan.FileScan", "windows.dumpfiles.DumpFiles", "windows.envars.Envars"]:
            self.add_plugin_item(file_system_item, sub_item)

        network_item = QTreeWidgetItem(self.plugins_list)
        network_item.setText(0, self.translations['network'][self.translations['current_language']])
        self.parent_items.append(network_item)

        for sub_item in ["windows.netscan.NetScan", "windows.netstat.NetStat"]:
            self.add_plugin_item(network_item, sub_item)

        registry_item = QTreeWidgetItem(self.plugins_list)
        registry_item.setText(0, self.translations['registry'][self.translations['current_language']])
        self.parent_items.append(registry_item)

        for sub_item in ["windows.printkey.PrintKey", "windows.registry.hivelist.HiveList",
                         "windows.registry.certificates.Certificates"]:
            self.add_plugin_item(registry_item, sub_item)

        memory_item = QTreeWidgetItem(self.plugins_list)
        memory_item.setText(0, self.translations['memory_and_handles'][self.translations['current_language']])
        self.parent_items.append(memory_item)

        for sub_item in ["windows.handles.Handles", "windows.dlllist.DllList", "windows.malfind.Malfind",
                         "windows.memmap.Memmap"]:
            self.add_plugin_item(memory_item, sub_item)

        system_info_item = QTreeWidgetItem(self.plugins_list)
        system_info_item.setText(0, self.translations['system_information'][self.translations['current_language']])
        self.parent_items.append(system_info_item)

        for sub_item in ["windows.info.Info", "windows.imageinfo.ImageInfo", "windows.kdbgscan.KdbgScan"]:
            self.add_plugin_item(system_info_item, sub_item)

        # Legger til flere Vol3 plugins
        kernel_item = QTreeWidgetItem(self.plugins_list)
        kernel_item.setText(0, "Kernel")
        self.parent_items.append(kernel_item)

        for sub_item in ["windows.modules.Modules", "windows.ssdt.SSDT"]:
            self.add_plugin_item(kernel_item, sub_item)

        time_analysis_item = QTreeWidgetItem(self.plugins_list)
        time_analysis_item.setText(0, "Time Analysis")
        self.parent_items.append(time_analysis_item)

        for sub_item in ["windows.timeliner.Timeliner"]:
            self.add_plugin_item(time_analysis_item, sub_item)

        additional_features_item = QTreeWidgetItem(self.plugins_list)
        additional_features_item.setText(0, "Additional Features")
        self.parent_items.append(additional_features_item)

        for sub_item in ["windows.volshell.Volshell", "yarascan.YaraScan"]:
            self.add_plugin_item(additional_features_item, sub_item)

    def add_plugin_item(self, parent_item, plugin_name):
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(0, 0, 0, 0)
        item_layout.setSpacing(10)  # Ensure consistent spacing
        item_label = QLabel(plugin_name)
        item_label.setToolTip(plugin_name)
        item_label.setStyleSheet("QToolTip:hover { background-color: white; color: black; border: solid;}")
        item_layout.addWidget(item_label, alignment=Qt.AlignLeft)

        checkbox = QCheckBox(self)
        item_layout.addWidget(checkbox, alignment=Qt.AlignRight)

        # Add heart button for favorites
        heart_label = QLabel("🤍")
        heart_label.setFont(QFont("Arial", 12))  # Adjusted font size to 12px
        heart_label.mousePressEvent = lambda event, p=plugin_name: self.toggle_favorite(p, heart_label)
        item_layout.addWidget(heart_label, alignment=Qt.AlignRight)

        item_widget.setLayout(item_layout)

        tree_item = QTreeWidgetItem(parent_item)
        self.plugins_list.setItemWidget(tree_item, 0, item_widget)
        self.plugin_items[plugin_name] = {'checkbox': checkbox, 'heart_label': heart_label, 'tree_item': tree_item}

    def filter_plugins(self, text):
        text = text.lower()
        if not text:
            # Reset all items to their original state
            for parent_item in self.parent_items:
                parent_item.setHidden(False)
                parent_item.setExpanded(False)  # Or True, depending on your default state
                for i in range(parent_item.childCount()):
                    child_item = parent_item.child(i)
                    child_item.setHidden(False)
            return

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
            if parent_has_visible_child:
                parent_item.setExpanded(True)
            else:
                parent_item.setExpanded(False)

    def change_plugin_list(self, index):
        if index == 0:  # All Plugins
            self.favorites_list.hide()
            self.plugins_list.show()
        else:  # Favorites
            self.plugins_list.hide()
            self.favorites_list.show()

    def toggle_favorite(self, plugin_name, heart_label):
        if plugin_name in self.favorites:
            self.remove_from_favorites(plugin_name)
            heart_label.setText("🤍")
        else:
            self.add_to_favorites(plugin_name)
            heart_label.setText("🧡")

    def add_to_favorites(self, plugin_name):
        if plugin_name not in self.favorites:
            self.favorites.add(plugin_name)
            favorite_item = QTreeWidgetItem(self.favorites_list)

            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(10)  # Ensure consistent spacing
            item_label = QLabel(plugin_name)
            item_layout.addWidget(item_label, alignment=Qt.AlignLeft)

            checkbox = QCheckBox(self)
            item_layout.addWidget(checkbox, alignment=Qt.AlignRight)

            heart_label = QLabel("🧡")
            heart_label.setFont(QFont("Arial", 12))  # Adjusted font size to 12px
            heart_label.mousePressEvent = lambda event, p=plugin_name: self.toggle_favorite(p, heart_label)
            item_layout.addWidget(heart_label, alignment=Qt.AlignRight)

            item_widget.setLayout(item_layout)
            self.favorites_list.setItemWidget(favorite_item, 0, item_widget)

            self.plugin_items[plugin_name]['favorite_checkbox'] = checkbox
            self.plugin_items[plugin_name]['favorite_heart_label'] = heart_label

    def remove_from_favorites(self, plugin_name):
        if plugin_name in self.favorites:
            self.favorites.remove(plugin_name)
            root = self.favorites_list.invisibleRootItem()
            for i in range(root.childCount()):
                child = root.child(i)
                widget = self.favorites_list.itemWidget(child, 0)
                if widget:
                    label = widget.findChild(QLabel)
                    if label and label.text() == plugin_name:
                        root.removeChild(child)
                        break

            # Update the main list heart label
            if 'heart_label' in self.plugin_items[plugin_name]:
                self.plugin_items[plugin_name]['heart_label'].setText("🤍")

            del self.plugin_items[plugin_name]['favorite_checkbox']
            del self.plugin_items[plugin_name]['favorite_heart_label']

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Memory Dumps (*.mem *.raw *.dd *.bin *.dmp *.mdmp *.hiberfil.sys *.pagefile.sys *.vmem *.vmsn *.vmtm *.sav *.)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            self.file_path = file_dialog.selectedFiles()[0]
            print(f"Selected file: {self.file_path}")
            self.analyze_button.setVisible(True)

    def analyze_memory_dump(self):
        selected_plugins = [plugin_name for plugin_name, items in self.plugin_items.items() if items['checkbox'].isChecked()]
        if not selected_plugins:
            print("No plugins selected.")
            self.output_text_edit.append("No plugins selected.")
            return

        for plugin in selected_plugins:
            print(f"Analyzing with plugin: {plugin}")
            self.output_text_edit.append(f"Analyzing with plugin: {plugin}")
            command = ["python", self.vol_path, "-f", self.file_path, plugin]
            self.worker = Worker(command)
            self.worker.result_ready.connect(self.display_result)
            self.worker.progress.connect(self.update_progress)
            self.worker.start()

    def display_result(self, result):
        self.output_text_edit.clear()
        self.output_text_edit.append(result)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def back_button_clicked(self):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the target Python file
        target_file = os.path.join(current_dir, "StartSide(Christina).py")
        # subprocess.Popen(['python', target_file])
        # Bytt ut gjeldende prosess med StartSide.py
        os.execl(sys.executable, sys.executable, target_file)

    def change_language(self):
        self.translations['current_language'] = self.language_combobox.currentText()
        self.setWindowTitle(self.translations['data_field'][self.translations['current_language']])
        self.search_bar.setPlaceholderText(self.translations['search'][self.translations['current_language']])
        self.favorites_combobox.setItemText(0, self.translations['all_plugins'][self.translations['current_language']])
        self.favorites_combobox.setItemText(1, self.translations['favorites'][self.translations['current_language']])
        self.view_result_button.setText(self.translations['view_result_button'][self.translations['current_language']])
        self.analyze_button.setText(self.translations['analyze_button'][self.translations['current_language']])
        self.update_plugins_list()

    def update_plugins_list(self):
        self.plugins_list.clear()
        language = self.translations['current_language']

        processes_item = QTreeWidgetItem(self.plugins_list)
        processes_item.setText(0, self.translations['processes_and_threads'][language])
        self.parent_items.append(processes_item)

        for sub_item in ["windows.pslist.PsList", "windows.psscan.PsScan", "windows.thrdscan.ThrdScan",
                         "windows.ldrmodules.LdrModules"]:
            self.add_plugin_item(processes_item, sub_item)

        file_system_item = QTreeWidgetItem(self.plugins_list)
        file_system_item.setText(0, self.translations['file_system'][language])
        self.parent_items.append(file_system_item)

        for sub_item in ["windows.filescan.FileScan", "windows.dumpfiles.DumpFiles", "windows.envars.Envars"]:
            self.add_plugin_item(file_system_item, sub_item)

        network_item = QTreeWidgetItem(self.plugins_list)
        network_item.setText(0, self.translations['network'][language])
        self.parent_items.append(network_item)

        for sub_item in ["windows.netscan.NetScan", "windows.netstat.NetStat"]:
            self.add_plugin_item(network_item, sub_item)

        registry_item = QTreeWidgetItem(self.plugins_list)
        registry_item.setText(0, self.translations['registry'][language])
        self.parent_items.append(registry_item)

        for sub_item in ["windows.printkey.PrintKey", "windows.registry.hivelist.HiveList",
                         "windows.registry.certificates.Certificates"]:
            self.add_plugin_item(registry_item, sub_item)

        memory_item = QTreeWidgetItem(self.plugins_list)
        memory_item.setText(0, self.translations['memory_and_handles'][language])
        self.parent_items.append(memory_item)

        for sub_item in ["windows.handles.Handles", "windows.dlllist.DllList", "windows.malfind.Malfind",
                         "windows.memmap.Memmap"]:
            self.add_plugin_item(memory_item, sub_item)

        system_info_item = QTreeWidgetItem(self.plugins_list)
        system_info_item.setText(0, self.translations['system_information'][language])
        self.parent_items.append(system_info_item)

        for sub_item in ["windows.info.Info", "windows.imageinfo.ImageInfo", "windows.kdbgscan.KdbgScan"]:
            self.add_plugin_item(system_info_item, sub_item)

        # Legger til flere Vol3 plugins
        kernel_item = QTreeWidgetItem(self.plugins_list)
        kernel_item.setText(0, "Kernel")
        self.parent_items.append(kernel_item)

        for sub_item in ["windows.modules.Modules", "windows.ssdt.SSDT"]:
            self.add_plugin_item(kernel_item, sub_item)

        time_analysis_item = QTreeWidgetItem(self.plugins_list)
        time_analysis_item.setText(0, "Time Analysis")
        self.parent_items.append(time_analysis_item)

        for sub_item in ["windows.timeliner.Timeliner"]:
            self.add_plugin_item(time_analysis_item, sub_item)

        additional_features_item = QTreeWidgetItem(self.plugins_list)
        additional_features_item.setText(0, "Additional Features")
        self.parent_items.append(additional_features_item)

        for sub_item in ["windows.volshell.Volshell", "yarascan.YaraScan"]:
            self.add_plugin_item(additional_features_item, sub_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

