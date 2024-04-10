from PyQt6.QtWidgets import  QApplication,QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton ,QMessageBox
from database import databasemanager
from PyQt6.QtGui import QIcon,QGuiApplication
import os
import sys

class SearchResult(QMainWindow):
    def __init__(self,search_text):
        super().__init__()
        self.search_text = search_text
        self.setWindowTitle("Search Results")
        self.setFixedSize(900, 560)
        self.center()
        icon_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(icon_path))
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        headers = ["Book ID","Book Name", "Author", "Status" , "Borrower ID" , "Borrower Name"]
        self.table.setHorizontalHeaderLabels(headers)
        for col in range(len(headers)):
                self.table.setColumnWidth(col, 143)
        layout.addWidget(self.table)
        
        self.quit_button = QPushButton("Quit")
        self.quit_button.setStyleSheet("""QPushButton{margin-right: 20px;
                margin-left: 20px;
                font-family: Comic Sans MS;
                background-color: #5ec480;
                color: white;
                padding: 8px 18px;
                border: none;
                border-radius: 21px;
                font-size: 18px;
                margin-top: 13px;}
                QPushButton:hover {
                background-color: #499964;
                }
                QPushButton:pressed {background-color: #499964;}
                """)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)
        
        self.search_books()
    
        self.central_widget.setLayout(layout)
    
    def search_books(self):
        obj = databasemanager()
        books, error = obj.search_book(self.search_text)
        if books:
            self.table.setRowCount(0)
            for row_num, book in enumerate(books):
                self.table.insertRow(row_num)
                for col_num, data in enumerate(book):
                    self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        elif error is None:
            self.show_message("Search Message",f"No books found matching: {self.search_text}")
            self.close()
        else:
            self.show_message("Error", f"An error occurred while searching the database:\n\n{error}")    

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
        