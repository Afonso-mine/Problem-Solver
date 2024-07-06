import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QDialog

def open_html_file(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'html', filename)
    webbrowser.open_new_tab(f'file://{file_path}')

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the support! Select one of the options below:")
        layout.addWidget(welcome_label)

        hardware_button = QPushButton("1 - Hardware", self)
        hardware_button.clicked.connect(self.show_hardware_options)
        layout.addWidget(hardware_button)

        software_button = QPushButton("2 - Software", self)
        software_button.clicked.connect(self.show_software_options)
        layout.addWidget(software_button)

        self.setLayout(layout)
        self.setWindowTitle('Support')
        self.show()

    def show_hardware_options(self):
        self.hardware_dialog = HardwareDialog()
        self.hardware_dialog.exec_()

    def show_software_options(self):
        self.software_dialog = SoftwareDialog()
        self.software_dialog.exec_()

class HardwareDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Select one of the options")
        layout.addWidget(label)

        self.hardware_group = QButtonGroup(self)

        options = [
            ("Storage", 1),
            ("Motherboard", 2),
            ("CPU", 3),
            ("GPU", 4),
            ("Keyboard", 5),
            ("Touchpad", 6)
        ]

        for text, value in options:
            radio_button = QRadioButton(text, self)
            self.hardware_group.addButton(radio_button, value)
            layout.addWidget(radio_button)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.on_hardware_selected)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('Hardware Support')

    def on_hardware_selected(self):
        selected = self.hardware_group.checkedId()
        if selected == 1:
            self.show_storage_options()
        elif selected == 2:
            open_html_file('H2.html')
        elif selected == 3:
            open_html_file('H3.html')
        elif selected == 4:
            open_html_file('H4.html')
        elif selected == 5:
            open_html_file('H5.html')
        elif selected == 6:
            open_html_file('H6.html')
        self.close()

    def show_storage_options(self):
        self.storage_dialog = StorageDialog()
        self.storage_dialog.exec_()

class StorageDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Select the storage type")
        layout.addWidget(label)

        self.storage_group = QButtonGroup(self)

        options = [
            ("SSD", 1),
            ("HDD", 2)
        ]

        for text, value in options:
            radio_button = QRadioButton(text, self)
            self.storage_group.addButton(radio_button, value)
            layout.addWidget(radio_button)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.on_storage_selected)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('Storage Type')

    def on_storage_selected(self):
        selected = self.storage_group.checkedId()
        if selected == 1:
            open_html_file('H1-1.html')
        elif selected == 2:
            open_html_file('H1-2.html')
        self.close()

class SoftwareDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Please select the software")
        layout.addWidget(label)

        self.software_group = QButtonGroup(self)

        options = [
            ("Windows", 1),
            ("Linux", 2)
        ]

        for text, value in options:
            radio_button = QRadioButton(text, self)
            self.software_group.addButton(radio_button, value)
            layout.addWidget(radio_button)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.on_software_selected)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('Software Support')

    def on_software_selected(self):
        selected = self.software_group.checkedId()
        if selected == 1:
            open_html_file('S1.html')
        elif selected == 2:
            self.show_linux_options()
        self.close()

    def show_linux_options(self):
        self.linux_dialog = LinuxDialog()
        self.linux_dialog.exec_()

class LinuxDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Select your distro")
        layout.addWidget(label)

        self.linux_group = QButtonGroup(self)

        options = [
            ("Debian", 1),
            ("Linux 2.4 (up)", 2)
        ]

        for text, value in options:
            radio_button = QRadioButton(text, self)
            self.linux_group.addButton(radio_button, value)
            layout.addWidget(radio_button)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.on_linux_selected)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle('Linux Distro')

    def on_linux_selected(self):
        selected = self.linux_group.checkedId()
        if selected == 1:
            open_html_file('S2-1.html')
        elif selected == 2:
            open_html_file('S2-2.html')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
