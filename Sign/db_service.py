import sqlite3

class DatabaseService:
    db_path = "../../database.db"


    def get_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        conn = sqlite3.connect(self.db_path)
        return conn

    def get_single_data(self, query, params):
        cursor = self.get_connection().cursor()
        cursor.execute(query, params)

        return cursor.fetchone()[0]


    def artist_from_name_key(self, name_key):
        query = """
            SELECT name FROM artist WHERE name_key = ?;
        """

        return self.get_single_data(query, (name_key,))

    def stage_from_id(self, stage_id):
        query = """
            SELECT name FROM stage WHERE id = ?;
        """

        return self.get_single_data(query, (stage_id,))

    def takeover_from_name_key(self, name_key):
        query = """
            SELECT name FROM takeover WHERE name_key = ?;
        """

        return self.get_single_data(query, (name_key,))