import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QInputDialog

class SupportApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Support App")

        layout = QVBoxLayout()

        self.intro_label = QLabel("Welcome to the support! Select one of the options below:")
        layout.addWidget(self.intro_label)

        self.main_combo = QComboBox()
        self.main_combo.addItem("Select an option", "")
        self.main_combo.addItem("Hardware", "hardware")
        self.main_combo.addItem("Software", "software")
        layout.addWidget(self.main_combo)

        self.sub_combo = QComboBox()
        layout.addWidget(self.sub_combo)

        self.show_button = QPushButton("Show Form")
        self.show_button.clicked.connect(self.show_form)
        layout.addWidget(self.show_button)

        self.setLayout(layout)

        self.main_combo.currentTextChanged.connect(self.update_sub_options)

    def update_sub_options(self, value):
        self.sub_combo.clear()
        if value == "Hardware":
            self.sub_combo.addItem("Select an option", "")
            self.sub_combo.addItem("Storage", "storage")
            self.sub_combo.addItem("Motherboard", "motherboard")
            self.sub_combo.addItem("CPU", "cpu")
            self.sub_combo.addItem("GPU", "gpu")
            self.sub_combo.addItem("Keyboard", "keyboard")
            self.sub_combo.addItem("Touchpad", "touchpad")
        elif value == "Software":
            self.sub_combo.addItem("Select an option", "")
            self.sub_combo.addItem("Windows", "windows")
            self.sub_combo.addItem("Linux", "linux")

    def show_form(self):
        main_option = self.main_combo.currentData()
        sub_option = self.sub_combo.currentData()

        if main_option == "hardware":
            if sub_option == "storage":
                self.show_storage_form()
            elif sub_option:
                self.open_html_file(f'H{self.sub_combo.currentIndex()}.html')

        elif main_option == "software":
            if sub_option:
                if sub_option == "linux":
                    self.show_linux_form()
                else:
                    self.open_html_file('S1.html')

    def show_storage_form(self):
        storage_type, ok = QInputDialog.getItem(self, "Select Storage Type", "Choose storage type:", ["SSD", "HDD"], 0, False)
        if ok and storage_type:
            if storage_type == "SSD":
                self.open_html_file('H1-1.html')
            elif storage_type == "HDD":
                self.open_html_file('H1-2.html')

    def show_linux_form(self):
        distro, ok = QInputDialog.getItem(self, "Select Linux Distro", "Choose your distro:", ["Debian", "Linux 2.4 (up)"], 0, False)
        if ok and distro:
            if distro == "Debian":
                self.open_html_file('S2-1.html')
            elif distro == "Linux 2.4 (up)":
                self.open_html_file('S2-2.html')

    def open_html_file(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'html', filename)
        webbrowser.open_new_tab(f'file://{file_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    support_app = SupportApp()
    support_app.show()
    sys.exit(app.exec_())
