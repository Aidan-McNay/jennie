"""Functions for interacting with the database of known concerts.

Author: Aidan McNay
Date: June 15th, 2024
"""

import sqlite3
from threading import Lock

concert_db_lock = Lock()


class ConcertDB:
    """An atomic wrapper for accessing the concert database.

    Inspired by https://stackoverflow.com/a/50645518/23068975

    Users should utilize the 'with' syntax, such as:

        with ConcertDB() as con:

    to allow for scope-based connections
    """

    def __init__(self, file=".db/concert.db"):
        """Stores the file name for later use."""
        self.file = file

    def __enter__(self):
        """Acquire the lock and establish a connection."""
        concert_db_lock.acquire()
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, _type, _value, _traceback):
        """Close the connection, then release the lock."""
        self.conn.commit()
        self.conn.close()
        concert_db_lock.release()
