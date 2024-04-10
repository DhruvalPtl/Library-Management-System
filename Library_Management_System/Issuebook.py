from PyQt6.QtWidgets import QGridLayout, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon,QGuiApplication
import os
import sys
from database import databasemanager

class IssueBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Issue Book")
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
        layout.addWidget(self.image_label, 0, 0, 10, 2)

        self.intro_label = QLabel("Issue Book")
        self.intro_label.setStyleSheet("font-size: 25px;color:white")
        layout.addWidget(self.intro_label, 0, 0, 2, 2, Qt.AlignmentFlag.AlignCenter)

        self.text_label = QLabel("➥ Here you can issue a book.\n")
        self.text_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text_label,2,0,2,2)
       
        self.text1_label = QLabel("➥ You must have to fill all required field\n to successfully issue a book from library\n")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,3,0,2,2)
        
        self.text1_label = QLabel("➥ NOTE: Book ID and Borrower ID must\n be unique")
        self.text1_label.setStyleSheet("margin-left: 0px;color:white;font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,4,0,2,2)

        self.bookid_label = QLabel("Book ID")
        layout.addWidget(self.bookid_label, 1, 3)

        self.bookid_input = QLineEdit()
        self.bookid_input.setPlaceholderText("Type book ID")
        layout.addWidget(self.bookid_input, 2, 3, 1, 3)

        self.borrower_label = QLabel("Borrower's Name")
        layout.addWidget(self.borrower_label, 3, 3)

        self.borrower_input = QLineEdit()
        self.borrower_input.setPlaceholderText("Type borrower's name")
        layout.addWidget(self.borrower_input, 4, 3, 1, 3)

        self.borrower_id_label = QLabel("Borrower's ID")
        layout.addWidget(self.borrower_id_label, 5, 3)

        self.borrower_id_input = QLineEdit()
        self.borrower_id_input.setPlaceholderText("Type borrower's ID")
        layout.addWidget(self.borrower_id_input, 6, 3, 1, 3)

        self.issue_button = QPushButton("Issue Book")
        self.issue_button.clicked.connect(self.issue_book)
        layout.addWidget(self.issue_button, 7, 3, 1, 3)

        self.quit_button = QPushButton("Quit", clicked=self.close)
        layout.addWidget(self.quit_button, 8, 3, 1, 3)

        layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(layout)

        self.setStyleSheet("""
            IssueBook{
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

    def issue_book(self):
        book_id = self.bookid_input.text()
        borrower_name = self.borrower_input.text()
        borrower_id = self.borrower_id_input.text()
        
        if  not book_id or not borrower_name or not borrower_id :
            self.show_message("Incomplete Information", "Please enter all fields.")
            return
        
        obj = databasemanager()
        result, error = obj.issue_book(borrower_id, borrower_name, book_id)
        if result == "OK" and error == None:
            self.clear_fields()
            self.show_message("Success", "Successfully issued the book.")
        elif result == None and error == "NO":
            self.show_message("Error", "Book is already issued or does not exist.")
        else:
            self.show_message("Database Error", f"{error}")
        
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
        """Clears all input fields."""
        for item in [self.bookid_input, self.borrower_input, self.borrower_id_input]:
            item.setText("")
