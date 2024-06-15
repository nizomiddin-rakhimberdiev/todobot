import os
import sqlite3
from multiprocessing import Pool
from typing import Union


class Database:

    def __init__(self, path_to_db="db.sqlite3"):
        self.path_to_db = path_to_db
        self.connection = sqlite3.connect(self.path_to_db)
        self.cursor = self.connection.cursor()

    def add_todo(self, title, description):
        self.cursor.execute("""
        INSERT INTO bot_todo (title, description)
        VALUES (?, ?)""", (title, description))


    def get_todos(self):
        return self.cursor.execute("SELECT * FROM bot_todo").fetchall()



