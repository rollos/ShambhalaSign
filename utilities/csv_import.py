import sqlite3

def execute_command_vals(conn, command, vals):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    c = conn.cursor()
    c.execute(command, vals)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = sqlite3.connect(db_file)
    return conn


def insert_artist(name_key, name, takeover_name_key):
    pass


sql_insert_stage = """
    INSERT INTO stage (name, id) VALUES (?, ?);
"""

sql_insert_takeover = """
    INSERT INTO takeover (name_key, name) VALUES (?, ?);
"""

sql_insert_artist = """
    INSERT INTO artist (name, name_key, takover_name_key) VALUES (?, ?, ?);
"""

sql_insert_artist_to_stage = """
    INSERT INTO artistToStage (artist_id, stage_id) VALUES (%s, ?, ?);
"""



def create_stages(conn):
    values = [
        ("Pagoda", 1),
        ("Village", 2),
        ("Fractal Forest", 3),
        ("Amp", 4),
        ("Living Room", 5),
        ("Grove", 6)
    ]


    for val in values:
        execute_command_vals(conn, sql_insert_stage, val)

def create_takeovers(conn):
    values = [
        ("Jungle Cakes", "jungle_cakes"),
        ("Wakaan", "wakkan"),
        ("Sunrise Sessions", "sunrise_sessions"),
        ("Ragga Jungle Rinse Out", "ragga_rinse_out"),
        ("Cosmic Bridge", "cosmic_bridge"),
        ("Deep Dark and Dangerous", "deep_dark")
    ]

    for val in values:
        execute_command_vals(conn, sql_insert_takeover, val)

if __name__ == '__main__':
    conn = create_connection("../database.db")
    if conn is not None:
        create_stages(conn)
        create_takeovers(conn)
    else:
        print("Error! cannot create the database connection.")