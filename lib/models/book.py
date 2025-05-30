from models import CURSOR, CONN

class Book:
    def __init__(self, name, author_id, id=None):
        self.id = id
        self.name = name
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.id}: {self.name}, Author ID: {self.author_id}>"


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author_id INTEGER,
                FOREIGN KEY(author_id) REFERENCES authors(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute(
                "INSERT INTO books (name, author_id) VALUES (?, ?)",
                (self.name, self.author_id)
            )
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                "UPDATE books SET name = ?, author_id = ? WHERE id = ?",
                (self.name, self.author_id, self.id)
            )
        CONN.commit()


    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM books WHERE name = ? LIMIT 1", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], author_id=row[2])
        return None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM books WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], author_id=row[2])
        return None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM books")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], author_id=row[2]) for row in rows]