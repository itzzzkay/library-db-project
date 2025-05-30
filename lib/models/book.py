from models import CURSOR, CONN 

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

    def save(self):
        if self.id is None:
            CURSOR.execute(
                "INSERT INTO books (name, author) VALUES (?, ?)",
                (self.name, self.author)
            )
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                "UPDATE books SET name = ?, author = ? WHERE id = ?",
                (self.name, self.author, self.id)
            )
        CONN.commit()

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM books WHERE name = ? LIMIT 1", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], author=row[2])
        return None
    
    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM books")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], author=row[2]) for row in rows]
    
    
