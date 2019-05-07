import sqlite3
import csv




sql_insert_stage = """
    INSERT INTO stage (name, id) VALUES (?, ?);
"""

sql_insert_takeover = """
    INSERT INTO takeover (name_key, name) VALUES (?, ?);
"""

sql_insert_artist = """
    INSERT or IGNORE INTO artist (name, name_key, takeover_name_key) VALUES (?, ?, ?);
"""

sql_insert_artist_to_stage = """
    INSERT  INTO artistToStage (artist_name_key, stage_id) VALUES (?, ?);
"""

sql_select_stages = """
    SELECT * FROM stage;
"""

sql_select_takeovers = """
    SELECT * FROM takeover;
"""

sql_select_artists = """
    SELECT * FROM artist;
"""

sql_select_artist_to_stage = """
    select * from artistToStage;
"""

sql_read_table_names = """
    PRAGMA table_info(table_name);
"""

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


def print_select(conn, command):
    c = conn.cursor()
    c.execute(command)

    results = c.fetchall()

    print(command)

    for result in results:

        print(result)


def create_artist_vals():
    values = []

    with open('Artist.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:

            if row[4] == "none":
                val = (row[0], row[1], None)
            else:
                val = (row[0], row[1], row[4])

            values.append(val)


    return values

def create_artist_to_stage_vals():
    values = []

    with open('Artist.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:

            val = (row[1], row[3])

            values.append(val)


    return values

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

def create_artists(conn):
    values = create_artist_vals()

    for val in values:
        execute_command_vals(conn, sql_insert_artist, val)

def create_artist_to_stage(conn):
    values = create_artist_to_stage_vals()

    for val in values:
        execute_command_vals(conn, sql_insert_artist_to_stage, val)

if __name__ == '__main__':
    conn = create_connection("../database.db")
    if conn is not None:
        create_stages(conn)
        create_takeovers(conn)
        create_artists(conn)
        create_artist_to_stage(conn)

        conn.commit()

    else:
        print("Error! cannot create the database connection.")