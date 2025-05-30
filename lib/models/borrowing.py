from models import CURSOR, CONN

class Borrowing:
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                member_id INTEGER,
                FOREIGN KEY(book_id) REFERENCES books(id),
                FOREIGN KEY(member_id) REFERENCES members(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def borrow(cls, book_id, member_id):
        CURSOR.execute(
            "INSERT INTO borrowings (book_id, member_id) VALUES (?, ?)",
            (book_id, member_id)
        )
        CONN.commit()

    @classmethod
    def borrowed_books(cls):
        sql = """
            SELECT books.name, members.name
            FROM borrowings
            JOIN books ON borrowings.book_id = books.id
            JOIN members ON borrowings.member_id = members.id;
        """
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM borrowings")
        return CURSOR.fetchall()