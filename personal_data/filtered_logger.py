
'''filtered logger'''

import re
from typing import List
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filtering values of the required fields'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}",
                         f"{item}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formatting method for logs"""
        msg = filter_datum(self.fields, self.REDACTION,
                           record.getMessage(), self.SEPARATOR)
        return (self.FORMAT %
                {"name": record.name, "levelname": record.levelname, "asctime":
                 self.formatTime(record, self.datefmt), "message": msg})


def get_logger() -> logging.Logger:
    '''Returns a logging object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Returns a connector to the database'''
    connection = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return connection


def main():
    db_connection = get_db()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        logger.info(str_row.strip())

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
