from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About")
        self.setGeometry(150, 150, 360, 390)
        self.setStyleSheet("background-color: #f4f6f7;")

        title = QLabel("About", self)
        title.setGeometry(147, 15, 100, 40)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1a5276;")

        self.image_label = QLabel(self)
        self.image_label.setGeometry(120, 65, 120, 120)
        self.image_label.setStyleSheet("border: 2px solid #aed6f1; border-radius: 10px; background-color: white;")
        pixmap = QPixmap("Pikachu.png")
        self.image_label.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        name_label = QLabel("Name: Leanne Buchnik", self)
        name_label.setGeometry(95, 205, 200, 30)
        name_label.setStyleSheet("font-size: 15px; font-weight: bold; color: #2c3e50;")

        email_label = QLabel("Email: leanne.buchnik@s.afeka.ac.il", self)
        email_label.setGeometry(62, 240, 260, 30)
        email_label.setStyleSheet("font-size: 14px; color: #34495e;")

        github_label = QLabel('<a href="https://github.com/Leanne08/Exersice4-icecream">My GitHub Repository</a>', self)
        github_label.setGeometry(107, 280, 180, 30)
        github_label.setStyleSheet("font-size: 14px;")
        github_label.setOpenExternalLinks(True)