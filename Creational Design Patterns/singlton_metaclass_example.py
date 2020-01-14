import sqlite3
class MetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaClass):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqllite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print(db1)
print(db2)