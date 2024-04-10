from PyQt6.QtWidgets import QGridLayout, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon,QGuiApplication
import sys
import os
from database import databasemanager

class AddBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Book")
        self.setFixedSize(900, 560)
        self.center()
        icon_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(icon_path))
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QGridLayout()
        layout.setVerticalSpacing(20)
        
        #image_path = os.path.join(os.getcwd(), "images", "4.jpg")
        image_path = os.path.join(sys._MEIPASS, "images/2.jpg")

        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setStyleSheet("margin: 0px;")
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label, 0, 0, 10, 3)

        self.text_label = QLabel("Add New Book")
        self.text_label.setStyleSheet("margin-left: 20px;font-size: 35px; color:white")
        layout.addWidget(self.text_label, 0, 0, 2, 3, Qt.AlignmentFlag.AlignCenter)
        
        self.text_label = QLabel("➥ Here you can add a book.\n")
        self.text_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text_label,2,0,2,3)
       
        self.text1_label = QLabel("➥ You must have to fill all required field\n to successfully ADD a book in library.\n")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,3,0,2,3)
        
        self.text1_label = QLabel("➥ NOTE: Book ID must be unique and \n default status is 'Available'.")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,4,0,2,3)

        self.bookname_label = QLabel("Book Name")
        layout.addWidget(self.bookname_label, 1, 3)

        self.bookname_input = QLineEdit()
        self.bookname_input.setPlaceholderText(" Type book name")
        layout.addWidget(self.bookname_input, 2, 3, 1, 3)
        self.bookname_input.setContentsMargins(0, 0, 0, 0)

        self.bookid_label = QLabel("Book ID")
        layout.addWidget(self.bookid_label, 3, 3)

        self.bookid_input = QLineEdit()
        self.bookid_input.setPlaceholderText("eg. BK001")
        layout.addWidget(self.bookid_input, 4, 3, 1, 3)

        self.author_label = QLabel("Author")
        layout.addWidget(self.author_label, 5, 3)

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Type author")
        layout.addWidget(self.author_input, 6, 3, 1, 3)

        self.status_label = QLabel("Status")
        layout.addWidget(self.status_label, 7, 3)

        self.status_input = QLineEdit()
        self.status_input.setPlaceholderText("Available/Issued")
        layout.addWidget(self.status_input, 8, 3, 1, 3)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_book)
        layout.addWidget(self.save_button, 9, 3)

        self.quit_button = QPushButton("Quit", clicked=self.close)
        layout.addWidget(self.quit_button, 9, 5)
        
        layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(layout)

        self.setStyleSheet("""
            AddBook{background-color: #DDE0E7; }
            QLabel {
                font-size: 18px;
                color: #373737;
                font-family: Comic Sans MS;
                margin-left: 20px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #f0f0f0;
                padding: 10px;
                margin: 0px 20px;
                font-size: 15px;
                border: 1px solid gray;
                border-radius: 20px;
                font-family: Comic Sans MS;
            }
            QPushButton {
                background-color: #5ec480;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 20px;
                font-size: 18px;
                font-family: Comic Sans MS;
                margin: 0px 18px 20px 20px;
                width: 200px;
            }
            QPushButton:pressed {background-color: #499964;}
        """)

    def save_book(self):
        book_name = self.bookname_input.text()
        book_id = self.bookid_input.text()
        author = self.author_input.text()
        status = self.status_input.text()
        
        if not book_id or not book_name:
            self.show_message("Incomplete Information", "Please enter all fields.")
            return
        if not status:
            status = 'Available'
        elif status.lower() not in ['available', 'issued']:
            self.show_message("Incomplete Information", "Please enter valid status (available or issued).")
            return
        
        obj = databasemanager()
        result, error = obj.add_book(book_name, book_id, author, status)
        if result == "OK":
            self.bookname_input.clear()
            self.bookid_input.clear()
            self.author_input.clear()
            self.status_input.clear()
            self.show_message("Message", "Book added successfully!")
        else:
            self.show_message("Error", f"An error occurred: {str(error)}")

    def center(self):
        primary_screen = QGuiApplication.primaryScreen()
        
        screen_geometry = primary_screen.geometry()
        
        screen_center = screen_geometry.center()
    
        window_position = self.rect()
        window_position.moveCenter(screen_center)
        
        self.move(window_position.topLeft())
  
    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
