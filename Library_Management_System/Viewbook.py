from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont,QIcon,QGuiApplication, QScreen
import os
import sys
from database import databasemanager

class ViewAllBooks(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("View Books")
        self.setFixedSize(900, 560)
        self.center()
        
        image_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(image_path))  

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout1 = QGridLayout()
        
        title_label = QLabel("All Books in Library")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 25px; font-weight: bold; color: #333333; margin-bottom: 10px;")
        layout1.addWidget(title_label,0,0)
        
        self.refresh_icon_button = QPushButton()
        self.refresh_icon_button.setStyleSheet("QPushButton {margin-top:10px;background-color: #DDE0E7; border-radius:20px; } QPushButton:pressed {background-color: #f0f0f0;}")
        refresh_icon_path = os.path.join(sys._MEIPASS, "images/icon.png")
        self.refresh_icon_button.setIcon(QIcon(refresh_icon_path))
        self.refresh_icon_button.clicked.connect(self.load_books)
        self.refresh_icon_button.setFixedSize(51,50)
        layout1.addWidget(self.refresh_icon_button,0,1)

        layout.addLayout(layout1)
        # Table widget
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        
        self.load_books()
        self.central_widget.setLayout(layout)
        
        self.quit_button = QPushButton("Quit", clicked=self.close)
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
                """)
        layout.addWidget(self.quit_button)
    
    def load_books(self):
        obj = databasemanager()
        books, error= obj.viewbook()
        if books:  
            # Set up table headers
            headers = ["Book ID","Book Name", "Author", "Status" , "Borrower ID" , "Borrower Name"]
            self.table_widget.setColumnCount(len(headers))
            self.table_widget.setHorizontalHeaderLabels(headers)
            for col in range(len(headers)):
                self.table_widget.setColumnWidth(col, 139)
            
            # Populate table with book data
            self.table_widget.setRowCount(len(books))
            for row_idx, book in enumerate(books):
                for col_idx, data in enumerate(book):
                    item = QTableWidgetItem(str(data))
                    item.setFont(QFont("Arial", 10))
                    self.table_widget.setItem(row_idx, col_idx, item)
        else:
            self.show_message("Error", f"An error occurred while loading books:\n{error}")

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
        