from database.connection import get_connection


def save_booking(booking):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO bookings (
                    customer_id,
                    food_id,
                    quantity,
                    booking_date,
                    booking_time
                )
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id, status, created_at;
                """,
                (
                    booking.customer.id,
                    booking.food.id,
                    booking.quantity,
                    booking.booking_date,
                    booking.booking_time
                )
            )

            booking_data = cursor.fetchone()

        connection.commit()

        if booking_data is None:
            return None

        booking.id = booking_data[0]
        booking.status = booking_data[1]
        booking.created_at = booking_data[2]

        return booking

    finally:
        connection.close()