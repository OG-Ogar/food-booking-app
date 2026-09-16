from models.food import Food
from database.connection import get_connection


def get_foods():

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT id, name, price, category, quantity
                FROM foods
                ORDER BY id;
                """
            )

            food_data = cursor.fetchall()

        return [
            Food(
                food[0],
                food[1],
                food[2],
                food[3],
                food[4]
            )
            for food in food_data
        ]

    finally:
        connection.close()