import json
import sqlite3


def list_styles():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT 
                s.id,
                s.style,
                s.price
            FROM Styles s
            """
        )
        query_results = db_cursor.fetchall()

        styles = []
        for row in query_results:
            styles.append(dict(row))

        serialized_styles = json.dumps(styles)
        return serialized_styles


def retrieve_style(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                s.id,
                s.style,
                s.price
            FROM Styles s
            Where Id = ?
                """,
            (primary_key,),
        )
        requested_data = db_cursor.fetchone()

        requested_data_as_dictionary = dict(requested_data)
        requested_data_as_json = json.dumps(requested_data_as_dictionary)
        return requested_data_as_json


def update_style(primary_key, replacement_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Styles
                SET
                    style = ?,
                    price = ?
            WHERE Id = ?
                """,
            (replacement_data["style"], replacement_data["price"], primary_key),
        )
        return True if db_cursor.rowcount > 0 else False
