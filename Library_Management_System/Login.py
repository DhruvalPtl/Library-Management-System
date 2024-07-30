import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap,QIcon,QGuiApplication
from database import logintodb, MakeDir
import os
MakeDir.create_folder()
from main import MainWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(900, 560)
        self.center()
        
        icon_path = os.path.join(sys._MEIPASS, "images/icon1.png")
        self.setWindowIcon(QIcon(icon_path))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
            
        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(10)
        self.central_widget.setContentsMargins(0, 0, 0, 0)
        
        #image_path = os.path.join(os.getcwd(), "images", "1.jpg")
        image_path = os.path.join(sys._MEIPASS, "images/1.jpg")
        
        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.layout.addWidget(self.image_label,0,0,9,3)
        
        self.text_label = QLabel("<h1>Welcome  to  Library<br>Management System</h1>")
        self.text_label.setStyleSheet("text-align:center;padding-top:10px;color: #f5f5f5;font-family: Comic Sans MS;")
        self.layout.addWidget(self.text_label,0,0,2,3, Qt.AlignmentFlag.AlignCenter)
        
        self.text_label = QLabel("LMS is software that helps in simplifying<br>the daily operations of the library.")
        self.text_label.setStyleSheet("margin-left:5px;color: #f5f5f5;font-size: 19px; font-weight: bold")
        self.layout.addWidget(self.text_label,2,0,2,3)
    
        self.text_label = QLabel("The purpose of a LMS is to manage &<br>track the daily work of the library such<br> as issuing books, return books,total books")
        self.text_label.setStyleSheet("margin-left:5px;color: #f5f5f5;font-size: 19px; font-weight: bold")
        self.layout.addWidget(self.text_label,4,0,2,3)
    
        self.intro_label = QLabel("Login    ")
        self.intro_label.setStyleSheet("font-size: 35px;")
        self.layout.addWidget(self.intro_label,0,4,1,6, Qt.AlignmentFlag.AlignCenter)

        self.intro1_label = QLabel("Login to library and manage your books!")
        self.intro1_label.setStyleSheet("font-size: 15px;")
        self.layout.addWidget(self.intro1_label,1,4,1,5, Qt.AlignmentFlag.AlignCenter)

        self.username_label = QLabel("Username")
        self.layout.addWidget(self.username_label,2,4)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText(" Type your username")
        self.layout.addWidget(self.username_input,3,4,1,5)

        self.password_label = QLabel("Password")
        self.layout.addWidget(self.password_label,4,4)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText(" Type your password")
        self.layout.addWidget(self.password_input,5,4,1,5)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button,6,4,1,5)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)
        self.layout.addWidget(self.register_button,7,4,1,5)
        
        self.emptspace_label = QLabel("")
        self.layout.addWidget(self.emptspace_label,8,3)
        
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(self.layout)
        
        self.setStyleSheet("""
            LoginWindow{background-color: #DDE0E7; }
            QLabel {
                color: #373737;
                font-size: 17px;
                font-weight: bold;
                font-family: Comic Sans MS;
            }
            QLineEdit {
                background-color: #e3e6eb;
                border: 1px solid gray;
                border-radius: 20px;
                font-size: 16px;
                font-family: Comic Sans MS;
                padding: 7px;
            }
            QPushButton {
                background-color: #51c5a2;
                color: white;
                padding: 9px 18px;
                border: none;
                border-radius: 22px;
                font-size: 18px;
                margin: 10px 0px 5px 0px;
                font-family: Comic Sans MS;
            }
            QPushButton:pressed {
                background-color: #48af90;
                }"
        """)
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
            
        if not username or not password:
            self.show_message("Incomplete Information", "Please enter both username and password.")
            return 
        
        obj = logintodb()        
        user, error = obj.login(username)
        
        if error:
            self.show_message("Database Error", f"An error occurred: {str(error)}")
        if user is None:
            self.show_message("Invalid Login", "Invalid username or password.")
        elif user[1] != password:
            self.show_message("Invalid Login", "Invalid username or password.")
        else:
            self.open_main_window()
        
    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        obj = logintodb()
        result, error = obj.register(username, password)
        if result == "done":
            self.show_message("Registration Successful!", "You have successfully registered.\nPlease log in to continue.")
        else:
            self.show_message("Registration Failed", f"Error: {str(error)}")
        
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

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())