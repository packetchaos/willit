import sqlite3
from sqlite3 import Error
import click
# import time


def new_db_connection(db_file):
    # create a connection to our database
    conn = None
    try:
        # A database file will be created if one doesn't exist
        conn = sqlite3.connect(db_file, timeout=10.0)
    except Error as E:
        click.echo(E)
    return conn


def create_table(conn, table_information):
    try:
        c = conn.cursor()
        c.execute('pragma journal_mode=wal;')
        c.execute(table_information)
    except Error as e:
        click.echo(e)


def db_query(statement):
    # start = time.time()
    database = r"willit.db"
    query_conn = new_db_connection(database)
    with query_conn:
        cur = query_conn.cursor()
        cur.execute('pragma journal_mode=wal;')
        cur.execute('pragma cache_size=-10000;')
        cur.execute('PRAGMA synchronous = OFF')
        cur.execute('pragma threads=4')
        cur.execute(statement)

        data = cur.fetchall()
        # end = time.time()
        # total = end - start
    query_conn.close()
    # click.echo("Sql Query took: {} seconds".format(total))
    return data


def drop_tables(conn, table):
    try:
        drop_table = '''DROP TABLE {}'''.format(table)
        cur = conn.cursor()
        cur.execute('pragma journal_mode=wal;')
        cur.execute(drop_table)
    except Error:
        pass
