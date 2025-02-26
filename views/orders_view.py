import json
import sqlite3


def list_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT 
                o.id,
                o.metal_id,
                o.style_id,
                o.size_id
            FROM Orders o
                """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))

        serialized_orders = json.dumps(orders)
        return serialized_orders


def retrieve_order(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT 
                o.id,
                o.metal_id,
                o.style_id,
                o.size_id
            FROM Orders o
            WHERE Id = ?
                """,
            (primary_key,),
        )
        requested_data = db_cursor.fetchone()
        requested_data_as_dictionary = dict(requested_data)
        requested_data_as_json = json.dumps(requested_data_as_dictionary)
        return requested_data_as_json


def update_order(primary_key, replacement_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Orders
                SET
                    metal_id = ?,
                    style_id = ?,
                    size_id = ?
            WHERE Id = ?
                """,
            (
                replacement_data["metal_id"],
                replacement_data["style_id"],
                replacement_data["size_id"],
                primary_key,
            ),
        )
        return True if db_cursor.rowcount > 0 else False
