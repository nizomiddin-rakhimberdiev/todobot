import os
import sqlite3
from datetime import datetime
from multiprocessing import Pool
from typing import Union


class Database:

    def __init__(self, path_to_db="db.sqlite3"):
        self.path_to_db = path_to_db
        self.connection = sqlite3.connect(self.path_to_db)
        self.cursor = self.connection.cursor()

    def add_todo(self, title, description):
        done = False
        created_at = datetime.now()
        updated_at = created_at
        self.cursor.execute("""
        INSERT INTO bot_todo (title, description, done, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)""", (title, description, done, created_at, updated_at))
        self.connection.commit()

    def get_todos(self):
        return self.cursor.execute("SELECT * FROM bot_todo").fetchall()

    def update_todo(self, todo_id):
        self.cursor.execute("""
        UPDATE bot_todo SET done = True WHERE id = ?;
        """, todo_id)
        self.connection.commit()
