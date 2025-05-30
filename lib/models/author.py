from models import CURSOR, CONN

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
        CONN.commit()
