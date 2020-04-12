from ..extensions import db

# Flask_MySQlDatabase Utilitie To Handle Cursor Effectively
class Database:
    def __init__(self):
        self.cursor = db.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tbf):
        db.connection.commit()
        self.cursor.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()