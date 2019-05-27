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
        conn = self.get_connection()

        with conn:

            crs = conn.cursor()
            crs.execute(query, params)

            return crs.fetchone()[0]

    def execute_command_vals(self, command, vals):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """

        conn = self.get_connection()

        c = conn.cursor()
        c.execute(command, vals)
        conn.commit()

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

    def get_artist_phrase(self, artist_name_key):
        query = """
            SELECT * FROM phrase 
            WHERE (any_artist = 1 OR artist_name_key = ?)
            AND id IN (SELECT id FROM table ORDER BY RANDOM() LIMIT 1);
        """

        return self.get_single_data(query, (artist_name_key,))

    def get_stage_phrase(self, stage_id):
        query = """
            SELECT * FROM phrase 
            WHERE (any_stage = 1 OR stage_id = ?)
            AND id IN (SELECT id FROM table ORDER BY RANDOM() LIMIT 1);
        """

        return self.get_single_data(query, (stage_id,))

    def get_takeover_phrase(self, takeover_name_key):
        query = """
            SELECT * FROM phrase 
            WHERE (any_stage = 1 OR takeover_name_key = ?)
            AND id IN (SELECT id FROM table ORDER BY RANDOM() LIMIT 1);
        """

        return self.get_single_data(query, (takeover_name_key,))

    def get_generic_phrase(self):
        query = """
                    SELECT * FROM phrase 
                    WHERE generic_phrase = 1
                    AND id IN (SELECT id FROM table ORDER BY RANDOM() LIMIT 1);
                """

        return self.get_single_data(query, ())

    def select_all_phrases(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        print("GETTING ALL PHRASES")
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM phrase")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def insert_phrase(self, args):
        query = """
            INSERT OR REPLACE INTO phrase 
            (id, phrase, artist_name_key, stage_id, takeover_name_key, any_stage, any_artist, any_takeover, generic_phrase)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        id = args["id"]
        text = args["p"]
        artist = args.get("a")
        stage = args.get("s")
        takeover = args.get("t")
        any_artist = "{artist}" in text
        any_stage = "{stage}" in text
        any_takeover = "{takeover}" in text
        generic_phrase = artist is None and takeover is None and stage is None and not any_artist and not any_takeover and not any_stage

        vals = (id, text, artist, stage, takeover, any_stage, any_artist, any_takeover, generic_phrase)

        self.execute_command_vals(query, vals)

