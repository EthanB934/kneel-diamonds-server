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


def update_size(primary_key, replacement_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Sizes
                SET
                    size = ?,
                    price = ?
            WHERE Id = ?
                """,
            (replacement_data["size"], replacement_data["price"], primary_key),
        )
        return True if db_cursor.rowcount > 0 else False


def create_size(new_size_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                INSERT INTO Sizes VALUES (null, ?, ?)
            """,
            (new_size_data["size"], new_size_data["price"]),
        )


def delete_size(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Sizes
                WHERE Id = ?
                """,
            (primary_key,),
        )
        number_of_rows_deleted = db_cursor.rowcount

        return True if number_of_rows_deleted > 0 else False
