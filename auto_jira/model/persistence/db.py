"""
This module contains the data base (sqlite3) definitions and functions.
"""
import sqlite3


# class DataBaseCursor:
#     def __init__(self, connection):
#         self.connection = connection


class DataBaseConnection:
    def __init__(self, path):
        self.path = path
        self.connection = None

    def create_connection(self):
        """This method creates and returns a sqlite connection.

        :return: SQLITE3 connection
        """
        self.connection = sqlite3.connect(self.path)
        return self.connection

    # def create_cursor(self):
    #     """This method returns a sqlite cursor.
    #
    #     :return: SQLITE3 cursor
    #     """
    #     return DataBaseCursor(self.connection)

    def close_connection(self):
        """This method closes the sqlite connection.

        :return: None
        """
        self.connection.close()
