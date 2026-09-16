from database.connection import get_connection


def create_customer(name, phone):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO customers (name, phone)
                VALUES (%s, %s)
                RETURNING id, name, phone, created_at;
                """,
                (name, phone)
            )

            customer = cursor.fetchone()

        connection.commit()

        return customer

    finally:
        connection.close()