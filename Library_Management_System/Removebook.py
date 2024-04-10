from PyQt6.QtWidgets import QGridLayout, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon,QGuiApplication
import os
import sys
from database import databasemanager 

class RemoveBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Book")
        self.setFixedSize(900, 560)
        self.center()
        icon_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(icon_path))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QGridLayout()
        layout.setVerticalSpacing(10)
        
        #image_path = os.path.join(os.getcwd(), "images", "4.jpg")
        image_path = os.path.join(sys._MEIPASS, "images/2.jpg")
        
        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setStyleSheet("margin:0px;")
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label, 0, 0, 9, 2)

        self.intro_label = QLabel("Remove Book")
        self.intro_label.setStyleSheet("font-size: 25px;color:white")
        layout.addWidget(self.intro_label, 0, 0, 2, 2, Qt.AlignmentFlag.AlignCenter)

        self.text_label = QLabel("➥ Here you can remove a book.\n")
        self.text_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text_label,2,0,2,2)
       
        self.text1_label = QLabel("➥ You must have to fill all required field\n to successfully remove book from library\n")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,3,0,2,2)
        
        self.text1_label = QLabel("➥ NOTE: Book ID must be unique\n")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,4,0,2,2)

        self.bookid_label = QLabel("Book ID")
        layout.addWidget(self.bookid_label, 1, 3)

        self.bookid_input = QLineEdit()
        self.bookid_input.setPlaceholderText("Type book ID")
        layout.addWidget(self.bookid_input, 2, 3, 1, 3)

        self.bookname_label = QLabel("Book Name")
        layout.addWidget(self.bookname_label, 3, 3)

        self.bookname_input = QLineEdit()
        self.bookname_input.setPlaceholderText("Type book name")
        layout.addWidget(self.bookname_input, 4, 3, 1, 3)

        self.remove_button = QPushButton("Remove Book")
        self.remove_button.clicked.connect(self.remove_book)
        layout.addWidget(self.remove_button, 5, 3, 1, 3)

        self.quit_button = QPushButton("Quit", clicked=self.close)
        layout.addWidget(self.quit_button, 6, 3, 1, 3)

        layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(layout)

        self.setStyleSheet("""
            RemoveBook{
                background-color: #DDE0E7;
            }
            QLabel {
                color: #373737;
                font-size: 18px;
                font-family: Comic Sans MS;
                font-weight: bold;
                margin-right: 20px;
                margin-left: 20px;
            }
            QLineEdit {
                font-family: Comic Sans MS;
                background-color: #f0f0f0;
                border: 1px solid gray;
                border-radius: 20px;
                padding: 10px;
                margin-right: 20px;
                margin-left: 20px;
                font-size: 15px
            }
            QPushButton {
                margin-right: 20px;
                margin-left: 20px;
                font-family: Comic Sans MS;
                background-color: #5ec480;
                color: white;
                padding: 8px 18px;
                border: none;
                border-radius: 21px;
                font-size: 18px;
                margin-top: 13px;
            }
            QPushButton:pressed {background-color: #499964;}
        """)

    def remove_book(self):
        book_id = self.bookid_input.text()
        if  not book_id:
            self.show_message("Incomplete Information", "Please enter fields.")
            return
        
        obj = databasemanager()
        result, error = obj.remove_book(book_id)
        if result == "OK" and error == None:
            self.show_message("Success", "The book has been removed.")
            self.clear_fields()
        elif result is None and error == "NO":
            self.show_message("Not Found", "Book ID not found in the Library")
        else:
            self.show_message("Error", f"An error occurred while removing the book:\n{error}")
            
    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def center(self):
        primary_screen = QGuiApplication.primaryScreen()
        
        screen_geometry = primary_screen.geometry()
        
        screen_center = screen_geometry.center()
    
        window_position = self.rect()
        window_position.moveCenter(screen_center)
        
        self.move(window_position.topLeft())

    def clear_fields(self):
        for item in [self.bookid_input, self.bookname_input]:
            item.setText("")
    