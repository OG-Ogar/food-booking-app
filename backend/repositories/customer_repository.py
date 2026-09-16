from models.customer import Customer
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

            customer_data = cursor.fetchone()

        connection.commit()

        if customer_data is None:
            return None

        return Customer(
            customer_data[0],
            customer_data[1],
            customer_data[2],
            customer_data[3]
        )

    finally:
        connection.close()