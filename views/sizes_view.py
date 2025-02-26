import json
import sqlite3


def list_sizes():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                s.id,
                s.size,
                s.price
            FROM Sizes s
            """
        )
        query_results = db_cursor.fetchall()

        sizes = []
        for row in query_results:
            sizes.append(dict(row))

        serialized_sizes = json.dumps(sizes)
        return serialized_sizes


def retrieve_size(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT 
                s.id,
                s.size,
                s.price
            FROM Sizes s
            WHERE Id = ?
                """,
            (primary_key,),
        )
        requested_data = db_cursor.fetchone()
        requested_data_as_dictionary = dict(requested_data)
        requested_data_as_json = json.dumps(requested_data_as_dictionary)
        return requested_data_as_json
