from .database import new_db_connection, create_table


def create_passwords_table():
    database = r"willit.db"
    ssh_conn = new_db_connection(database)
    ssh_table = """CREATE TABLE IF NOT EXISTS ssh (
                            username text,
                            password text
                            );"""
    create_table(ssh_conn, ssh_table)
