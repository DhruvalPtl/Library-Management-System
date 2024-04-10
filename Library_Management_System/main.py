from PyQt6.QtWidgets import QGridLayout, QMainWindow, QLabel, QPushButton, QWidget, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt,pyqtSignal
from PyQt6.QtGui import QPixmap,QIcon,QGuiApplication
from Addbook import AddBook
from Viewbook import ViewAllBooks
from Issuebook import IssueBook
from Removebook import RemoveBook
from Returnbook import ReturnBook
from searchresult import SearchResult
import os
import sys
from database import databasemanager, logintodb

class MainWindow(QMainWindow):
    quit_signal = pyqtSignal()
    #icon_path = os.path.join(os.getcwd(), "images", "icon.png")
    refresh_icon_path = os.path.join(sys._MEIPASS, "images/icon.png")
    obj = databasemanager()
    obj1 = logintodb()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setFixedSize(900, 560)
        self.center()
        icon_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(icon_path))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        mainlayout = QGridLayout()
        layout = QGridLayout()
        layout.setVerticalSpacing(10)
        
        #image_path = os.path.join(os.getcwd(), "images", "3.png")
        image_path = os.path.join(sys._MEIPASS, "images/3.png")
        
        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label,0,0,9,4)
        
        self.count1_label = QLabel(f"<h1 style='text-align: center;'>{self.obj.total_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Total Books</p>")
        self.count1_label.setStyleSheet("margin-left:40px;background-color:#DDE0E7;color:black;padding:10px;border: 1px solid black;border-radius:10px")
        layout.addWidget(self.count1_label,6,0)

        self.count2_label = QLabel(f"<h1 style='text-align: center;'>{self.obj1.total_member()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Total Member</p>")
        self.count2_label.setStyleSheet("margin-left:40px;background-color:#DDE0E7;color:black;padding:10px;border: 1px solid black;border-radius:10px")
        layout.addWidget(self.count2_label,6,1)
        
        
        self.count3_label = QLabel(f"<h1 style='text-align: center;'>{self.obj.avail_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Available Books</p>")
        self.count3_label.setStyleSheet("margin-left:40px;background-color:#DDE0E7;color:black;padding:10px;border: 1px solid black;border-radius:10px")
        layout.addWidget(self.count3_label,7,0)
        
        
        self.count4_label = QLabel(f"<h1 style='text-align: center;'>{self.obj.borrowed_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Borrowed Books</p>")
        self.count4_label.setStyleSheet("margin-left:40px;width:9px;background-color:#DDE0E7;color:black;padding:10px;border: 1px solid black;border-radius:10px")
        layout.addWidget(self.count4_label,7,1)
        

        self.text_label = QLabel("<h1>Welcome  to  Library<br>Management System</h1>")
        self.text_label.setStyleSheet("text-align:center;padding-top:10px;color: White;font-family: Comic Sans MS;")
        layout.addWidget(self.text_label,0,0,2,3, Qt.AlignmentFlag.AlignCenter)

        self.text_label = QLabel("➥ Here you can manage books in Library.\n")
        self.text_label.setStyleSheet("font-size: 19px; font-weight: bold")
        layout.addWidget(self.text_label,2,0,2,3)
       
        self.text1_label = QLabel("➥ From now you can checkin and checkout\n to borrowing materials, updating books\n and organizing books")
        self.text1_label.setStyleSheet("font-size: 19px; font-weight: bold")
        layout.addWidget(self.text1_label,3,0,2,3)
        
        mainlayout.addLayout(layout,0,0)
        
        layout2 = QGridLayout()
        
        search_icon_path = os.path.join(sys._MEIPASS, "images/icon3.png")
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search  Book by name or ID..")
        self.search_box.setFixedWidth(300)
        layout2.addWidget(self.search_box, 0, 0, 1, 3)
        
        self.search_icon_button = QPushButton()
        self.search_icon_button.setStyleSheet("QPushButton { margin: 11px 0px 0px 5px;padding: 5px; background-color:none;border-radius: 16px;} QPushButton:pressed {background-color: #d8d8d8;}")
        self.search_icon = QIcon(search_icon_path)
        self.search_icon_button.setIcon(self.search_icon)
        self.search_icon_button.clicked.connect(self.open_search_result)
        self.search_icon_button.setFixedSize(45,43)
        layout2.addWidget(self.search_icon_button,0,2)
        
        self.refersh_icon_button = QPushButton()
        self.refersh_icon_button.setStyleSheet("QPushButton {margin-top:10px;background-color: #DDE0E7; border-radius:20px; } QPushButton:pressed {background-color: #f0f0f0;}")
        self.refersh_icon = QIcon(self.refresh_icon_path)
        self.refersh_icon_button.setIcon(self.refersh_icon)
        self.refersh_icon_button.clicked.connect(self.refresh)
        self.refersh_icon_button.setFixedSize(80,50)
        layout2.addWidget(self.refersh_icon_button,0,3)
        
        self.add_button = QPushButton("Add Book")
        self.add_button.setStyleSheet("margin-top:0px")
        self.add_button.clicked.connect(self.open_add)
        layout2.addWidget(self.add_button,1,0,2,5)

        self.remove_button = QPushButton("Remove Book")
        self.remove_button.clicked.connect(self.open_remove)
        layout2.addWidget(self.remove_button,2,0,2,5)

        self.view_button = QPushButton("View All Books")
        self.view_button.clicked.connect(self.open_view)
        layout2.addWidget(self.view_button,3,0,2,5)

        self.issue_button = QPushButton("Issue Book To Student")
        self.issue_button.clicked.connect(self.open_issue)
        layout2.addWidget(self.issue_button,4,0,2,5)

        self.return_button = QPushButton("Return Book")
        self.return_button.clicked.connect(self.open_return)
        layout2.addWidget(self.return_button,5,0,2,5)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(lambda: self.show_message("Confirmation"))
        layout2.addWidget(self.exit_button,6,0,2,5)
        self.quit_signal.connect(self.close_all_windows)

        layout.setContentsMargins(0, 0, 0, 0)
        layout2.setContentsMargins(0, 0, 0, 0)
        mainlayout.setContentsMargins(0, 0, 0, 0)
        mainlayout.addLayout(layout2,0,1)
        self.central_widget.setLayout(mainlayout)

        self.setStyleSheet("""
            MainWindow{background-color: #DDE0E7; }
            QLineEdit {
                background-color: #f4f4f4;
                border: 1px solid #ccc;
                padding: 5px;
                font-size: 17px;
                border-radius:17px;
                margin: 10px 0px 0px 0px;
            }
            QLabel {
                color: White;
                font-family: Comic Sans MS;
            }
            QPushButton {
                background-color: #5ec480;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-family: Comic Sans MS;
                margin:0px 40px 0px 0px
            }
            QPushButton:pressed {background-color: #499964;}
        """)
    
    def closeEvent(self, event):
        self.obj.close_connection()
        event.accept()
    
    def refresh(self):
        self.count1_label.setText(f"<h1 style='text-align: center;'>{self.obj.total_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Total Books</p>")
        self.count2_label.setText(f"<h1 style='text-align: center;'>{self.obj1.total_member()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Total Member</p>")
        self.count3_label.setText(f"<h1 style='text-align: center;'>{self.obj.avail_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Available Books</p>")
        self.count4_label.setText(f"<h1 style='text-align: center;'>{self.obj.borrowed_book()}</h1>\n<p style='font-size:14px;font-weight:bold;text-align: center;'>Borrowed Books</p>")
    
    def open_search_result(self):
        self.search_text = self.search_box.text()
        if not self.search_text:
            return
        
        self.search_result_page = SearchResult(self.search_text)
        self.search_result_page.show()    
    
    def open_add(self):
        self.add_page = AddBook()
        self.add_page.show()

    def open_remove(self):
        self.remove_page = RemoveBook()
        self.remove_page.show()

    def open_view(self):
        self.view_page = ViewAllBooks()
        self.view_page.show()
        
    def open_issue(self):
        self.issue_page = IssueBook()
        self.issue_page.show()    

    def open_return(self):
        self.return_page = ReturnBook()
        self.return_page.show()

    def center(self):
        primary_screen = QGuiApplication.primaryScreen()
        
        screen_geometry = primary_screen.geometry()
        
        screen_center = screen_geometry.center()
    
        window_position = self.rect()
        window_position.moveCenter(screen_center)
        
        self.move(window_position.topLeft())

    def show_message1(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def show_message(self, title):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText("Are you sure you want to quit?")
        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")
        msg_box.addButton(yes_button, QMessageBox.ButtonRole.YesRole)
        msg_box.addButton(no_button, QMessageBox.ButtonRole.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            self.quit_signal.emit()
            self.close()        

    def close_all_windows(self):
        if hasattr(self, 'add_page'):
            self.add_page.close()
        if hasattr(self, 'remove_page'):
            self.remove_page.close()
        if hasattr(self, 'view_page'):
            self.view_page.close()
        if hasattr(self, 'issue_page'):
            self.issue_page.close()
        if hasattr(self, 'return_page'):
            self.return_page.close()
        if hasattr(self, 'search_result_page'):
            self.search_result_page.close()
            