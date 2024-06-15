# ========================================================================
# concerts.py
# ========================================================================
# Functions for interacting with the database of known concerts
#
# Author: Aidan McNay
# Date: June 15th, 2024

import sqlite3
from threading import Lock

# ------------------------------------------------------------------------
# Create a lock for accessing the database
# ------------------------------------------------------------------------

concert_db_lock = Lock()

# ------------------------------------------------------------------------
# Create an atomic wrapper for accessing the database
# ------------------------------------------------------------------------
# Inspired by https://stackoverflow.com/a/50645518/23068975


class ConcertDB:
    def __init__(self, file=".db/concert.db"):
        self.file = file

    def __enter__(self):
        concert_db_lock.acquire()
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, _type, _value, _traceback):
        self.conn.commit()
        self.conn.close()
        concert_db_lock.release()
