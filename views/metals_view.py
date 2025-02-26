import sqlite3
import json


def list_metals():
    # creates a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # SQL Query
        db_cursor.execute(
            """
            SELECT 
                m.id, 
                m.metal, 
                m.price 
            FROM Metals m 
            """
        )
        # Stores return from SQL
        query_results = db_cursor.fetchall()

        # Initializes an empty python list
        metals = []
        # Adds SQL list items as Python dictionaries to initial list
        for row in query_results:
            metals.append(dict(row))

        # Serialize metals list into JSON formatting
        serialized_metals = json.dumps(metals)

        return serialized_metals


def retrieve_metal(primary_key):
    # This function will return one list item from the SQL database instead of the whole list of items
    # connects to SQL database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        # retains SQL row in memory, will be used later when converting item to Python
        conn.row_factory = sqlite3.Row
        # method that will select the data in range of the SQL query
        db_cursor = conn.cursor()
        # primary key is required in parameters, evaluates in SQL query
        db_cursor.execute(
            """
            SELECT 
                m.id,
                m.metal,
                m.price
            FROM Metals m
            WHERE m.id = ?
            """,
            (primary_key,),
        )
        # Returns one SQL object by primary key
        query_results = db_cursor.fetchone()
        query_as_dictionary = dict(query_results)
        serialized_python_to_JSON = json.dumps(query_as_dictionary)

        return serialized_python_to_JSON


def update_metal(primary_key, replacement_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    metal = ?,
                    price =  ?
            WHERE Id = ?
            """,
            (replacement_data["metal"], replacement_data["price"], primary_key),
        )

        return True if db_cursor.rowcount > 0 else False


def create_metal(new_metal_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                INSERT INTO Metals (metal, price) VALUES (?, ?)
            """,
            (new_metal_data["metal"], new_metal_data["price"]),
        )


def delete_metal(primary_key):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Metals
                WHERE Id = ?
                """,
            (primary_key,),
        )
        number_of_rows_deleted = db_cursor.rowcount

        return True if number_of_rows_deleted > 0 else False
