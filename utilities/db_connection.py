# db_utils.py
import os  
import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = sqlite3.connect(db_file)
    return conn

def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param connection: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    c = connection.cursor()
    c.execute(create_table_sql)




if __name__ == '__main__':
    sql_create_artist_table = """
         CREATE TABLE IF NOT EXISTS artist (
                                                name text NOT NULL,
                                                name_key text PRIMARY KEY,
                                                takeover_name_key text,
                                                FOREIGN KEY (takeover_name_key) REFERENCES takeover (name_key)
                                            ); 
                                            """

    sql_create_stage_table = """
        CREATE TABLE IF NOT EXISTS stage (
                                              id integer PRIMARY  KEY,
                                              name text NOT NULL
        );
        """

    sql_create_takeover_table = """
        CREATE TABLE IF NOT EXISTS takeover (
                                              name_key text PRIMARY KEY,
                                              name text NOT NULL
        );
        """

    sql_create_artist_to_stage_table = """
        CREATE TABLE IF NOT EXISTS artistToStage (
                                                    artist_name_key text NOT NULL,
                                                    stage_id int NOT NULL,
                                                    FOREIGN KEY (artist_name_key) REFERENCES artist (name_key),
                                                    FOREIGN KEY (stage_id) REFERENCES stage (id),
                                                    PRIMARY KEY (artist_name_key, stage_id)
        );
        """


    sql_create_phrase_table = """
        CREATE TABLE IF NOT EXISTS phrase (
                                            id int PRIMARY  KEY,
                                            phrase text NOT NULL,
                                            stage_id int,
                                            artist_name_key text,
                                            takeover_name_key text,
                                            any_stage BOOLEAN NOT NULL,
                                            any_artist BOOLEAN NOT NULL,
                                            any_takeover BOOLEAN NOT NULL,
                                            generic_phrase BOOLEAN NOT NULL,
                                            
                                            FOREIGN KEY (artist_name_key) REFERENCES artist (name_key),
                                            FOREIGN KEY (stage_id) REFERENCES stage (id),
                                            FOREIGN KEY (takeover_name_key) REFERENCES takeover (name_key)                                           
        );
    """

    sql_drop_artist_table = """
        DROP TABLE artist;
    """

    sql_drop_phrase_table = """
            DROP TABLE phrase;
        """

    conn = create_connection("../database.db")
    if conn is not None:
        create_table(conn, sql_drop_phrase_table)
        # create artist table
        create_table(conn, sql_create_artist_table)
        # create stage table
        create_table(conn, sql_create_stage_table)
        # create takeover table
        create_table(conn, sql_create_takeover_table)
        # create artist to stage table
        create_table(conn, sql_create_artist_to_stage_table)
        # create phrase table
        create_table(conn, sql_create_phrase_table)

        conn.commit()
    else:
        print("Error! cannot create the database connection.")
