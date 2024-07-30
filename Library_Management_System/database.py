import sqlite3
import os
import sys
from pathlib import Path

class MakeDir():
    @staticmethod
    def create_folder():
        try:
            base_path = Path("C:/Library Management System/Database")
            db_file = base_path / "LMSDB.db"
            os.makedirs(base_path, exist_ok=True)
            conn = sqlite3.connect(db_file)
            a = conn.cursor()
            a.execute('''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)''')
            a.execute("create table if not exists bookinfo(book_id text PRIMARY KEY, book_name text, author_name text, status  text, borrower_id text, borrower_name text)")
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            return e
        
class logintodb():
    def  __init__(self):
        #self.database_login_path = os.path.join(os.getcwd(), "database", "LMS.db")
        #database_path = os.path.join(sys._MEIPASS, "LMS.db")
        # if getattr(sys, 'frozen', False):
        #     base_path = sys._MEIPASS
        # else:
        #     base_path = os.path.abspath(os.path.dirname(__file__))
        database_path = 'C:/Library Management System/Database/LMSDB.db'
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        
    def login(self,username):
        try:
            self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = self.cursor.fetchone()
            return user , None
        except sqlite3.Error as e:
            return None , e
       
    def register(self,username,password):
        try:
            self.cursor.execute("INSERT INTO users VALUES (?,?)", (username, password))
            self.conn.commit()
            return  "done",None
        except sqlite3.Error as e:
            return None, e
    
    def total_member(self):
        self.cursor.execute( ''' SELECT * FROM users''' )
        rows = self.cursor.fetchall()
        return len(rows)
         
class databasemanager():
    def  __init__(self):
        #self.database_access_path = os.path.join(os.getcwd(), "database", "LMS.db")
        # #database_path = os.path.join(sys._MEIPASS, "LMS.db")   
        # if getattr(sys, 'frozen', False):
        #     base_path = sys._MEIPASS
        # else:
        #     base_path = os.path.abspath(os.path.dirname(__file__))

        database_path = 'C:/Library Management System/Database/LMSDB.db'
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

        
    def total_book(self):
        self.cursor.execute('''SELECT * FROM bookinfo ''')
        rows = self.cursor.fetchall()
        return len(rows)
    
    def avail_book(self):
        self.cursor.execute('''SELECT COUNT(*) FROM bookinfo WHERE status="Available" ''')
        available_count = self.cursor.fetchone()[0]
        return available_count
        
    def borrowed_book(self):
        self.cursor.execute('''SELECT COUNT(*) FROM bookinfo WHERE status="Issued" ''')
        borrow_count = self.cursor.fetchone()[0]
        return borrow_count
    
    def remove_book(self, book_id):
        try:
            self.cursor.execute("DELETE FROM bookinfo WHERE book_id = ?", (book_id,))
            self.conn.commit()
            
            if self.cursor.rowcount != 0:
                return "OK", None
            else:
                return None, "NO"
        except sqlite3.Error as e:
            return None, e
            
    def return_book(self, book_id, borrower_id):
        try:
            self.cursor.execute("UPDATE bookinfo SET status='Available', borrower_id=NULL, borrower_name=NULL WHERE book_id=? AND borrower_id=?", (book_id, borrower_id))
            self.conn.commit()
            
            if self.cursor.rowcount != 0:
                return "OK", None
            else:
                return None, "NO"
        except sqlite3.Error as e:
            return None, e
    
    def issue_book(self,borrower_id, borrower_name, book_id):
        try:
            self.cursor.execute("UPDATE bookinfo SET status='Issued', borrower_id=?, borrower_name=? WHERE book_id=?", 
                       (borrower_id, borrower_name, book_id))
            if self.cursor.rowcount == 0:
                return None, "NO"
            else:
                self.conn.commit()
                return "OK", None
        except sqlite3.Error as e:
            return None, e

    def add_book(self,book_name, book_id, author, status):
        try:
            self.cursor.execute("insert into bookinfo(book_name, book_id, author_name, status) values(?,?,?,?)",(book_name, book_id, author, status.capitalize()))
            self.conn.commit()
            return "OK",None
        except sqlite3.Error as e:
            return None, e
    
    def viewbook(self):
        try:
            self.cursor.execute("SELECT * FROM bookinfo")
            books = self.cursor.fetchall()
            return books,None
        except sqlite3.Error as e:
            return None, e
    
    def search_book(self, book_name):
        try:
            query = "SELECT * FROM bookinfo WHERE book_name LIKE ? OR book_id LIKE ?"
            self.cursor.execute(query, ('%' + str(book_name) + '%', '%' + str(book_name) + '%'))
            books = self.cursor.fetchall()
            return books, None
        except sqlite3.Error as e:
            return None, e

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
