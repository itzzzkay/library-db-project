from models import CURSOR, CONN 
from models.author import Author
from models.member import Member 

class Book:
    
    def __init__(self, name, author, id=None):
        self.id = id
        self.name = name
        self.author = author

    def __repr__(self):
        return f"<Book {self.id}: {self.name}, Written by: {self.author}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()