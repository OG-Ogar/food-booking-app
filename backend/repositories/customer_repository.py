from models.customer import Customer
from database.connection import get_connection


def create_customer(name, phone, password_hash):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO customers (name, phone, password_hash)
                VALUES (%s, %s, %s)
                RETURNING id, name, phone, password_hash, created_at;
                """,
                (name, phone, password_hash)
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
            customer_data[4]
        )

    finally:
        connection.close()

def get_customer_by_phone(phone):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT id, name, phone, password_hash created_at
                FROM customers
                WHERE phone = %s;
                """,
                (phone,)
            )

            customer_data = cursor.fetchone()

        if customer_data is None:
            return None

        return Customer(
            customer_data[0],
            customer_data[1],
            customer_data[2],
            customer_data[3]
            customer_data[4]
        )

    finally:
        connection.close()