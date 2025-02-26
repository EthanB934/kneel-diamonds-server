import json
import sqlite3


def list_orders(url):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if "_expand" in url["query_parameters"]:
            db_cursor.execute(
                """
                SELECT 
                    o.id,
                    o.metal_id,
                    o.style_id,
                    o.size_id,
                    m.id metalId,
                    m.metal metalMetal,
                    m.price metalPrice,
                    sty.id styleId,
                    sty.style styleStyle,
                    sty.price stylePrice,
                    s.id sizeId,
                    s.size sizeSize,
                    s.price sizePrice
                FROM Orders o
                JOIN Metals m 
                    ON m.id = o.metal_id
                JOIN Styles sty 
                    ON sty.id = o.style_id
                JOIN Sizes s 
                    ON s.id = o.size_id
                    """
            )
            query_results = db_cursor.fetchall()

            orders = []
            for row in query_results:
                metal = {
                    "id": row["metalId"],
                    "metal": row["metalMetal"],
                    "price": row["metalPrice"],
                }
                style = {
                    "id": row["styleId"],
                    "style": row["styleStyle"],
                    "price": row["stylePrice"],
                }
                size = {
                    "id": row["sizeId"],
                    "size": row["sizeSize"],
                    "price": row["sizePrice"],
                }
                metal = {
                    "id": row["metalId"],
                    "metal": row["metalMetal"],
                    "price": row["metalPrice"],
                }
                order = {
                    "id": row["id"],
                    "metal_id": row["metal_id"],
                    "metal": metal,
                    "style_id": row["style_id"],
                    "style": style,
                    "size_id": row["size_id"],
                    "size": size,
                }
                orders.append(order)
                serialized_orders = json.dumps(orders)
            return serialized_orders
        else:
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


def create_order(new_order_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                INSERT INTO Orders VALUES (null, ?, ?, ?)
            """,
            (
                new_order_data["metal_id"],
                new_order_data["style_id"],
                new_order_data["size_id"],
            ),
        )


def delete_order(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Orders
                WHERE Id = ?
                """,
            (primary_key,),
        )
        number_of_rows_deleted = db_cursor.rowcount

        return True if number_of_rows_deleted > 0 else False
