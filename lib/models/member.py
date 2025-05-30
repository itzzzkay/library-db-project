from models import CURSOR, CONN

class Member:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Member {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        CONN.close()

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO members (name) VALUES (?)", (self.name,))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE members SET name = ? WHERE id = ?", (self.name, self.id))
        CONN.commit()
        CONN.close()

    def find_by_name
